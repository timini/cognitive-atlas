"""Descriptive map sensitivity to retaining positive out-of-range numeric answers.

Keep the historical v2 whole-response ASCII decimal rule. Do not repair malformed
answers, replace samples, make model calls, or perform new inferential tests.
Only range_geometry.json beside this script is written.
"""

import csv
import hashlib
import importlib.metadata
import json
import math
import os
import platform
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import orthogonal_procrustes

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.reconstruct import RADIUS_KM, spherical, unit_vectors

EXPORTS = {
    "en": "3b382690950b9511f5806ebc-114bbc2e2e5a9331",
    "ar": "b2e583773ba8111b0607ae88-3ef8ee3db9b488b1",
    "zh": "2ee0bcb921b94263ac26e635-bae2d55a858255c4",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_unbounded(raw):
    text = raw.strip()
    if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", text, flags=re.ASCII) is None:
        return None
    value = float(text)
    return value if math.isfinite(value) and value > 0 else None


def map_shift(first_latlon, second_latlon):
    first, second = unit_vectors(first_latlon), unit_vectors(second_latlon)
    rotation = orthogonal_procrustes(first, second)[0]
    rotated = first @ rotation
    angles = np.arctan2(np.linalg.norm(np.cross(rotated, second), axis=1),
                        np.sum(rotated * second, axis=1))
    values = RADIUS_KM * angles
    return {"mean_km": float(values.mean()), "max_km": float(values.max()),
            "per_capital_km": values.tolist(), "orthogonal_rotation": rotation.tolist()}


def main():
    assert parse_unbounded(" 20150\n") == 20150.0
    assert parse_unbounded("264`\n") is None and parse_unbounded("264_\n") is None
    assert all(parse_unbounded(x) is None for x in ["0", "-1", "NaN", "Infinity", "20,150", "20150 km", "1e4", "١٢٣"])
    paths = {language: ROOT / "public/data" / export for language, export in EXPORTS.items()}
    results = {language: json.loads((path / "result.json").read_text()) for language, path in paths.items()}
    places = results["en"]["places"]
    assert len(places) == 100 and all(r["places"] == places for r in results.values())
    ids = {p["id"]: i for i, p in enumerate(places)}
    reference = np.asarray([[p["latitude"], p["longitude"]] for p in places])
    report = {
        "scope": "100-capital descriptive sensitivity: retain finite positive v2-format numeric observations above 20040 km; never repair malformed output",
        "script_sha256": sha256(Path(__file__)),
        "reconstruction_source_sha256": sha256(ROOT / "atlas/reconstruct.py"),
        "sources": {language: {name: {"path": str((path / name).relative_to(ROOT)), "sha256": sha256(path / name)}
                              for name in ["responses.csv", "result.json", "manifest.json"]}
                    for language, path in paths.items()},
        "environment": {"python": sys.version, "platform": platform.platform(),
                        "packages": {name: importlib.metadata.version(name) for name in ["numpy", "scipy", "scikit-learn"]},
                        "thread_environment": {key: os.environ.get(key) for key in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"]}},
        "capitals": 100, "pairs": 4950, "capital_ids": list(ids),
        "parser": {"whole_response_pattern": r"[0-9]+(?:\.[0-9]+)?", "strip_outer_whitespace": True,
                   "additional_rule": "strictly positive finite float; no upper bound", "format_diagnostic_checks_passed": True},
        "reconstruction": {"algorithm": "atlas.reconstruct.spherical", "starts": 4, "seed": 42,
                           "radius_km": RADIUS_KM, "alignment": "single global orthogonal transform with reflection permitted",
                           "stress_definition": "sqrt(sum((fitted-target)^2)/sum(target^2)) over unordered pairs"},
        "cautions": ["Descriptive sensitivity, not a significance test or a new experiment.",
                     "Original observations and quality classifications remain immutable.",
                     "Retaining above-range answers does not assert that those distances are geographically possible.",
                     "Stress uses each analysis condition's own target matrix; both values and the matrix changes are reported."],
        "conditions": {}, "language_pair_map_shifts": [],
    }
    new_maps, accepted_maps = {}, {}
    for language, path in paths.items():
        with (path / "responses.csv").open(newline="") as handle:
            rows = list(csv.DictReader(handle))
        terminal = [row for row in rows if row["terminal"].lower() == "true"]
        slots = {(row["pair_id"], int(row["sample_number"])) for row in terminal}
        assert len(slots) == len(terminal) == 49500
        values, accepted = defaultdict(list), defaultdict(list)
        excluded = []
        reinstated = []
        for row in terminal:
            value = parse_unbounded(row["raw_response"])
            if value is None:
                excluded.append({key: row[key] for key in ["response_id", "pair_id", "sample_number", "raw_response", "quality"]})
                assert row["quality"] != "valid"
                continue
            values[row["pair_id"]].append(value)
            if row["quality"] == "valid":
                assert value == float(row["parsed_distance_km"])
                accepted[row["pair_id"]].append(value)
            else:
                assert value > 20040 and row["quality"] == "beyond_earth_diameter_arc"
                reinstated.append({"response_id": row["response_id"], "pair_id": row["pair_id"],
                                   "sample_number": int(row["sample_number"]), "distance_km": value,
                                   "original_quality": row["quality"]})
        target = np.zeros((100, 100))
        changes = []
        assert len(values) == len(accepted) == len(results[language]["pairs"]) == 4950
        for pair in results[language]["pairs"]:
            pid = pair["id"]
            assert sorted(accepted[pid]) == sorted(pair["samples"])
            median = float(np.median(values[pid]))
            i, j = ids[pair["place_a_id"]], ids[pair["place_b_id"]]
            target[i, j] = target[j, i] = median
            if median != pair["median"]:
                changes.append({"pair_id": pid, "accepted_median_km": pair["median"],
                                "range_retained_median_km": median, "difference_km": median - pair["median"],
                                "accepted_n": len(accepted[pid]), "range_retained_n": len(values[pid])})
        new_map, fit = spherical(target, reference, seed=42, starts=4)
        assert fit["converged"]
        saved = results[language]["layers"]["median"]["reconstructions"]["spherical"]
        shift = map_shift(saved["inferred_latlon"], new_map)
        new_maps[language], accepted_maps[language] = new_map, saved["inferred_latlon"]
        report["conditions"][language] = {
            "raw_attempts": len(rows), "completed_slots": len(terminal),
            "original_quality_counts_completed": dict(Counter(row["quality"] for row in terminal)),
            "accepted_observations": sum(map(len, accepted.values())),
            "range_retained_observations": sum(map(len, values.values())),
            "reinstated_observations": reinstated, "still_excluded_observations": excluded,
            "median_changes": changes, "range_retained_target_max_km": float(target.max()),
            "range_retained_targets_above_fixed_sphere_max_arc": int(np.sum(target[np.triu_indices(100, 1)] > np.pi * RADIUS_KM)),
            "accepted_stress": saved["stress"], "range_retained_stress": fit["stress"],
            "stress_difference": fit["stress"] - saved["stress"],
            "accepted_to_range_retained_map_shift": shift,
            "range_retained_inferred_latlon": new_map.tolist(),
            "fit_converged": fit["converged"], "fit_function_evaluations": fit["function_evaluations"],
        }
        print(json.dumps({"language": language, "reinstated": len(reinstated), "median_changes": changes,
                          "mean_map_shift_km": shift["mean_km"], "max_map_shift_km": shift["max_km"],
                          "range_retained_stress": fit["stress"]}), flush=True)
    chinese = report["conditions"]["zh"]
    assert not chinese["reinstated_observations"] and not chinese["median_changes"]
    assert len(chinese["still_excluded_observations"]) == 4
    assert chinese["accepted_to_range_retained_map_shift"]["max_km"] < 0.001
    assert abs(chinese["stress_difference"]) < 1e-10
    report["unchanged_Mandarin_verification_passed"] = True
    for first, second in combinations(EXPORTS, 2):
        before = map_shift(accepted_maps[first], accepted_maps[second])
        after = map_shift(new_maps[first], new_maps[second])
        comparison = {"first": first, "second": second, "accepted_map_shift": before,
                      "range_retained_map_shift": after, "mean_shift_change_km": after["mean_km"] - before["mean_km"]}
        report["language_pair_map_shifts"].append(comparison)
        print(json.dumps({"first": first, "second": second, "accepted_mean_shift_km": before["mean_km"],
                          "range_retained_mean_shift_km": after["mean_km"]}), flush=True)
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(output, flush=True)


if __name__ == "__main__":
    main()
