import json

import numpy as np
import pytest

from atlas.analysis import analyze
from atlas.data import load_places, write_csv
from atlas.experiment import create_experiment
from atlas.providers import ProviderError, Reply
from atlas.runner import history, run
from atlas.validation import validate_inputs


def experiment(tmp_path):
    write_csv(tmp_path / "places.csv", load_places("data/capitals-v1.csv")[:3])
    return create_experiment(tmp_path / "places.csv", root=tmp_path / "runs", samples=1, rpm=1e9)


def test_manifest_and_pair_tamper_detection(tmp_path):
    directory = experiment(tmp_path)
    validate_inputs(directory)
    path = directory / "pairs.csv"
    original = path.read_text()
    path.write_text(original.replace("AR--AU", "ZZ--AU"))
    with pytest.raises(ValueError, match="Pair file"):
        validate_inputs(directory)
    path.write_text(original)
    path = directory / "manifest.json"
    m = json.loads(path.read_text())
    m["parameters"]["temperature"] = .2
    path.write_text(json.dumps(m))
    with pytest.raises(ValueError, match="manifest"):
        validate_inputs(directory)


async def test_retry_is_preserved(tmp_path, monkeypatch):
    directory = experiment(tmp_path)
    import atlas.runner
    async def no_delay(_):
        pass
    monkeypatch.setattr(atlas.runner.asyncio, "sleep", no_delay)
    class RetryProvider:
        calls = 0
        async def query(self, *args):
            self.calls += 1
            if self.calls == 1:
                raise ProviderError("http_429", True)
            return Reply("100", {}, 20, 2, "test", 1, "STOP")
    p = RetryProvider()
    result = await run(directory, p)
    assert result["valid_samples"] == 3 and result["attempts"] == 4
    rows = history(directory)
    assert rows[0]["quality"] == "http_429" and rows[0]["terminal"] == "False"


async def test_invalid_content_not_retried_or_filled(tmp_path):
    directory = experiment(tmp_path)
    class InvalidProvider:
        async def query(self, *args):
            return Reply("100 or 200", {}, 20, 2, "test", 1, "STOP")
    await run(directory, InvalidProvider())
    assert len(history(directory)) == 3
    with pytest.raises(ValueError, match="Missing valid distances"):
        analyze(directory)


def test_incomplete_run_not_analyzed(tmp_path):
    with pytest.raises(ValueError, match="incomplete"):
        analyze(experiment(tmp_path))


def test_published_measurements_are_derived_from_raw_csv():
    """Independent audit of the real published pilot. No provider mocks here."""
    from collections import defaultdict
    from pathlib import Path

    from atlas.data import read_csv
    from atlas.experiment import prompt_for
    from atlas.parsing import parse_distance
    index = Path("public/data/experiments.json")
    if not index.exists():
        pytest.skip("No real export yet")
    for entry in json.loads(index.read_text()):
        directory = Path("public") / entry["url"].lstrip("/")
        result = json.loads(directory.read_text())
        raw = read_csv(directory.parent / "responses.csv")
        assert all("test_fixture" not in r["provider_payload"] for r in raw)
        assert len(raw) == result["quality"]["attempts"]
        assert len({r["response_id"] for r in raw}) == len(raw)
        by_pair = defaultdict(list)
        places = {p["id"]: p for p in result["places"]}
        prompts = {p["id"]: prompt_for(result["experiment"], p, places) for p in result["pairs"]}
        for row in raw:
            assert row["experiment_id"] == result["experiment"]["id"]
            assert row["prompt"] == prompts[row["pair_id"]]
            if row["provider_payload"] and row["finish_reason"] == "STOP":
                parsed = parse_distance(row["raw_response"], result["experiment"].get("response_parser", "legacy"))
                assert parsed.quality == row["quality"]
                if parsed.value is None:
                    assert row["parsed_distance_km"] == ""
                else:
                    assert parsed.value == float(row["parsed_distance_km"])
            by_pair[row["pair_id"]].append(row)
        assert sum(r["quality"] == "valid" for r in raw) == result["quality"]["valid"]
        for pair in result["pairs"]:
            attempts = by_pair[pair["id"]]
            terminal = [r for r in attempts if r["terminal"] == "True"]
            assert len(terminal) == result["experiment"]["sampling_count"]
            assert len({r["sample_number"] for r in terminal}) == len(terminal)
            values = [float(r["parsed_distance_km"]) for r in attempts if r["quality"] == "valid"]
            assert pair["mean"] == pytest.approx(np.mean(values))
            assert pair["median"] == pytest.approx(np.median(values))
            assert pair["variance"] == pytest.approx(np.var(values, ddof=1))
            assert len(values) + pair["missing_samples"] == result["experiment"]["sampling_count"]
            assert pair["samples"] == values
        for name, layer in result["layers"].items():
            errors = np.array([p[name] - p["true_distance_km"] for p in result["pairs"]])
            assert layer["metrics"]["mae_km"] == pytest.approx(np.abs(errors).mean())
            assert layer["metrics"]["rmse_km"] == pytest.approx(np.sqrt((errors ** 2).mean()))
            assert layer["reconstructions"]["spherical"]["converged"]
