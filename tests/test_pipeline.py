import json

import httpx
import numpy as np
import pytest
from scipy.spatial.distance import pdist, squareform

from atlas.data import generate_pairs, geodesic, load_places, write_csv
from atlas.deformation import mesh, warp_points
from atlas.experiment import create_experiment
from atlas.parsing import parse_distance
from atlas.providers import Gemini, Reply
from atlas.reconstruct import align_planar, classical, planar, spherical, spherical_distances, unit_vectors
from atlas.runner import history, run
from atlas.statistics import aggregate, triangle_metrics


@pytest.mark.parametrize("raw,value,quality", [("1,234", 1234, "valid"), ("1234 km", 1234, "valid"),
    ("1.2e3", 1200, "valid"), ("0", None, "non_positive_or_non_finite"),
    ("-4", None, "non_positive_or_non_finite"), ("20041", None, "beyond_earth_diameter_arc"),
    ("100 miles", None, "wrong_units"), ("100 to 200", None, "multiple_numbers"),
    ("about 100", None, "non_numeric"), ("NaN", None, "non_numeric"), ("12,34", None, "multiple_numbers")])
def test_parser(raw, value, quality):
    result = parse_distance(raw)
    assert result.value == value and result.quality == quality


def test_geodesic_and_pairs():
    a = {"id": "a", "latitude": 0, "longitude": 0}
    b = {"id": "b", "latitude": 0, "longitude": 1}
    assert geodesic(a, b) == pytest.approx(111.319490793, abs=1e-6)
    assert generate_pairs([b, a])[0]["id"] == "a--b"
    assert len(generate_pairs(load_places("data/capitals-v1.csv"))) == 190


def test_aggregation():
    s = aggregate([100] * 9 + [1000])
    assert s["median"] == s["trimmed_mean"] == 100
    assert s["mean"] == 190 and s["variance"] == pytest.approx(81000)
    assert s["robust"] < 101 and s["outliers"] == 1
    assert aggregate([100])["std"] is None


def test_triangle_and_mds():
    x = np.array([[0, 0], [3, 0], [0, 4], [3, 4.]])
    d = squareform(pdist(x))
    assert triangle_metrics(d)["triangle_violation_rate"] == 0
    assert np.allclose(squareform(pdist(classical(d))), d)
    fit, _ = planar(d)
    assert np.max(abs(squareform(pdist(fit)) - d)) < 0.01
    ordinal, detail = planar(d, metric=False)
    assert np.isfinite(ordinal).all() and detail["stress"] < 0.05
    bad = np.array([[0., 1, 3], [1, 0, 1], [3, 1, 0]])
    assert triangle_metrics(bad)["triangle_violation_rate"] == 1


def test_alignment():
    x = np.array([[0., 0], [2, 1], [0, 2], [-3, 0]])
    y = 3 * x @ np.array([[0, 1], [1, 0]]) + [5, 10]
    aligned, _ = align_planar(x, y)
    assert np.allclose(aligned, y)


def test_spherical():
    ll = np.array([[0., 0], [10, 45], [40, -60], [-40, 120], [50, 140], [-10, -80]])
    d = spherical_distances(unit_vectors(ll))
    inferred, detail = spherical(d, ll, starts=2)
    assert detail["stress"] < 1e-6
    assert np.allclose(spherical_distances(unit_vectors(inferred)), d, atol=.001)
    assert detail["mean_displacement_km"] < .01


def test_deformation_exact_controls_and_identity():
    source = [[0, 0], [20, 30], [-30, -40], [60, -20]]
    m = mesh(source, source)
    points = np.array([[10., 10], [-30, -60], [130, 45]])
    assert np.allclose(warp_points(points, m), points)
    target = [[1, 2], [21, 32], [-29, -38], [61, -18]]
    m = mesh(source, target)
    assert np.allclose(warp_points(m["source"][:4], m), m["target"][:4])


class FakeProvider:
    """Unit-test fixture only; never written into published research data."""
    def __init__(self):
        self.calls = 0

    async def query(self, *args):
        self.calls += 1
        return Reply("100", {"test_fixture": True}, 20, 2, "test", 1., "STOP")


async def test_csv_resume_and_no_cross_sample_cache(tmp_path):
    places = load_places("data/capitals-v1.csv")[:3]
    write_csv(tmp_path / "places.csv", places)
    run_dir = create_experiment(tmp_path / "places.csv", root=tmp_path / "runs", samples=2, rpm=1e8)
    p = FakeProvider()
    await run(run_dir, p, max_jobs=2)
    assert p.calls == 2
    await run(run_dir, p)
    assert p.calls == 6
    before = (run_dir / "responses.csv").read_bytes()
    await run(run_dir, p)
    assert p.calls == 6 and (run_dir / "responses.csv").read_bytes() == before
    assert len(history(run_dir)) == 6


async def test_budget_blocks_calls(tmp_path):
    write_csv(tmp_path / "places.csv", load_places("data/capitals-v1.csv")[:3])
    directory = create_experiment(tmp_path / "places.csv", root=tmp_path / "runs", max_cost=1e-12)
    provider = FakeProvider()
    await run(directory, provider)
    assert provider.calls == 0


async def test_google_wire_protocol():
    def handler(request):
        body = json.loads(request.content)
        assert request.headers["x-goog-api-key"] == "unit-test"
        assert "key=" not in str(request.url)
        assert "tools" not in body and len(body["contents"]) == 1
        return httpx.Response(200, json={"modelVersion": "version", "candidates": [
            {"content": {"parts": [{"text": "345"}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 22, "candidatesTokenCount": 2}})
    p = Gemini("unit-test", transport=httpx.MockTransport(handler))
    result = await p.query("gemini-2.5-flash-lite", "Distance?", {"temperature": 1, "top_p": .95,
                           "max_tokens": 32, "thinking_budget": 0})
    await p.close()
    assert result.text == "345" and result.model_version == "version"
