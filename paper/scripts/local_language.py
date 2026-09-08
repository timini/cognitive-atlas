"""Exploratory local-language accuracy; fixed capitals, empirical within-pair bootstrap.

Primary estimand is expected absolute error of ONE response, not error of the
median of ten. This smooth estimand avoids nonregular bootstrap behavior of
heavily tied sample medians. Gain = English error minus translated-prompt error.
Home means at least one endpoint belongs to the explicit language-affinity group.
Interaction = gain on home pairs minus gain on other pairs. Country groups are
an operational proxy; they do not describe every resident's language. Only
repeated-call uncertainty is estimated, never uncertainty over countries/prompts.
"""

import hashlib
import json
from pathlib import Path

import numpy as np

GROUPS = {
    "fr": ["CA", "CD", "FR", "SN"],
    "es": ["AR", "CL", "CO", "ES", "MX", "PE"],
    "ar": ["DZ", "EG", "MA", "SA"],
    "zh": ["CN", "SG"],
}
SEED, REPLICATES = 20260910, 9999


def holm(pvalues):
    p = np.asarray(pvalues)
    order = np.argsort(p)
    adjusted = np.empty_like(p)
    adjusted[order] = np.minimum(1, np.maximum.accumulate(p[order] * (len(p) - np.arange(len(p)))))
    return adjusted


def contrast_weights(home):
    home = np.asarray(home, dtype=bool)
    if not home.any() or home.all():
        raise ValueError("Both home and comparison pairs are required")
    wh = home / home.sum()
    wo = (~home) / (~home).sum()
    return np.column_stack([wh, wo, wh - wo])


def interval_and_p(observed, deviations):
    q = np.quantile(deviations, [0.025, 0.975])
    return {
        "gain_km": float(observed),
        "ci95_km": [float(observed - q[1]), float(observed - q[0])],
        "p": float(
            (1 + np.count_nonzero(np.abs(deviations) >= abs(observed) - 1e-10)) / (len(deviations) + 1)
        ),
    }


def main():
    previous = json.loads(Path("paper/results/language-difference-audit.json").read_text())
    r = {}
    sources = previous["sources"]
    for lang, source in sources.items():
        raw = Path(source["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == source["sha256"]
        r[lang] = json.loads(raw)
    pairs = {l: {p["id"]: p for p in value["pairs"]} for l, value in r.items()}
    ids = sorted(set(pairs["en"]) - set(previous["excluded_pair_ids"]))
    endpoints = np.array([pid.split("--") for pid in ids])
    truth = np.array([pairs["en"][pid]["true_distance_km"] for pid in ids])
    values = {l: np.array([pairs[l][pid]["samples"] for pid in ids]) for l in r}
    assert all(x.shape == (len(ids), 10) for x in values.values())
    errors = {l: np.abs(x - truth[:, None]) for l, x in values.items()}
    mean_errors = {l: x.mean(axis=1) for l, x in errors.items()}
    report = {
        "method": __doc__,
        "seed": SEED,
        "replicates": REPLICATES,
        "groups": GROUPS,
        "sources": sources,
        "excluded_pair_ids": previous["excluded_pair_ids"],
        "complete_pairs": len(ids),
        "results": [],
        "bootstrap": "Resample independently within pair and language; centered deviations; sqrt(10/9) finite-sample variance correction; basic pointwise 95% intervals; two-sided Monte Carlo p; Holm across 8 tests (home gain and interaction for each of 4 languages).",
        "classification": "Official national or co-official language, plus majority Spanish-language countries; fixed before inspecting local-language results. French operational group excludes Algeria/Morocco; bilingual Canada and Singapore included. No claim of monolingual cities.",
    }
    for li, (lang, group) in enumerate(GROUPS.items()):
        home = np.isin(endpoints, group).any(axis=1)
        weights = contrast_weights(home)
        gain = mean_errors["en"] - mean_errors[lang]
        observed = gain @ weights
        rng = np.random.default_rng(SEED + li)
        deviations = np.empty((REPLICATES, 3))
        for start in range(0, REPLICATES, 50):
            count = min(50, REPLICATES - start)
            draws = []
            for l in ["en", lang]:
                indices = rng.integers(0, 10, size=(count, len(ids), 10))
                draws.append(
                    np.take_along_axis(errors[l][None, :, :], indices, axis=-1).mean(axis=-1) - mean_errors[l]
                )
            deviations[start : start + count] = ((draws[0] - draws[1]) * np.sqrt(10 / 9)) @ weights
        analytic_var = (errors["en"].var(axis=1, ddof=1) + errors[lang].var(axis=1, ddof=1)) / 10
        analytic_se = np.sqrt(analytic_var @ (weights**2))
        # Independent analytic variance validates the resampling implementation.
        assert np.allclose(deviations.std(axis=0, ddof=1), analytic_se, rtol=0.06)
        item = {
            "language": lang,
            "capital_ids": group,
            "home_pairs": int(home.sum()),
            "other_pairs": int((~home).sum()),
            "home_english_MAE_km": float(mean_errors["en"][home].mean()),
            "home_language_MAE_km": float(mean_errors[lang][home].mean()),
            "other_english_MAE_km": float(mean_errors["en"][~home].mean()),
            "other_language_MAE_km": float(mean_errors[lang][~home].mean()),
            "home": interval_and_p(observed[0], deviations[:, 0]),
            "other": {"gain_km": float(observed[1])},
            "interaction": interval_and_p(observed[2], deviations[:, 2]),
            "analytic_se_km": analytic_se.tolist(),
            "bootstrap_se_km": deviations.std(axis=0, ddof=1).tolist(),
            "median_estimate_home_gain_km": float(
                (
                    np.abs(np.median(values["en"], axis=1) - truth)
                    - np.abs(np.median(values[lang], axis=1) - truth)
                )[home].mean()
            ),
            "leave_one_home_capital_out": {},
        }
        for city in group:
            keep = ~(endpoints == city).any(axis=1)
            remain_home = home[keep]
            co = gain[keep] @ contrast_weights(remain_home)
            item["leave_one_home_capital_out"][city] = {
                "home_gain_km": float(co[0]),
                "interaction_km": float(co[2]),
            }
        report["results"].append(item)
        print(json.dumps(item), flush=True)
    adjusted = holm([item[k]["p"] for item in report["results"] for k in ["home", "interaction"]])
    for i, item in enumerate(report["results"]):
        item["home"]["p_holm_8"] = float(adjusted[2 * i])
        item["interaction"]["p_holm_8"] = float(adjusted[2 * i + 1])
    report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path("paper/results/local-language-audit.json").write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
