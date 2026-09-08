import json

import pytest

from atlas.data import generate_pairs, load_places
from scripts.run_languages import prepare


def test_100_preserves_all_original_controls():
    old = {p['id']: p for p in load_places('data/capitals-50-v2.csv')}
    places = load_places('data/capitals-100-v3.csv')
    new = {p['id']: p for p in places}
    assert len(new) == len(places) == 100
    assert {k: new[k] for k in old} == old
    assert len(generate_pairs(places)) == 4950
    assert all(-90 <= p['latitude'] <= 90 and -180 <= p['longitude'] <= 180 for p in places)
    assert new['BO']['capital_name'] == 'Sucre'
    assert new['CI']['capital_name'] == 'Yamoussoukro'
    assert new['CH']['capital_name'] == 'Bern'


def test_matching_group_and_resume_protection(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    from atlas.data import write_csv
    # A tiny real-coordinate fixture; never calls a model.
    write_csv('places.csv', [dict(id='GB', country_name='United Kingdom', capital_name='London', latitude=51.5, longitude=-.12),
                             dict(id='FR', country_name='France', capital_name='Paris', latitude=48.85, longitude=2.35),
                             dict(id='DE', country_name='Germany', capital_name='Berlin', latitude=52.52, longitude=13.40)])
    prepare('group.json', dataset='places.csv', languages=['en', 'ar', 'zh'], samples=2, budget=.2)
    group = json.loads((tmp_path/'group.json').read_text())
    manifests = [json.loads((tmp_path/path/'manifest.json').read_text()) for path in group['paths']]
    assert [m['language'] for m in manifests] == ['en', 'ar', 'zh']
    assert len({m['dataset_sha256'] for m in manifests}) == 1
    assert all(m['sampling_count'] == 2 and m['execution']['max_cost_usd'] == .2 for m in manifests)
    with pytest.raises(ValueError, match='resume'):
        prepare('group.json')
    with pytest.raises(ValueError, match='distinct'):
        prepare('bad.json', languages=['en', 'en'])
    assert not (tmp_path/'bad.json').exists()
