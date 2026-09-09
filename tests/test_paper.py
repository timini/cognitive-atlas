"""Scientific contracts for the current 100-capital manuscript; no paid calls."""
import json
from pathlib import Path

import numpy as np
import pytest

from paper.revision100 import common
from paper.revision100.build import verify_release
from paper.revision100.error_control import sign_control, triangle_summary
from paper.revision100.local import bootstrap_deviations, contrast_weights, distance_balance, summary
from paper.revision100.verify import main as verify_paper


def test_current_paper_and_publication_have_only_the_three_100_capital_conditions():
    verify_paper()
    entries=json.loads(Path('public/data/experiments.json').read_text())
    assert len(entries)==3 and {e['language'] for e in entries}=={'en','ar','zh'}
    assert all(e['capital_count']==100 for e in entries)
    assert entries==json.loads(Path('paper/experiment-index.json').read_text())


def test_frozen_inputs_reject_changed_content(tmp_path,monkeypatch):
    path=tmp_path/'input.txt';path.write_text('original')
    (tmp_path/'input-lock.json').write_text(json.dumps({'files':{'input.txt':common.sha(path)}}))
    monkeypatch.setattr(common,'ROOT',tmp_path);monkeypatch.setattr(common,'PAPER',tmp_path)
    common.verify_inputs()
    path.write_text('changed')
    with pytest.raises(ValueError,match='Frozen manuscript input changed'):common.verify_inputs()


def test_release_build_contract_is_complete():
    verify_release()
    lock=json.loads(Path('paper/release-lock.json').read_text())['files']
    assert all(str(p) in lock for p in Path('paper/revision100').glob('*.py'))
    assert all(str(p) in lock for p in Path('paper/revision100').glob('*.json'))
    inputs=json.loads(Path('paper/input-lock.json').read_text())['files']
    assert 'public/data/world.json' in inputs and 'uv.lock' in inputs
    assert sum(p.endswith('/responses.csv') for p in inputs)==3


def test_region_interaction_and_distance_standardization():
    home=np.array([True,False,True,False,False])
    weights=contrast_weights(home)
    assert np.allclose(np.ones(5)*20@weights,[20,20,0])
    assert np.allclose(np.array([30,10,30,10,10])@weights,[30,10,20])
    with pytest.raises(ValueError):contrast_weights([True,True])
    truth=np.arange(1,101);selected=np.arange(100)%2==0
    balanced=distance_balance(np.ones(100)*5,truth,selected)
    assert balanced['covered_pair_fraction']==1
    assert balanced['standardized_home_gain_km']==5
    assert balanced['standardized_interaction_km']==0


def test_bootstrap_identity_null_and_variance_not_coverage():
    a=np.ones((40,10))*100;w=contrast_weights(np.arange(40)<10)
    deviations=bootstrap_deviations(a,a,w,99,1)
    assert np.array_equal(deviations,np.zeros((99,3)))
    assert summary(0,deviations[:,0])['p']==1
    rng=np.random.default_rng(22);a=rng.normal(100,10,(40,10));b=rng.normal(100,20,(40,10))
    d=bootstrap_deviations(a,b,w,1999,2)
    se=np.sqrt(((a.var(axis=1,ddof=1)+b.var(axis=1,ddof=1))/10)@(w*w))
    assert np.allclose(d.std(axis=0,ddof=1),se,rtol=.06)


def test_manuscript_is_not_about_superseded_studies():
    text=Path('paper/main.tex').read_text()
    assert '50-capital' not in text and '20-capital' not in text
    assert 'Spanish' not in text and 'French' not in text
    assert '148,500' in text and '4,948' in text
    assert 'not provider-enforced output schemas' in text
    assert 'population median maps' in text
    assert 'coverage collapsed' in text


def test_error_sign_controls_preserve_pairwise_accuracy_and_admissible_domain():
    truth = np.array([1., 19000., 100., 200.])
    observed = np.array([3., 17000., 90., 200.])
    rng = np.random.default_rng(42)
    signs = []
    for _ in range(50):
        artificial, forced = sign_control(truth, observed, rng)
        assert forced == 2
        assert np.array_equal(np.abs(artificial - truth), np.abs(observed - truth))
        assert np.all((artificial > 0) & (artificial <= 20040))
        assert artificial[0] == 3 and artificial[1] == 17000 and artificial[3] == 200
        signs.append(artificial[2])
    assert set(signs) == {90, 110}
    for invalid in ([0., 1.], [-1., 1.], [1., np.nan], [1., 20041.]):
        with pytest.raises(ValueError):
            sign_control(np.array([100., 200.]), np.array(invalid), rng)
    edges = np.array([[0, 1, 2]])
    assert triangle_summary(np.array([3., 4., 5.]), edges)['violation_rate'] == 0
    result = triangle_summary(np.array([3., 4., 8.]), edges)
    assert result['violation_rate'] == 1 and result['mean_excess_all_triples_km'] == 1
