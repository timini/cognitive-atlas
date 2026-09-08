"""Scientific audit invariants; no paid API calls and no expensive resampling."""

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("local_language", ROOT / "paper/scripts/local_language.py")
LOCAL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LOCAL)


def test_local_contrast_removes_uniform_language_advantage():
    weights = LOCAL.contrast_weights([True, False, True, False, False])
    assert np.allclose(np.ones(5) * 20 @ weights, [20, 20, 0])
    assert np.allclose(np.array([30, 10, 30, 10, 10]) @ weights, [30, 10, 20])
    assert np.allclose(weights.sum(axis=0), [1, 1, 0])
    with pytest.raises(ValueError):
        LOCAL.contrast_weights([True, True])


def test_null_and_multiple_test_correction():
    assert LOCAL.interval_and_p(0, np.zeros(100))["p"] == 1
    assert np.allclose(LOCAL.holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])
    p = np.array([0.0001, 0.3, 1, 0.02])
    assert np.all(LOCAL.holm(p) >= p)


def test_paper_results_match_sources_and_analysis_code():
    for name, script in [
        ("language-difference-audit", "check_language_differences"),
        ("local-language-audit", "local_language"),
    ]:
        report = json.loads((ROOT / f"paper/results/{name}.json").read_text())
        assert (
            hashlib.sha256((ROOT / f"paper/scripts/{script}.py").read_bytes()).hexdigest()
            == report["script_sha256"]
        )
        for source in report["sources"].values():
            assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
        assert report["complete_pairs"] == 1223
        assert report["excluded_pair_ids"] == ["AR--VN", "KR--RU"]


def test_local_effects_are_computed_from_individual_errors():
    report = json.loads((ROOT / "paper/results/local-language-audit.json").read_text())
    for result in report["results"]:
        assert result["home_pairs"] + result["other_pairs"] == report["complete_pairs"]
        home = result["home_english_MAE_km"] - result["home_language_MAE_km"]
        other = result["other_english_MAE_km"] - result["other_language_MAE_km"]
        assert np.isclose(home, result["home"]["gain_km"])
        assert np.isclose(home - other, result["interaction"]["gain_km"])
        assert np.allclose(result["analytic_se_km"], result["bootstrap_se_km"], rtol=0.06)
        for key in ["home", "interaction"]:
            assert result[key]["p_holm_8"] >= result[key]["p"]


def test_manuscript_totals_and_spanish_percentage():
    checks = json.loads((ROOT / "paper/results/manuscript-checks.json").read_text())
    assert checks["total_language_valid"] == 61237
    assert checks["total_language_attempts"] == 61251
    assert np.isclose(checks["spanish_home_gain_percent"], 6.9717407)
