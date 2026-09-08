"""Read-only audit of published observations; one-sided city-label permutation baseline."""

import json
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.stats import rankdata, spearmanr

SEED, PERMUTATIONS = 20260908, 9999
reports = []
for entry in json.loads(Path("paper/experiment-index.json").read_text()):
    if entry.get("capital_count") != 50:
        continue
    result = json.loads((Path("public") / entry["url"].lstrip("/")).read_text())
    if result["experiment"].get("prompt_family") == "great-circle-formatted-number-v2":
        continue
    pairs, places = result["pairs"], result["places"]
    ids = {p["id"]: i for i, p in enumerate(places)}
    n = len(places)
    upper = np.triu_indices(n, 1)
    estimated, truth = np.zeros((n, n)), np.zeros((n, n))
    for pair in pairs:
        i, j = ids[pair["place_a_id"]], ids[pair["place_b_id"]]
        estimated[i, j] = estimated[j, i] = pair["median"]
        truth[i, j] = truth[j, i] = pair["true_distance_km"]
    x, y = rankdata(estimated[upper]), rankdata(truth[upper])
    x, y = x - x.mean(), y - y.mean()
    denominator = np.linalg.norm(x) * np.linalg.norm(y)
    observed = float(x @ y / denominator)
    assert np.isclose(observed, spearmanr(estimated[upper], truth[upper]).statistic)
    ranked = np.zeros((n, n))
    ranked[upper] = x
    ranked[(upper[1], upper[0])] = x
    rng = np.random.default_rng(SEED)
    shuffled = np.empty(PERMUTATIONS)
    for k in range(PERMUTATIONS):
        permutation = rng.permutation(n)
        shuffled[k] = ranked[permutation[upper[0]], permutation[upper[1]]] @ y / denominator
        if k == 0:
            assert np.isclose(
                shuffled[k],
                spearmanr(estimated[permutation[upper[0]], permutation[upper[1]]], truth[upper]).statistic,
            )
    exceedances = int(np.sum(shuffled >= observed))
    unique = [len(set(p["samples"])) for p in pairs]
    full = [p for p in pairs if p["n"] == 10]
    london = next(p for p in pairs if p["id"] == "FR--GB")
    report = {
        "model": entry["model"],
        "source": entry["url"],
        "pairs": len(pairs),
        "spearman": observed,
        "mean_absolute_error_km": result["layers"]["median"]["metrics"]["mae_km"],
        "city_label_permutations": PERMUTATIONS,
        "seed": SEED,
        "exceedances": exceedances,
        "one_sided_permutation_p": (exceedances + 1) / (PERMUTATIONS + 1),
        "shuffled_correlation_range": [float(shuffled.min()), float(shuffled.max())],
        "shuffled_mean": float(shuffled.mean()),
        "full_ten_sample_pairs": len(full),
        "all_ten_identical_pairs": sum(len(set(p["samples"])) == 1 for p in full),
        "unique_answers_per_pair": dict(sorted(Counter(unique).items())),
        "median_within_pair_cv_percent": float(np.median([p["cv"] for p in pairs]) * 100),
        "p90_within_pair_cv_percent": float(np.quantile([p["cv"] for p in pairs], 0.9) * 100),
        "london_paris": {"true_km": london["true_distance_km"], "samples": london["samples"]},
    }
    reports.append(report)
    print(json.dumps(report), flush=True)
Path("paper/results/distance-structure-audit.json").write_text(json.dumps(reports, indent=2))
