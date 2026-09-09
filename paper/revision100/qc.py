"""Independent audit of the frozen 100-capital, formatted-number-v2 observations.

Run from any directory: .venv/bin/python paper/revision100/qc.py
No model calls, published-file mutations, ad hoc format repair, or distributional
independence assumptions. Requires NumPy; output is strict JSON next to this file.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import platform
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
EXPORTS = {
    "en": "3b382690950b9511f5806ebc-114bbc2e2e5a9331",
    "ar": "b2e583773ba8111b0607ae88-3ef8ee3db9b488b1",
    "zh": "2ee0bcb921b94263ac26e635-bae2d55a858255c4",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def parse_v2(raw):
    """Independent exact replay of historical ASCII-decimal acceptance and QC."""
    text = raw.strip()
    if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", text) is None:
        return None, "invalid_numeric_format"
    value = float(text)
    if not math.isfinite(value) or value <= 0:
        return None, "non_positive_or_non_finite"
    if value > 20040:
        return None, "beyond_earth_diameter_arc"
    return value, "valid"


def summary(values):
    x = np.asarray(values, dtype=float)
    if not len(x):
        return {"count": 0}
    return {
        "count": len(x), "mean": float(x.mean()), "median": float(np.median(x)),
        "minimum": float(x.min()), "maximum": float(x.max()),
        "percentiles_5_25_75_95": np.percentile(x, [5, 25, 75, 95]).tolist(),
    }


def accuracy(samples, pair_ids, truth):
    if not pair_ids or any(not samples[p] for p in pair_ids):
        raise ValueError("Empty pair in accuracy calculation")
    med_errors = np.array([np.median(samples[p]) - truth[p] for p in pair_ids])
    pair_expected_errors = [np.mean(np.abs(np.asarray(samples[p]) - truth[p])) for p in pair_ids]
    pooled_errors = [abs(x - truth[p]) for p in pair_ids for x in samples[p]]
    return {
        "pairs": len(pair_ids), "observations": sum(len(samples[p]) for p in pair_ids),
        "pair_median_mae_km": float(np.abs(med_errors).mean()),
        "pair_median_rmse_km": float(np.sqrt(np.mean(med_errors ** 2))),
        "pair_median_signed_error_km": float(med_errors.mean()),
        "single_response_mae_equal_pair_weight_km": float(np.mean(pair_expected_errors)),
        "single_response_mae_pooled_observation_weight_km": float(np.mean(pooled_errors)),
    }


def audit():
    evidence = {
        "title": "Independent 100-capital sampling, parser, and exclusion audit",
        "script_sha256": sha(Path(__file__)),
        "software": {"python": platform.python_version(), "numpy": np.__version__},
        "protocol": "great-circle-formatted-number-v2",
        "parser": "ascii_decimal_v2",
        "methods": {
            "parser_replay": "Independent implementation: strip surrounding whitespace, whole-response ASCII decimal match, finite positive number, <=20040 km. Non-STOP completions are classified refusal_or_truncated after parsing, matching historical runner behavior.",
            "complete_case": "Keep only pairs with exactly ten accepted terminal observations in every language.",
            "numeric_range_retained": "Keep every finite positive terminal STOP response that meets the original v2 ASCII format, including >20040 km; malformed output is not repaired or coerced.",
            "accuracy": "Pair median MAE averages equally over pairs. Single-response MAE is reported both as the equal-pair average of each pair's sample mean absolute error and as the pooled-observation mean.",
            "dispersion": "Sample SD uses ddof=1; CV is sample SD divided by sample mean. Tied/identical counts use exact saved numeric values; ten-valid-pair counts are reported separately.",
            "timing": "Timestamps are recorded before provider dispatch. Within-pair first-to-last timestamps describe clustering; they do not establish response independence, caching, or any causal time effect.",
        },
        "conditions": {}, "source_sha256": {},
    }
    data = {}
    for lang, export in EXPORTS.items():
        directory = ROOT / "public/data" / export
        for name in ["manifest.json", "responses.csv", "pairs.csv", "places.csv", "result.json"]:
            path = directory / name
            evidence["source_sha256"][str(path.relative_to(ROOT))] = sha(path)
        manifest = json.loads((directory / "manifest.json").read_text())
        assert manifest["prompt_family"] == evidence["protocol"]
        assert manifest["response_parser"] == evidence["parser"]
        assert manifest["sampling_count"] == 10 and manifest["language"] == lang
        assert "response_json_schema" not in manifest["parameters"]
        pairs = rows(directory / "pairs.csv")
        truth = {p["id"]: float(p["true_distance_km"]) for p in pairs}
        assert len(truth) == 4950 and len(rows(directory / "places.csv")) == 100
        attempts = rows(directory / "responses.csv")
        terminal = [r for r in attempts if r["terminal"] == "True"]
        slots = Counter((r["pair_id"], int(r["sample_number"])) for r in terminal)
        expected = {(p, n) for p in truth for n in range(10)}
        assert set(slots) == expected and all(n == 1 for n in slots.values())
        assert len({r["response_id"] for r in attempts}) == len(attempts)
        valid, numeric, times = defaultdict(list), defaultdict(list), defaultdict(list)
        invalid, mismatches = [], []
        for r in terminal:
            value, quality = parse_v2(r["raw_response"])
            if r["finish_reason"] != "STOP":
                value, quality = None, "refusal_or_truncated"
            recorded = float(r["parsed_distance_km"]) if r["parsed_distance_km"] else None
            if quality != r["quality"] or value != recorded:
                mismatches.append(r["response_id"])
            if quality == "valid":
                valid[r["pair_id"]].append(value)
            else:
                invalid.append({k: r[k] for k in ["response_id", "pair_id", "sample_number", "attempt", "quality", "raw_response", "finish_reason", "timestamp"]})
            if quality in ("valid", "beyond_earth_diameter_arc"):
                numeric[r["pair_id"]].append(float(r["raw_response"].strip()))
            times[r["pair_id"]].append(datetime.fromisoformat(r["timestamp"]).timestamp())
        assert not mismatches, mismatches
        # Retries are distinct attempt rows, not additional sampled answers.
        attempt_slots = Counter((r["pair_id"], int(r["sample_number"])) for r in attempts)
        first = {}
        for r in attempts:
            slot = (r["pair_id"], int(r["sample_number"]))
            t = datetime.fromisoformat(r["timestamp"]).timestamp()
            first[slot] = min(first.get(slot, t), t)
        first_by_pair = defaultdict(list)
        for (pair, _), t in first.items():
            first_by_pair[pair].append(t)
        starts = [datetime.fromisoformat(r["timestamp"]).timestamp() for r in attempts]
        ordered_pair_starts = np.array([min(first_by_pair[p]) for p in sorted(truth)])
        unique_counts = Counter(len(set(valid[p])) for p in truth)
        complete_unique = Counter(len(set(valid[p])) for p in truth if len(valid[p]) == 10)
        sd = [float(np.std(valid[p], ddof=1)) for p in truth]
        cv = [float(np.std(valid[p], ddof=1) / np.mean(valid[p])) for p in truth]
        counts_by_pair = {}
        for p in sorted(truth):
            subset = [r for r in invalid if r["pair_id"] == p]
            if subset:
                counts_by_pair[p] = {"valid": len(valid[p]), "invalid": len(subset), "quality": dict(Counter(r["quality"] for r in subset)), "true_distance_km": truth[p]}
        condition = {
            "export_id": export, "experiment_id": manifest["id"],
            "model": manifest["model"], "parameters": manifest["parameters"],
            "dataset_sha256": manifest["dataset_sha256"],
            "attempts": len(attempts), "completed_unique_sample_slots": len(slots),
            "valid_observations": sum(map(len, valid.values())),
            "terminal_invalid_observations": len(invalid),
            "additional_nonterminal_attempts": len(attempts) - len(terminal),
            "quality_counts_all_attempts": dict(Counter(r["quality"] for r in attempts)),
            "retry_slots": [{"pair_id": p, "sample_number": n, "attempts": count} for (p, n), count in sorted(attempt_slots.items()) if count > 1],
            "parse_replay_mismatches": mismatches, "terminal_invalid_records": invalid,
            "pairs_with_invalid_observations": counts_by_pair,
            "valid_count_per_pair_frequency": dict(sorted(Counter(map(len, valid.values())).items())),
            "usage_estimated_cost_usd": math.fsum(float(r["estimated_cost_usd"]) for r in attempts),
            "provider_model_versions": dict(Counter(r["model_version"] for r in terminal)),
            "dispersion": {
                "all_valid_pairs_unique_value_count_frequency": dict(sorted(unique_counts.items())),
                "ten_valid_pairs_unique_value_count_frequency": dict(sorted(complete_unique.items())),
                "ten_valid_pairs_all_ten_identical": complete_unique[1],
                "ten_valid_pairs_with_any_tie": sum(v for k, v in complete_unique.items() if k < 10),
                "sample_sd_km": summary(sd), "coefficient_of_variation": summary(cv),
            },
            "timing": {
                "first_attempt_timestamp": min(r["timestamp"] for r in attempts),
                "last_attempt_timestamp": max(r["timestamp"] for r in attempts),
                "dispatch_window_seconds": max(starts) - min(starts),
                "first_attempt_within_pair_span_seconds": summary([max(t) - min(t) for t in first_by_pair.values()]),
                "terminal_attempt_within_pair_span_seconds": summary([max(t) - min(t) for t in times.values()]),
                "canonical_pair_order_adjacent_first_dispatch_reversals": int(np.sum(np.diff(ordered_pair_starts) < 0)),
                "canonical_pair_order_adjacent_first_dispatch_gap_seconds": summary(np.diff(ordered_pair_starts)),
                "manifest_sampling_strategy": manifest["sampling_strategy"],
            },
        }
        evidence["conditions"][lang] = condition
        data[lang] = {"valid": valid, "numeric": numeric, "truth": truth}
    assert len({c["dataset_sha256"] for c in evidence["conditions"].values()}) == 1
    keys = sorted(data["en"]["truth"])
    assert all(data[lang]["truth"] == data["en"]["truth"] for lang in data)
    complete = [p for p in keys if all(len(data[lang]["valid"][p]) == 10 for lang in data)]
    numeric_complete = [p for p in keys if all(len(data[lang]["numeric"][p]) == 10 for lang in data)]
    evidence["common_exclusions"] = {
        "complete_case_pairs": len(complete), "complete_case_excluded_pair_ids": sorted(set(keys) - set(complete)),
        "numeric_range_retained_complete_case_pairs": len(numeric_complete),
        "numeric_range_retained_complete_case_excluded_pair_ids": sorted(set(keys) - set(numeric_complete)),
        "valid_observations_omitted_by_complete_case_rule": sum(len(data[lang]["valid"][p]) for lang in data for p in set(keys) - set(complete)),
        "complete_case_observations_all_languages": len(complete) * 10 * 3,
        "numeric_range_retained_complete_case_observations_all_languages": len(numeric_complete) * 10 * 3,
    }
    for lang, d in data.items():
        evidence["conditions"][lang]["accuracy"] = {
            "all_pairs_accepted": accuracy(d["valid"], keys, d["truth"]),
            "common_complete_case_accepted": accuracy(d["valid"], complete, d["truth"]),
            "all_pairs_numeric_range_retained": accuracy(d["numeric"], keys, d["truth"]),
            "common_complete_case_numeric_range_retained": accuracy(d["numeric"], numeric_complete, d["truth"]),
        }
        published = json.loads((ROOT / "public/data" / EXPORTS[lang] / "result.json").read_text())
        expected_mae = published["layers"]["median"]["metrics"]["mae_km"]
        replay_mae = evidence["conditions"][lang]["accuracy"]["all_pairs_accepted"]["pair_median_mae_km"]
        assert math.isclose(expected_mae, replay_mae, rel_tol=0, abs_tol=1e-9)
        evidence["conditions"][lang]["published_median_mae_replay_absolute_difference_km"] = abs(expected_mae - replay_mae)
    evidence["sensitivity_language_contrasts"] = {}
    for scenario in evidence["conditions"]["en"]["accuracy"]:
        contrasts = {}
        for a, b in [("en", "ar"), ("en", "zh"), ("ar", "zh")]:
            metrics_a = evidence["conditions"][a]["accuracy"][scenario]
            metrics_b = evidence["conditions"][b]["accuracy"][scenario]
            contrasts[f"{b}_minus_{a}"] = {
                "pair_median_mae_difference_km": metrics_b["pair_median_mae_km"] - metrics_a["pair_median_mae_km"],
                "single_response_mae_equal_pair_weight_difference_km": metrics_b["single_response_mae_equal_pair_weight_km"] - metrics_a["single_response_mae_equal_pair_weight_km"],
                "interpretation": "Positive means the first-named language has larger error. Descriptive sensitivity only; no p-value or confidence interval computed here.",
            }
        evidence["sensitivity_language_contrasts"][scenario] = contrasts
    evidence["totals"] = {field: sum(c[field] for c in evidence["conditions"].values()) for field in ["attempts", "completed_unique_sample_slots", "valid_observations", "terminal_invalid_observations", "additional_nonterminal_attempts", "usage_estimated_cost_usd"]}
    return evidence


if __name__ == "__main__":
    report = audit()
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "totals": report["totals"], "common_exclusions": report["common_exclusions"]}, indent=2, allow_nan=False))
