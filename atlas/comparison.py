"""Descriptive comparisons on identical entity sets. No causal or significance claims."""
import json
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.stats import pearsonr, spearmanr

from atlas.data import digest
from atlas.reconstruct import RADIUS_KM, unit_vectors


def compare_results(a, b, aggregation="median"):
    if [p["id"] for p in a["places"]] != [p["id"] for p in b["places"]]:
        raise ValueError("Models must use the same ordered capital set")
    if a["experiment"]["dataset_sha256"] != b["experiment"]["dataset_sha256"]:
        raise ValueError("Dataset versions differ")
    pairs_a = {p["id"]: p[aggregation] for p in a["pairs"]}
    pairs_b = {p["id"]: p[aggregation] for p in b["pairs"]}
    if pairs_a.keys() != pairs_b.keys():
        raise ValueError("Pair sets differ")
    x = np.array([pairs_a[k] for k in sorted(pairs_a)])
    y = np.array([pairs_b[k] for k in sorted(pairs_a)])
    ra = a["layers"][aggregation]["reconstructions"]["spherical"]
    rb = b["layers"][aggregation]["reconstructions"]["spherical"]
    xa, xb = unit_vectors(ra["inferred_latlon"]), unit_vectors(rb["inferred_latlon"])
    rotation, _ = orthogonal_procrustes(xb, xa)
    displacement = RADIUS_KM * np.arccos(np.clip(np.sum(xa * (xb @ rotation), axis=1), -1, 1))
    return {"model_a": a["experiment"]["model"], "model_b": b["experiment"]["model"],
            "aggregation": aggregation, "pearson": float(pearsonr(x, y).statistic),
            "spearman": float(spearmanr(x, y).statistic),
            "mean_absolute_distance_disagreement_km": float(np.abs(x - y).mean()),
            "mean_aligned_map_displacement_km": float(displacement.mean()),
            "max_aligned_map_displacement_km": float(displacement.max())}


def export_comparisons(public="public/data"):
    public = Path(public)
    entries = json.loads((public / "experiments.json").read_text())
    results = {e["id"]: json.loads((public / e["id"] / "result.json").read_text()) for e in entries}
    cohorts = {}
    for entry in entries:
        r = results[entry["id"]]
        e = r["experiment"]
        # Different model thinking controls are retained and disclosed, not collapsed.
        key = digest({"dataset": e["dataset_sha256"], "language": e["language"],
                      "prompt": e["prompt_template"], "samples": e["sampling_count"],
                      "temperature": e["parameters"]["temperature"], "top_p": e["parameters"]["top_p"],
                      "max_tokens": e["parameters"]["max_tokens"]})
        cohort = cohorts.setdefault(key, {"id": key, "capital_count": len(r["places"]),
                                         "language": e["language"], "models": [], "pairwise": []})
        cohort["models"].append({"export_id": entry["id"], "experiment_id": e["id"], "model": e["model"],
                                  "label": e.get("model_label", e["model"]), "parameters": e["parameters"],
                                  "valid_samples": r["quality"]["valid"],
                                  "aggregations": {name: {**layer["metrics"],
                                      "spherical_stress": layer["reconstructions"]["spherical"]["stress"],
                                      "mean_displacement_km": layer["reconstructions"]["spherical"]["mean_displacement_km"]}
                                      for name, layer in r["layers"].items()}})
    for cohort in cohorts.values():
        for a, b in combinations(cohort["models"], 2):
            for name in ["mean", "median", "trimmed_mean", "robust"]:
                cohort["pairwise"].append(compare_results(results[a["export_id"]], results[b["export_id"]], name))
    result = {"schema_version": 1, "cohorts": list(cohorts.values()),
              "note": "Descriptive comparisons. Gemini 2.5 thinking budget 0 and Gemini 3 minimal thinking are different controls; minimal does not guarantee zero thinking."}
    target = public / "comparisons.json"
    tmp = target.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False))
    tmp.replace(target)
    return target
