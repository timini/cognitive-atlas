from itertools import combinations

import numpy as np
from scipy import stats
from scipy.optimize import least_squares


def aggregate(values):
    x = np.asarray(values, dtype=float)
    if not len(x) or not np.isfinite(x).all() or (x <= 0).any():
        raise ValueError("Need positive finite observations")
    med = float(np.median(x))
    mad = float(np.median(np.abs(x - med)))
    # Scale floor avoids dividing by zero for repeated identical model answers.
    scale = max(1.4826 * mad, 1.0)
    robust = least_squares(lambda m: (x - m[0]) / scale, [med], loss="huber").x[0]
    q1, q3 = np.quantile(x, [0.25, 0.75])
    mean = float(x.mean())
    std = float(x.std(ddof=1)) if len(x) > 1 else None
    return {"n": len(x), "mean": mean, "median": med, "trimmed_mean": float(stats.trim_mean(x, 0.1)),
            "robust": float(robust), "std": std, "variance": std ** 2 if std is not None else None,
            "min": float(x.min()), "max": float(x.max()), "q1": float(q1), "q3": float(q3),
            "iqr": float(q3 - q1), "mad": mad, "cv": std / mean if std is not None else None,
            "outliers": int(((x < q1 - 1.5 * (q3 - q1)) | (x > q3 + 1.5 * (q3 - q1))).sum())}


def triangle_metrics(d, max_triples=200000, seed=42):
    n = len(d)
    total = n * (n - 1) * (n - 2) // 6
    if total <= max_triples:
        triples = np.asarray(list(combinations(range(n), 3)))
    else:
        rng = np.random.default_rng(seed)
        triples = np.asarray([rng.choice(n, 3, replace=False) for _ in range(max_triples)])
    sides = np.sort(np.stack([d[triples[:, 0], triples[:, 1]], d[triples[:, 0], triples[:, 2]],
                              d[triples[:, 1], triples[:, 2]]], axis=1), axis=1)
    excess = np.maximum(0, sides[:, 2] - sides[:, :2].sum(axis=1))
    return {"tested_triangles": len(triples), "total_triangles": total,
            "triangle_violation_rate": float((excess > 1e-7).mean()),
            "triangle_mean_excess_km": float(excess.mean()), "triangle_max_excess_km": float(excess.max()),
            "triangle_sampling": "all" if total <= max_triples else "uniform_with_replacement",
            "triangle_seed": seed}


def metrics(d, truth):
    upper = np.triu_indices(len(d), 1)
    x, y = d[upper], truth[upper]
    error = x - y
    centered = np.eye(len(d)) - np.ones_like(d) / len(d)
    eig = np.linalg.eigvalsh(-0.5 * centered @ (d ** 2) @ centered)
    spherical_eig = np.linalg.eigvalsh(np.cos(d / 6371.0088))
    k = min(3, len(d) - 1)
    nn = np.mean([len(set(np.argsort(d[i])[1:k + 1]) & set(np.argsort(truth[i])[1:k + 1])) / k
                  for i in range(len(d))])
    return {"mae_km": float(abs(error).mean()), "rmse_km": float(np.sqrt(np.mean(error ** 2))),
            "median_absolute_error_km": float(np.median(abs(error))),
            "mean_absolute_relative_error": float(np.mean(abs(error) / y)),
            "signed_error_km": float(error.mean()), "pearson": float(stats.pearsonr(x, y).statistic),
            "spearman": float(stats.spearmanr(x, y).statistic), "kendall": float(stats.kendalltau(x, y).statistic),
            "nearest_neighbor_preservation_k3": float(nn),
            "euclidean_negative_eigenmass": float(abs(eig[eig < 0]).sum() / abs(eig).sum()),
            "spherical_negative_eigenmass": float(abs(spherical_eig[spherical_eig < 0]).sum() / abs(spherical_eig).sum()),
            "symmetry": "imposed_by_unordered_design_not_tested", **triangle_metrics(d)}


def bootstrap_interval(values, rng, count=1000):
    x = np.asarray(values)
    if len(x) < 2:
        return [None, None]
    draws = rng.choice(x, (count, len(x)), replace=True).mean(axis=1)
    return np.quantile(draws, [0.025, 0.975]).tolist()
