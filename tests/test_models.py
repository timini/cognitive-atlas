import json

import httpx
import pytest

from atlas.data import load_places, write_csv
from atlas.experiment import create_experiment
from atlas.providers import Gemini, Reply
from atlas.runner import history, run


def test_expanded_dataset_is_superset_with_reviewed_capitals():
    old = {p["id"]: p for p in load_places("data/capitals-v1.csv")}
    new = {p["id"]: p for p in load_places("data/capitals-50-v2.csv")}
    assert len(new) == 50
    assert all(new[k] == p for k, p in old.items())
    assert new["TZ"]["capital_name"] == "Dodoma"
    assert new["NL"]["capital_name"] == "Amsterdam"
    assert new["SG"]["country_name"] == "Singapore"


@pytest.mark.parametrize("model", ["gemini-3-flash-preview", "gemini-3.5-flash"])
async def test_gemini_3_thinking_protocol_and_usage(model, tmp_path):
    def handler(request):
        body = json.loads(request.content)
        assert body["generationConfig"]["thinkingConfig"] == {"thinkingLevel": "minimal"}
        assert body["generationConfig"]["maxOutputTokens"] == 128
        return httpx.Response(200, json={"candidates": [{"content": {"parts": [
            {"text": "not an observation", "thought": True}, {"text": "1200"}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 50, "candidatesTokenCount": 4, "thoughtsTokenCount": 12}})
    p = Gemini("test", transport=httpx.MockTransport(handler))
    r = await p.query(model, "test prompt", {"temperature": 1, "top_p": .95, "max_tokens": 128, "thinking_level": "minimal"})
    await p.close()
    assert r.text == "1200" and r.output_tokens == 16


async def test_successful_reservations_reconcile_and_resume(tmp_path):
    write_csv(tmp_path / "places.csv", load_places("data/capitals-v1.csv")[:3])
    directory = create_experiment(tmp_path / "places.csv", root=tmp_path / "runs", samples=2,
                                  model="gemini-3.5-flash", max_cost=.0025, concurrency=1, rpm=1e9)
    class Provider:
        calls = 0
        async def query(self, *args):
            self.calls += 1
            return Reply("100", {"fixture": True}, 20, 2, "test", 1, "STOP")
    provider = Provider()
    await run(directory, provider, max_jobs=2)
    rows = history(directory)
    assert all(float(r["reserved_cost_usd"]) == float(r["estimated_cost_usd"]) for r in rows)
    await run(directory, provider)
    assert provider.calls == 6
