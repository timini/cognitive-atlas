"""Conditional inference for saved language runs. No model calls or data mutations.

Null: response distributions are exchangeable between languages within each fixed
capital pair. Sample numbers are NOT matched observations. Randomization pools
20 observations per pair and assigns 10 to each language independently per pair.
Conditions are observational prompt variants, not randomly assigned treatments.
Inference assumes independent calls/exchangeability under the null; it does not
sample new cities, prompts, days, or model versions. Complete-case primary analysis
excludes pairs lacking ten valid observations in ANY of the five languages.
Two statistics per comparison: absolute median-matrix disagreement (upper-tail),
and absolute difference in median-based MAE (two-sided). Holm correct all 20 tests.
"""

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

SEED = 20260909
PERMUTATIONS = 4999
BATCH = 40
LANGUAGES = ["en", "fr", "es", "ar", "zh"]


def holm(pvalues):
    p = np.asarray(pvalues)
    order = np.argsort(p)
    adjusted = np.empty_like(p)
    adjusted[order] = np.minimum(1, np.maximum.accumulate(p[order] * (len(p) - np.arange(len(p)))))
    return adjusted


assert np.allclose(holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])
# A single split must preserve observations and sample sizes.
rng = np.random.default_rng(SEED)
toy = np.arange(60).reshape(3, 20)
perm = np.argsort(rng.random((3, 20)), axis=-1)
split = np.take_along_axis(toy, perm, axis=-1)
assert np.array_equal(np.sort(split, axis=-1), toy)
assert split[:, :10].shape == split[:, 10:].shape == (3, 10)

results = {}
sources = {}
for entry in json.loads(Path("paper/experiment-index.json").read_text()):
    path = Path("public") / entry["url"].lstrip("/")
    content = path.read_bytes()
    r = json.loads(content)
    if r["experiment"].get("prompt_family") == "great-circle-formatted-number-v2":
        lang = r["experiment"]["language"]
        assert lang not in results
        results[lang] = r
        sources[lang] = {
            "path": str(path),
            "sha256": hashlib.sha256(content).hexdigest(),
            "experiment_id": r["experiment"]["id"],
        }
assert set(results) == set(LANGUAGES)
base = results["en"]["experiment"]
for r in results.values():
    for field in [
        "model",
        "provider",
        "parameters",
        "dataset_sha256",
        "sampling_count",
        "sampling_strategy",
        "prompt_family",
        "response_parser",
        "entity_name_policy",
    ]:
        assert r["experiment"][field] == base[field], field
    assert r["resolved_model_versions"] == results["en"]["resolved_model_versions"]
pairs = {lang: {p["id"]: p for p in results[lang]["pairs"]} for lang in LANGUAGES}
all_ids = sorted(pairs["en"])
assert all(set(p) == set(all_ids) for p in pairs.values())
kept = [pid for pid in all_ids if all(pairs[lang][pid]["n"] == 10 for lang in LANGUAGES)]
excluded = sorted(set(all_ids) - set(kept))
truth = np.array([pairs["en"][pid]["true_distance_km"] for pid in kept])
x = {lang: np.array([pairs[lang][pid]["samples"] for pid in kept]) for lang in LANGUAGES}
assert all(a.shape == (len(kept), 10) for a in x.values())
medians = {lang: np.median(a, axis=-1) for lang, a in x.items()}
mae = {lang: float(np.mean(np.abs(m - truth))) for lang, m in medians.items()}
report = {
    "seed": SEED,
    "permutations": PERMUTATIONS,
    "model": base["model"],
    "sources": sources,
    "total_pairs": len(all_ids),
    "complete_pairs": len(kept),
    "excluded_pair_ids": excluded,
    "method": __doc__,
    "complete_pair_median_MAE_km": mae,
    "all_pairs_median_MAE_km": {
        lang: results[lang]["layers"]["median"]["metrics"]["mae_km"] for lang in LANGUAGES
    },
    "comparisons": [],
}
print(
    json.dumps({k: v for k, v in report.items() if k not in ["sources", "method", "comparisons"]}), flush=True
)
for ci, (a, b) in enumerate(itertools.combinations(LANGUAGES, 2)):
    rng = np.random.default_rng(SEED + ci)
    pooled = np.concatenate([x[a], x[b]], axis=-1)
    observed_disagreement = float(np.abs(medians[a] - medians[b]).mean())
    observed_accuracy = mae[b] - mae[a]
    null_disagreement = np.empty(PERMUTATIONS)
    null_accuracy = np.empty(PERMUTATIONS)
    for start in range(0, PERMUTATIONS, BATCH):
        count = min(BATCH, PERMUTATIONS - start)
        # IID continuous keys yield uniform permutations independently per pair.
        order = np.argsort(rng.random((count, len(kept), 20)), axis=-1)
        shuffled = np.take_along_axis(pooled[None, :, :], order, axis=-1)
        ma, mb = np.median(shuffled[:, :, :10], axis=-1), np.median(shuffled[:, :, 10:], axis=-1)
        null_disagreement[start : start + count] = np.abs(ma - mb).mean(axis=-1)
        null_accuracy[start : start + count] = np.abs(mb - truth).mean(axis=-1) - np.abs(ma - truth).mean(
            axis=-1
        )
    item = {
        "a": a,
        "b": b,
        "mean_absolute_median_disagreement_km": observed_disagreement,
        "null_disagreement_mean_km": float(null_disagreement.mean()),
        "null_disagreement_95pct_interval_km": np.quantile(null_disagreement, [0.025, 0.975]).tolist(),
        "mae_difference_b_minus_a_km": observed_accuracy,
        "null_accuracy_difference_95pct_interval_km": np.quantile(null_accuracy, [0.025, 0.975]).tolist(),
        "judgment_p": float(
            (1 + np.count_nonzero(null_disagreement >= observed_disagreement - 1e-10)) / (PERMUTATIONS + 1)
        ),
        "accuracy_p": float(
            (1 + np.count_nonzero(np.abs(null_accuracy) >= abs(observed_accuracy) - 1e-10))
            / (PERMUTATIONS + 1)
        ),
        "all_pair_MAE_difference_b_minus_a_km": report["all_pairs_median_MAE_km"][b]
        - report["all_pairs_median_MAE_km"][a],
    }
    report["comparisons"].append(item)
    print(json.dumps(item), flush=True)
# Family includes both questions for all ten pairwise language comparisons.
adjusted = holm([c[key] for c in report["comparisons"] for key in ["judgment_p", "accuracy_p"]])
for i, c in enumerate(report["comparisons"]):
    c["judgment_p_holm_20"] = float(adjusted[2 * i])
    c["accuracy_p_holm_20"] = float(adjusted[2 * i + 1])
report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
Path("paper/results/language-difference-audit.json").write_text(json.dumps(report, indent=2) + "\n")
print("FINISHED; wrote paper/results/language-difference-audit.json", flush=True)
