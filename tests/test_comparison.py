import copy
import json
from pathlib import Path

import numpy as np
import pytest

from atlas.comparison import compare_results
from atlas.reconstruct import RADIUS_KM, angular_jacobian, spherical_distances, unit_vectors


def pilot():
    entry = json.loads(Path("public/data/experiments.json").read_text())[0]
    return json.loads((Path("public") / entry["url"].lstrip("/")).read_text())


def test_self_comparison_has_identity_geometry():
    a = pilot()
    result = compare_results(a, a)
    assert result["spearman"] == pytest.approx(1)
    assert result["mean_absolute_distance_disagreement_km"] == 0
    assert result["mean_aligned_map_displacement_km"] < .001


def test_comparison_rejects_different_entities():
    a = pilot()
    b = copy.deepcopy(a)
    b["places"] = b["places"][:-1]
    with pytest.raises(ValueError, match="same ordered"):
        compare_results(a, b)


def test_analytic_jacobian_matches_independent_finite_difference():
    angles = np.radians([[10, 15], [-20, 65], [30, -70], [-45, -100]]).ravel()
    idx = np.triu_indices(4, 1)
    def residual(a):
        return spherical_distances(unit_vectors(np.degrees(a.reshape(-1, 2))))[idx] / RADIUS_KM
    numeric = []
    for k in range(len(angles)):
        step = np.zeros_like(angles)
        step[k] = 1e-6
        numeric.append((residual(angles + step) - residual(angles - step)) / 2e-6)
    assert np.allclose(angular_jacobian(angles).toarray(), np.array(numeric).T, atol=1e-8)
