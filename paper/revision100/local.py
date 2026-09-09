"""Exploratory fixed-pair single-response error contrasts for the 100-capital study.

Empirical, variance-adjusted basic bootstrap; independent requests assumed.
No population-of-cities or causal language inference. Regional groups and analyses
are post hoc. Four Holm-adjusted tests concern home gain and interaction for two
specified groups. Distance-balanced and leave-one-capital-out results are descriptive.
"""
import json
from pathlib import Path

import numpy as np

from atlas.inference import holm
from paper.revision100.common import DISTANCE_AUDIT, GROUPS, PAPER, load_results, write_report

SEED, REPLICATES = 20260913, 9999


def contrast_weights(home):
    home = np.asarray(home, dtype=bool)
    if not home.any() or home.all():
        raise ValueError('Both associated and other pairs required')
    wh, wo = home/home.sum(), (~home)/(~home).sum()
    return np.column_stack([wh, wo, wh-wo])


def bootstrap_deviations(a, b, weights, replicates, seed):
    if a.shape != b.shape or a.ndim != 2 or a.shape[1] < 2:
        raise ValueError('Equal pair-by-sample arrays with at least two responses required')
    rng = np.random.default_rng(seed)
    n = a.shape[1]
    out = np.empty((replicates, weights.shape[1]))
    for start in range(0, replicates, 20):
        count = min(20, replicates-start)
        delta = np.zeros((count, len(a)))
        for sign, values in [(1, a),(-1,b)]:
            indices = rng.integers(0,n,size=(count,len(a),n))
            delta += sign*(np.take_along_axis(values[None],indices,axis=-1).mean(axis=-1)-values.mean(axis=1))
        out[start:start+count] = (delta*np.sqrt(n/(n-1))) @ weights
    return out


def summary(value, deviations):
    lower, upper = np.quantile(deviations,[.025,.975])
    exceed = int((np.abs(deviations)>=abs(value)-1e-10).sum())
    return {'gain_km':float(value),'ci95_km':[float(value-upper),float(value-lower)],'p':float((1+exceed)/(1+len(deviations))), 'exceedances':exceed,'replicates':len(deviations)}


def distance_balance(gain, truth, home):
    edges = np.quantile(truth,np.linspace(0,1,6))
    bins = np.minimum(4,np.searchsorted(edges[1:],truth,side='right'))
    rows=[]
    for k in range(5):
        selected=bins==k; h=selected&home; o=selected&~home
        rows.append({'bin':k,'lower_km':float(edges[k]),'upper_km':float(edges[k+1]),'home_pairs':int(h.sum()),'other_pairs':int(o.sum()),'weight':float(selected.mean()),'home_gain_km':float(gain[h].mean()) if h.any() else None,'other_gain_km':float(gain[o].mean()) if o.any() else None})
    common=[r for r in rows if r['home_pairs'] and r['other_pairs']]
    mass=sum(r['weight'] for r in common)
    hg=sum(r['weight']*r['home_gain_km'] for r in common)/mass
    og=sum(r['weight']*r['other_gain_km'] for r in common)/mass
    return {'bins':rows,'covered_pair_fraction':mass,'standardized_home_gain_km':hg,'standardized_other_gain_km':og,'standardized_interaction_km':hg-og,'method':'Pooled truth-distance quintile weights applied to both groups within common-support bins; descriptive, not causal adjustment'}


def main():
    results=load_results()
    audit=json.loads(DISTANCE_AUDIT.read_text())
    pairs={l:{p['id']:p for p in r['pairs']} for l,r in results.items()}
    ids=sorted(set(pairs['en'])-set(audit['excluded_pair_ids']))
    endpoints=np.array([p.split('--') for p in ids])
    truth=np.array([pairs['en'][p]['true_distance_km'] for p in ids])
    values={l:np.array([pairs[l][p]['samples'] for p in ids]) for l in pairs}
    assert all(v.shape==(4948,10) for v in values.values())
    errors={l:np.abs(v-truth[:,None]) for l,v in values.items()}
    report={'method':__doc__,'seed':SEED,'replicates':REPLICATES,'complete_pairs':len(ids),'excluded_pair_ids':audit['excluded_pair_ids'],'groups':GROUPS,'holm_family_size':4,'results':[]}
    for li,(lang,group) in enumerate(GROUPS.items()):
        associated=np.isin(endpoints,group); home=associated.any(axis=1)
        weights=contrast_weights(home)
        gain=errors['en'].mean(axis=1)-errors[lang].mean(axis=1)
        observed=gain@weights
        deviations=bootstrap_deviations(errors['en'],errors[lang],weights,REPLICATES,SEED+li)
        var=(errors['en'].var(axis=1,ddof=1)+errors[lang].var(axis=1,ddof=1))/10
        se=np.sqrt(var@(weights**2))
        assert np.allclose(deviations.std(axis=0,ddof=1),se,rtol=.06)
        item={'language':lang,'capital_ids':group,'home_pairs':int(home.sum()),'other_pairs':int((~home).sum()),'both_endpoints':int(associated.all(axis=1).sum()),'one_endpoint':int((associated.sum(axis=1)==1).sum()),'home_truth_median_km':float(np.median(truth[home])),'other_truth_median_km':float(np.median(truth[~home])),'home_english_MAE_km':float(errors['en'][home].mean()),'home_language_MAE_km':float(errors[lang][home].mean()),'other_english_MAE_km':float(errors['en'][~home].mean()),'other_language_MAE_km':float(errors[lang][~home].mean()),'home':summary(observed[0],deviations[:,0]),'other_gain_km':float(observed[1]),'interaction':summary(observed[2],deviations[:,2]),'analytic_se_km':se.tolist(),'bootstrap_se_km':deviations.std(axis=0,ddof=1).tolist(),'distance_balance':distance_balance(gain,truth,home),'leave_one_capital_out':{}}
        for city in group:
            keep=~(endpoints==city).any(axis=1)
            contrast=gain[keep]@contrast_weights(home[keep])
            item['leave_one_capital_out'][city]={'home_gain_km':float(contrast[0]),'interaction_km':float(contrast[2])}
        # Available-pair and range-retained sensitivities preserve unequal sample counts.
        all_ids=sorted(pairs['en']); all_end=np.array([p.split('--') for p in all_ids]); all_home=np.isin(all_end,group).any(axis=1)
        all_gain=np.array([np.abs(np.array(pairs['en'][p]['samples'])-pairs['en'][p]['true_distance_km']).mean()-np.abs(np.array(pairs[lang][p]['samples'])-pairs[lang][p]['true_distance_km']).mean() for p in all_ids])
        c=all_gain@contrast_weights(all_home)
        item['all_available_pairs']={'home_gain_km':float(c[0]),'interaction_km':float(c[2]),'pairs':len(all_ids)}
        report['results'].append(item)
        print(lang,'home',item['home'],'interaction',item['interaction'],flush=True)
    corrected=holm([r[k]['p'] for r in report['results'] for k in ['home','interaction']])
    for i,r in enumerate(report['results']):
        for j,k in enumerate(['home','interaction']):r[k]['p_holm_4']=float(corrected[2*i+j])
    write_report(PAPER/'revision100/local.json',report,Path(__file__))


if __name__=='__main__':main()
