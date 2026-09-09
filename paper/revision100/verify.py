"""Verify the revised manuscript's source contracts and reported numerical claims."""
import json

import numpy as np

from atlas.inference import holm
from paper.revision100.build import verify_release
from paper.revision100.common import DISTANCE_AUDIT, MAP_AUDIT, PAPER, ROOT, load_results, sha


def main():
    verify_release()
    runs=load_results()
    assert list(runs)==['en','ar','zh']
    assert sum(r['quality']['valid'] for r in runs.values())==148491
    assert sum(r['quality']['attempts'] for r in runs.values())==148504
    assert all(r['experiment']['sampling_count']==10 and r['experiment']['model']=='gemini-3.5-flash' for r in runs.values())
    audit=json.loads(DISTANCE_AUDIT.read_text());maps=json.loads(MAP_AUDIT.read_text())
    assert audit['complete_pairs']==4948 and audit['excluded_pair_ids']==['AR--VN','BE--FR']
    assert np.allclose([audit['all_pairs_median_MAE_km'][l] for l in runs],[215.86483240339416,233.97775707040924,222.02246817386398])
    assert np.allclose(holm([c[k] for c in audit['comparisons'] for k in ['judgment_p','accuracy_p']]),[c[k] for c in audit['comparisons'] for k in ['judgment_p_holm','accuracy_p_holm']])
    for c in maps['comparisons']:
        null=np.array(c['null_statistics_km']);assert len(null)==999
        assert (1+sum(null>=c['observed_mean_capital_shift_km']-1e-10))/1000==c['map_p']
        assert c['all_fits_converged']
    local=json.loads((PAPER/'revision100/local.json').read_text());geo=json.loads((PAPER/'revision100/geometry.json').read_text())
    assert local['script_sha256']==sha(PAPER/'revision100/local.py')
    assert np.allclose(holm([r[k]['p'] for r in local['results'] for k in ['home','interaction']]),[r[k]['p_holm_4'] for r in local['results'] for k in ['home','interaction']])
    for r in local['results']:
        assert np.isclose(r['home_english_MAE_km']-r['home_language_MAE_km'],r['home']['gain_km'])
        assert r['one_endpoint']+r['both_endpoints']==r['home_pairs']
        assert r['distance_balance']['covered_pair_fraction']==1
    assert geo['source_script_sha256']==sha(PAPER/'revision100/geometry.py')
    assert all(c['fit']['all_starts_converged'] for c in geo['conditions'].values())
    assert all(c['input_triangle_checks']['triples']==161700 for c in geo['conditions'].values())
    assert geo['conditions']['truth']['input_triangle_checks']['violated_triples']==0
    for l in runs:assert geo['conditions'][l]['archived_four_start_verification']['pass']
    # All exact prompts and all 100 capital rows must be present in generated artifacts.
    prompts=json.loads((PAPER/'results/exact-language-prompts.json').read_text())
    assert prompts=={l:r['experiment']['prompt_template'] for l,r in runs.items()}
    assert len((PAPER/'generated/capitals-table.tex').read_text().splitlines())==100
    assert len(json.loads((PAPER/'experiment-index.json').read_text()))==3
    for report in [audit,maps]:
        for source in report['sources'].values():assert sha(ROOT/source['path'])==source['sha256']
    print('Verified 100-capital scope, frozen sources, counts, statistics, fits, prompts, and generated tables')


if __name__=='__main__':main()
