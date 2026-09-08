"""Descriptive comparisons on identical entity sets. No causal or significance claims."""
import json
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.stats import pearsonr, spearmanr

from atlas.data import digest
from atlas.languages import ENTITY_NAME_POLICY, LANGUAGE_LABELS, PARSER_ID, PROMPTS, PROTOCOL_ID
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
            "experiment_a": a["experiment"]["id"], "experiment_b": b["experiment"]["id"],
            "language_a": a["experiment"]["language"], "language_b": b["experiment"]["language"],
            "aggregation": aggregation, "pearson": float(pearsonr(x, y).statistic),
            "spearman": float(spearmanr(x, y).statistic),
            "mean_absolute_distance_disagreement_km": float(np.abs(x - y).mean()),
            "mean_aligned_map_displacement_km": float(displacement.mean()),
            "max_aligned_map_displacement_km": float(displacement.max())}


def language_condition(result):
    """Only registered equivalent prompt conditions may enter a language cohort."""
    e = result["experiment"]
    if (e.get("prompt_family") != PROTOCOL_ID or
        e.get("response_parser") != PARSER_ID or
        e.get("entity_name_policy") != ENTITY_NAME_POLICY or
        e["prompt_template"] != PROMPTS.get(e["language"])):
        return None
    return {"dataset": e["dataset_sha256"], "model": e["model"], "provider": e["provider"],
            "resolved_versions": result["resolved_model_versions"], "parameters": e["parameters"],
            "samples": e["sampling_count"], "sampling_strategy": e["sampling_strategy"],
            "prompt_family": PROTOCOL_ID, "response_parser": PARSER_ID,
            "entity_names": ENTITY_NAME_POLICY, "analysis_parameters": result["analysis_parameters"]}


def comparison_row(entry, result, language=False):
    e = result["experiment"]
    return {"export_id": entry["id"], "experiment_id": e["id"], "model": e["model"],
            "language": e["language"], "label": LANGUAGE_LABELS[e["language"]] if language else e.get("model_label", e["model"]),
            "parameters": e["parameters"], "prompt_template": e["prompt_template"],
            "valid_samples": result["quality"]["valid"],
            "expected_samples": len(result["pairs"]) * e["sampling_count"],
            "aggregations": {name: {**layer["metrics"],
                "spherical_stress": layer["reconstructions"]["spherical"]["stress"],
                "mean_displacement_km": layer["reconstructions"]["spherical"]["mean_displacement_km"]}
                for name, layer in result["layers"].items()}}


def export_comparisons(public="public/data"):
    public = Path(public)
    entries = json.loads((public / "experiments.json").read_text())
    results = {e["id"]: json.loads((public / e["id"] / "result.json").read_text()) for e in entries}
    cohorts, language_cohorts = {}, {}
    for entry in entries:
        r = results[entry["id"]]
        e = r["experiment"]
        key = digest({"dataset": e["dataset_sha256"], "language": e["language"],
                      "prompt": e["prompt_template"], "samples": e["sampling_count"],
                      "temperature": e["parameters"]["temperature"], "top_p": e["parameters"]["top_p"],
                      "max_tokens": e["parameters"]["max_tokens"], "response_parser": e.get("response_parser", "legacy")})
        cohort = cohorts.setdefault(key, {"id": key, "capital_count": len(r["places"]),
                                         "language": e["language"], "models": [], "pairwise": []})
        cohort["models"].append(comparison_row(entry, r))
        condition = language_condition(r)
        if condition:
            key = digest(condition)
            cohort = language_cohorts.setdefault(key, {"id": key, "capital_count": len(r["places"]),
                "model_label": e.get("model_label", e["model"]), "condition": condition,
                "models": [], "pairwise": []})
            cohort["models"].append(comparison_row(entry, r, language=True))
    for cohort in [*cohorts.values(), *language_cohorts.values()]:
        for a, b in combinations(cohort["models"], 2):
            for name in ["mean", "median", "trimmed_mean", "robust"]:
                cohort["pairwise"].append(compare_results(results[a["export_id"]], results[b["export_id"]], name))
    for cohort in language_cohorts.values():
        cohort["models"].sort(key=lambda row: list(LANGUAGE_LABELS).index(row["language"]))
    result = {"schema_version": 2, "cohorts": list(cohorts.values()),
              "language_cohorts": list(language_cohorts.values()),
              "note": "Descriptive comparisons. Gemini 2.5 thinking budget 0 and Gemini 3 minimal thinking are different controls; minimal does not guarantee zero thinking.",
              "language_note": "Same model version, generation settings, entities, parser and prompt family. Only instruction language changes. Translations were assistant-authored, without independent native-speaker validation. English is a freshly collected matched-format baseline, separate from earlier experiments. Differences include possible translation effects; no significance claim."}
    target = public / "comparisons.json"
    tmp = target.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, indent=2, allow_nan=False))
    tmp.replace(target)
    return target
