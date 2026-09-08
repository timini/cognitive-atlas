import json
import shutil
from pathlib import Path

import numpy as np
from scipy.spatial.distance import pdist, squareform

from atlas.data import digest, load_places, read_csv, write_csv
from atlas.deformation import mesh, projected, warp_points
from atlas.reconstruct import align_planar, classical, dimensionality, planar, spherical, stress
from atlas.runner import history
from atlas.statistics import aggregate, bootstrap_interval, metrics

AGGREGATIONS = ["mean", "median", "trimmed_mean", "robust"]


def analyze(directory, seed=42, bootstrap=1000):
    directory = Path(directory)
    manifest = json.loads((directory / "manifest.json").read_text())
    places, pairs, responses = load_places(directory / "places.csv"), read_csv(directory / "pairs.csv"), history(directory)
    if len([r for r in responses if r["terminal"] == "True"]) != len(pairs) * manifest["sampling_count"]:
        raise ValueError("Run incomplete. Complete collection before publishing a research result.")
    ids = {p["id"]: i for i, p in enumerate(places)}
    n = len(places)
    truth = np.zeros((n, n))
    matrices = {a: np.zeros((n, n)) for a in AGGREGATIONS}
    statistics = []
    rng = np.random.default_rng(seed)
    for pair in pairs:
        observations = [r for r in responses if r["pair_id"] == pair["id"] and r["quality"] == "valid"]
        if len({r["sample_number"] for r in observations}) != len(observations):
            raise ValueError("Duplicate accepted sample")
        values = [float(r["parsed_distance_km"]) for r in observations]
        if not values:
            raise ValueError(f"Missing valid distances for {pair['id']}; no imputation is permitted")
        summary = aggregate(values)
        true = float(pair["true_distance_km"])
        i, j = ids[pair["place_a_id"]], ids[pair["place_b_id"]]
        truth[i, j] = truth[j, i] = true
        for a in AGGREGATIONS:
            matrices[a][i, j] = matrices[a][j, i] = summary[a]
        lo, hi = bootstrap_interval(values, rng, bootstrap)
        statistics.append({**pair, "true_distance_km": true, **summary, "samples": values,
                           "missing_samples": manifest["sampling_count"] - len(values),
                           "mean_ci_low": lo, "mean_ci_high": hi,
                           "absolute_error_km": abs(summary["mean"] - true),
                           "signed_error_km": summary["mean"] - true,
                           "relative_error": (summary["mean"] - true) / true,
                           "log_ratio_error": float(np.log(summary["mean"] / true))})
    params = {"seed": seed, "bootstrap_pair_replicates": bootstrap, "algorithm_version": 1}
    analysis_id = digest({"responses": responses, "parameters": params})[:16]
    out = directory / "analyses" / analysis_id
    if (out / "result.json").exists():
        return out
    out.mkdir(parents=True, exist_ok=True)
    write_csv(out / "pair_statistics.csv", [{k: v for k, v in s.items() if k != "samples"} for s in statistics])
    latlon = np.array([[p["latitude"], p["longitude"]] for p in places])
    reference = projected(latlon)
    layers = {}
    coords_rows = []
    world = json.loads(Path("public/data/world.json").read_text())
    for name, d in matrices.items():
        summary = metrics(d, truth)
        for matrix_name, matrix in [(name, d), ("truth", truth)]:
            write_csv(out / f"matrix-{matrix_name}.csv", [
                {"place_id": p["id"], **{q["id"]: matrix[i, j] for j, q in enumerate(places)}}
                for i, p in enumerate(places)])
        inferred, sphere_detail = spherical(d, latlon, seed)
        control_mesh = mesh(latlon, inferred)
        countries = []
        for f in world["features"]:
            polys = [f["geometry"]["coordinates"]] if f["geometry"]["type"] == "Polygon" else f["geometry"]["coordinates"]
            rings = []
            for poly in polys:
                for ring in poly:
                    dense = []
                    for a, b in zip(ring[:-1], ring[1:]):
                        a, b = np.array(a), np.array(b)
                        steps = max(1, int(np.ceil(np.linalg.norm(b - a) / 1.5)))
                        dense.extend(a + (b - a) * t / steps for t in range(steps))
                    dense.append(np.array(ring[-1]))
                    source = np.array(dense) * [1, -1]
                    target = warp_points(source, control_mesh)
                    rings.append({"source": source.round(5).tolist(), "target": target.round(5).tolist()})
            countries.append({"name": f["properties"]["name"], "rings": rings})
        sphere_xy = projected(inferred)
        sphere_xy[:, 0] = reference[:, 0] + (sphere_xy[:, 0] - reference[:, 0] + 180) % 360 - 180
        reconstructions = {"spherical": {"coordinates": sphere_xy.tolist(), "inferred_latlon": inferred.tolist(),
                                         **sphere_detail}}
        for algorithm in ["classical", "metric", "nonmetric"]:
            if algorithm == "classical":
                coords = classical(d)
                detail = {"stress": stress(squareform(pdist(coords)), d), "stress_definition": "normalized_distance_residual"}
            else:
                coords, detail = planar(d, metric=algorithm == "metric", seed=seed)
            aligned, alignment = align_planar(coords, reference)
            reconstructions[algorithm] = {"coordinates": aligned.tolist(), "raw_coordinates": coords.tolist(),
                                          "alignment": alignment, **detail}
        capital_metrics = []
        for p in places:
            related = [s for s in statistics if p["id"] in (s["place_a_id"], s["place_b_id"])]
            capital_metrics.append({"place_id": p["id"], "mae_km": float(np.mean([abs(s[name] - s["true_distance_km"]) for s in related])),
                                    "mean_cv": float(np.mean([s["cv"] for s in related if s["cv"] is not None])),
                                    "mean_std_km": float(np.mean([s["std"] for s in related if s["std"] is not None]))})
        for algorithm, result in reconstructions.items():
            for i, p in enumerate(places):
                coords_rows.append({"aggregation": name, "algorithm": algorithm, "place_id": p["id"],
                                    "aligned_x": result["coordinates"][i][0], "aligned_y": result["coordinates"][i][1],
                                    "inferred_lat": inferred[i, 0] if algorithm == "spherical" else None,
                                    "inferred_lon": inferred[i, 1] if algorithm == "spherical" else None,
                                    "displacement_km": sphere_detail["displacement_km"][i] if algorithm == "spherical" else None})
        layers[name] = {"metrics": summary, "reconstructions": reconstructions,
                        "dimensionality": dimensionality(d, seed=seed), "capital_metrics": capital_metrics,
                        "mesh": control_mesh, "countries": countries}
    write_csv(out / "coordinates.csv", coords_rows)
    result = {"experiment": manifest, "analysis_id": analysis_id, "analysis_parameters": params,
              "places": places, "pairs": statistics, "layers": layers,
              "quality": {"attempts": len(responses), "valid": sum(r["quality"] == "valid" for r in responses),
                          "invalid_attempts": sum(r["quality"] != "valid" for r in responses),
                          "estimated_cost_usd": sum(float(r["estimated_cost_usd"]) for r in responses)},
              "limitations": ["20 capitals are a purposive pilot, not a representative global sample.",
                              "Behavioral judgments do not reveal a literal hidden neural representation.",
                              "Planar MDS stress includes the difficulty of flattening a spherical world.",
                              "Coastline deformation is illustrative and may fold; inspect raw capitals.",
                              "Identical answers at this sampling condition do not establish epistemic certainty.",
                              "Pair bootstrap intervals condition on observed samples; no positional confidence ellipses are claimed."]}
    (out / "result.json").write_text(json.dumps(result, ensure_ascii=False, allow_nan=False, separators=(",", ":")))
    return out


def export(directory, analysis_dir, public="public/data"):
    directory, analysis_dir, public = Path(directory), Path(analysis_dir), Path(public)
    result = json.loads((analysis_dir / "result.json").read_text())
    name = result["experiment"]["id"] + "-" + result["analysis_id"]
    target = public / name
    target.mkdir(parents=True, exist_ok=True)
    for src in [directory / "manifest.json", directory / "responses.csv", directory / "places.csv", directory / "pairs.csv",
                *analysis_dir.glob("*.csv"), analysis_dir / "result.json"]:
        dest = target / src.name
        if dest.exists() and dest.read_bytes() != src.read_bytes():
            raise ValueError("Refusing to overwrite an immutable export")
        shutil.copyfile(src, dest)
    index_path = public / "experiments.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else []
    item = {"id": name, "model": result["experiment"]["model"], "language": result["experiment"]["language"],
            "created_at": result["experiment"]["created_at"], "url": f"/data/{name}/result.json"}
    if not any(x["id"] == name for x in index):
        index.append(item)
    tmp = index_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(index, indent=2))
    tmp.replace(index_path)
    return target
