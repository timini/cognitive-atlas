import numpy as np
import pytest

from atlas.map_inference import make_groups, map_displacement, permuted_medians
from atlas.reconstruct import to_latlon, unit_vectors


def test_alignment_statistic_is_rotation_invariant():
    x = [[10, 20], [-30, 50], [40, -100], [-50, -70]]
    rotation = np.array([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
    assert map_displacement(x, to_latlon(unit_vectors(x)@rotation)) < .001
    assert map_displacement(x, [[10, 20], [-30, 50], [60, -100], [-50, -70]]) > 100


def test_ragged_valid_counts_are_not_imputed():
    a, b = [[100]*10, [200]*4, [300]*10], [[100]*10, [200]*9, [300]*7]
    groups = make_groups(a, b)
    x, y = permuted_medians(groups, 3, seed=10)
    assert np.array_equal(x, [100, 200, 300])
    assert np.array_equal(y, [100, 200, 300])
    assert sum(len(row[0]) for row in groups) == 3
    with pytest.raises(ValueError, match='at least one'):
        make_groups([[1], []], [[2], [3]])


def test_published_map_audits_preserve_null_statistics_and_provenance():
    import hashlib
    import json
    from pathlib import Path

    from atlas.inference import holm
    code = hashlib.sha256(Path('atlas/map_inference.py').read_bytes()).hexdigest()
    for path in Path('public/data/map-audits').glob('*.json'):
        report = json.loads(path.read_text())
        assert report['code_sha256'] == code
        assert report['total_pairs'] == report['capital_count']*(report['capital_count']-1)//2
        pvalues = []
        for c in report['comparisons']:
            null = np.array(c['null_statistics_km'])
            assert len(null) == report['permutations']
            assert c['all_fits_converged']
            p = (1+np.count_nonzero(null >= c['observed_mean_capital_shift_km']-1e-10))/(len(null)+1)
            assert p == c['map_p']
            pvalues.append(p)
        assert np.array_equal(holm(pvalues), [c['map_p_holm'] for c in report['comparisons']])
        for s in report['sources'].values():
            assert hashlib.sha256(Path(s['path']).read_bytes()).hexdigest() == s['sha256']
