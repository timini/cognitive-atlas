"""Synthetic method diagnostics, entirely separate from empirical model observations.

Run: .venv/bin/python paper/revision100/calibration.py
Checks the actual local.py empirical variance-adjusted basic bootstrap under known
zero contrasts; never generates, repairs, or substitutes research measurements.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from atlas.inference import holm
from paper.revision100 import local

SEED = 20260914
OUTER_DATASETS = 240
INNER_REPLICATES = 499
PAIR_COUNT = 40
SAMPLES_PER_PAIR = 10
ALPHA = .05
SCENARIOS = ["rounded_tied_regular", "unequal_variances", "rare_extreme_skew", "zero_variance"]


def digest_bytes(value):
    return hashlib.sha256(value).hexdigest()


def binomial_summary(events):
    n = len(events)
    k = int(np.sum(events))
    p = k / n
    z = 1.959963984540054
    den = 1 + z*z/n
    center = (p + z*z/(2*n)) / den
    radius = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
    return {
        "count": k, "denominator": n, "rate": p,
        "binomial_mcse": math.sqrt(p*(1-p)/n),
        "wilson_95_monte_carlo_interval": [center-radius, center+radius],
        "interval_note": "Monte Carlo uncertainty across independent outer datasets, not a research-effect confidence interval. Plug-in MCSE is zero at boundaries; the Wilson interval still has positive width.",
    }


def simulate(rng, scenario):
    # Offsets vary by pair but are identical across conditions, preserving exact
    # equality of condition expectations in every fixed stratum.
    offset = np.arange(PAIR_COUNT, dtype=float)[None, :, None] * 5
    shape = (3, PAIR_COUNT, SAMPLES_PER_PAIR)
    if scenario == "rounded_tied_regular":
        return 100 + offset + 5 * (rng.binomial(8, .5, size=shape)-4)
    if scenario == "unequal_variances":
        scale = np.array([2, 7, 12])[:, None, None]
        return 100 + offset + scale * (rng.binomial(8, .5, size=shape)-4)
    if scenario == "rare_extreme_skew":
        values = np.empty(shape)
        # E[English] = 100 + .001*10000 = 110. Other conditions have the same
        # expectation but frequent symmetric small deviations. Sparse unseen
        # tails are precisely what n=10 empirical resampling cannot identify.
        values[0] = 100 + 10000*rng.binomial(1, .001, size=shape[1:])
        values[1] = 110 + 2*(2*rng.binomial(1, .5, size=shape[1:])-1)
        values[2] = 110 + 4*(2*rng.binomial(1, .5, size=shape[1:])-1)
        return values + offset
    if scenario == "zero_variance":
        return np.broadcast_to(100 + offset, shape).copy()
    raise ValueError(scenario)


def main():
    local_path = Path(local.__file__)
    local_hash_before = digest_bytes(local_path.read_bytes())
    function_names = ["bootstrap_deviations", "summary", "contrast_weights"]
    groups = [np.arange(PAIR_COUNT) < 10, (np.arange(PAIR_COUNT) >= 20) & (np.arange(PAIR_COUNT) < 24)]
    weights = [local.contrast_weights(g)[:, [0, 2]] for g in groups]
    report = {
        "title": "Synthetic calibration diagnostics of the local-contrast bootstrap",
        "status": "Synthetic method validation only; none of these values are LLM observations or empirical geographic findings.",
        "script_sha256": digest_bytes(Path(__file__).read_bytes()),
        "algorithm_source": str(local_path.relative_to(ROOT)),
        "algorithm_source_sha256": local_hash_before,
        "algorithm_function_sha256": {name: digest_bytes(inspect.getsource(getattr(local, name)).encode()) for name in function_names},
        "holm_source_sha256": digest_bytes(inspect.getsource(holm).encode()),
        "software": {"python": platform.python_version(), "numpy": np.__version__},
        "seed": SEED, "outer_independent_datasets_per_scenario": OUTER_DATASETS,
        "inner_empirical_bootstrap_replicates": INNER_REPLICATES,
        "pairs": PAIR_COUNT, "conditions": 3, "samples_per_pair_per_condition": SAMPLES_PER_PAIR,
        "associated_pair_counts": [int(g.sum()) for g in groups],
        "associated_pair_indices_zero_based": [np.flatnonzero(g).tolist() for g in groups],
        "alpha": ALPHA, "pointwise_ci_level": .95, "holm_family_size": 4,
        "true_contrasts": "All four home/interaction contrasts are exactly zero: each condition has the same population mean within every pair.",
        "bootstrap": "Calls local.bootstrap_deviations, local.summary and local.contrast_weights directly. Each resample draws exactly ten observed values with replacement independently in each condition and stratum; deviations receive sqrt(10/9) correction. No Gaussian replacement for empirical resampling.",
        "tests": ["comparator_1_home", "comparator_1_interaction", "comparator_2_home", "comparator_2_interaction"],
        "scenario_definitions": {
            "rounded_tied_regular": "All conditions:100+5*pair_index+5*(Binomial(8,.5)-4); many tied values, equal variances, within-pair mean100+offset.",
            "unequal_variances": "100+5*pair_index+scale*(Binomial(8,.5)-4), condition scales2,7,12; equal means, unequal variances.",
            "rare_extreme_skew": "English100+offset+10000*Bernoulli(.001); comparator1=110+offset+2*Rademacher; comparator2=110+offset+4*Rademacher. All means110+offset. Deliberate unseen-tail stress case, not a fitted model of real responses.",
            "zero_variance": "Every observation is100+5*pair_index in every condition; exact zero contrasts and degenerate intervals.",
        },
        "scenarios": {},
    }
    for si, scenario in enumerate(SCENARIOS):
        rng = np.random.default_rng(np.random.SeedSequence([SEED, si]))
        coverage, rejection, widths, observed, family = [], [], [], [], []
        rare_counts = []
        for iteration in range(OUTER_DATASETS):
            values = simulate(rng, scenario)
            pvalues, covers, interval_widths, estimates = [], [], [], []
            if scenario == "rare_extreme_skew":
                rare_counts.append(int(np.sum(values[0] > 1000)))
            for comparator in range(2):
                a, b = values[0], values[comparator+1]
                obs = (a.mean(axis=1)-b.mean(axis=1)) @ weights[comparator]
                seed = np.random.SeedSequence([SEED, si, iteration, comparator, 991]).generate_state(1)[0]
                deviations = local.bootstrap_deviations(a, b, weights[comparator], INNER_REPLICATES, int(seed))
                for j in range(2):
                    item = local.summary(obs[j], deviations[:, j])
                    lo, hi = item["ci95_km"]
                    covers.append(lo <= 0 <= hi)
                    interval_widths.append(hi-lo)
                    estimates.append(float(obs[j]))
                    pvalues.append(item["p"])
            adjusted = holm(pvalues)
            coverage.append(covers)
            rejection.append(np.asarray(pvalues) <= ALPHA)
            family.append(bool(np.any(adjusted <= ALPHA)))
            widths.append(interval_widths)
            observed.append(estimates)
        coverage = np.asarray(coverage)
        rejection = np.asarray(rejection)
        widths = np.asarray(widths)
        observed = np.asarray(observed)
        result = {
            "pointwise": {name: {
                "coverage_95": binomial_summary(coverage[:, j]),
                "unadjusted_type1_rejection": binomial_summary(rejection[:, j]),
                "mean_interval_width": float(widths[:, j].mean()),
                "mean_estimated_contrast": float(observed[:, j].mean()),
            } for j, name in enumerate(report["tests"])},
            "holm_familywise_type1_rejection": binomial_summary(family),
        }
        if rare_counts:
            result["english_rare_tail_observations_per_outer_dataset_frequency"] = {str(k): rare_counts.count(k) for k in sorted(set(rare_counts))}
            result["outer_datasets_with_no_english_tail_observation"] = sum(k == 0 for k in rare_counts)
        report["scenarios"][scenario] = result
        print(scenario, "coverage", coverage.mean(axis=0).tolist(), "HolmFWER", float(np.mean(family)), flush=True)
    assert digest_bytes(local_path.read_bytes()) == local_hash_before, "Algorithm source changed during diagnostics; rerun"
    report["interpretation"] = [
        "These finite simulation scenarios test actual interval coverage and Type I rejection, extending an analytic-SE agreement check, but cannot prove universal bootstrap validity.",
        "Regular tied and unequal-variance scenarios should be assessed against nominal coverage/rejection with their reported Monte Carlo uncertainty. No automatic pass/fail rule or selection of seeds based on results was used.",
        "The rare-tail stress condition demonstrates a fundamental limitation: empirical n=10 samples may omit a tail that materially contributes to the population mean, causing invalid uncertainty even when variances are algebraically corrected. Its failure is not evidence that real outputs have this tail distribution.",
        "The deterministic zero-variance condition is a boundary case with exact zero contrasts, expected coverage one and rejection zero; nominal95% coverage is not the target for this degenerate case.",
        "Forty fixed synthetic strata and home groups10/4 are diagnostic choices, not replicas of the full4948-pair empirical design. Results do not establish independence of real API samples or population generalization across cities.",
        "Basic intervals and centered-bootstrap two-sided p-values are not exact inversions under skewness. Four-test Holm correction controls a family only insofar as its marginal p-values are valid; it cannot repair an invalid bootstrap null distribution.",
    ]
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
