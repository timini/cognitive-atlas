"""Build the revised manuscript assets from verified, fixed 100-capital inputs."""
import json

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform

from atlas.reconstruct import stress
from paper.revision100.common import (
    DISTANCE_AUDIT,
    EXPORTS,
    LABELS,
    MAP_AUDIT,
    PAPER,
    ROOT,
    load_results,
    sha,
)

COLORS={'en':'#263c54','ar':'#aa4d57','zh':'#436f91'}
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'savefig.bbox':'tight'})


def esc(value):
    return str(value).replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')


def rows(name, data):
    (PAPER/'generated'/name).write_text('\n'.join(' & '.join(map(str,row))+r' \\' for row in data)+'\n')


def verify_release():
    lock=json.loads((PAPER/'release-lock.json').read_text())
    for path,expected in lock['files'].items():
        if sha(ROOT/path)!=expected:raise ValueError(f'Release input changed: {path}; create an explicit new release lock')


def main():
    verify_release()
    runs=load_results()
    audit=json.loads(DISTANCE_AUDIT.read_text()); maps=json.loads(MAP_AUDIT.read_text())
    local=json.loads((PAPER/'revision100/local.json').read_text()); geo=json.loads((PAPER/'revision100/geometry.json').read_text())
    qc=json.loads((PAPER/'revision100/qc.json').read_text())
    for name in ['generated','figures','results']:(PAPER/name).mkdir(exist_ok=True)
    # The lock is checked before any outputs are written; expected hashes are never refreshed here.
    (PAPER/'results/exact-language-prompts.json').write_text(json.dumps({l:r['experiment']['prompt_template'] for l,r in runs.items()},indent=2,ensure_ascii=False)+'\n')
    for name,report in [('language-difference-audit',audit),('map-difference-audit',maps)]:
        (PAPER/'results'/f'{name}.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    rows('language-table.tex',[[LABELS[l],f"{r['quality']['valid']:,}",f"{r['layers']['median']['metrics']['mae_km']:.1f}",f"{r['layers']['median']['metrics']['rmse_km']:.1f}",f"{r['layers']['median']['metrics']['spearman']:.5f}",f"{100*r['layers']['median']['metrics']['triangle_violation_rate']:.2f}"] for l,r in runs.items()])
    grows=[]
    for l,g in geo['conditions'].items():
        fit=g['fit']; tri=g['input_triangle_checks']; disp=fit['best_aligned_true_displacement']
        grows.append(['WGS84 control' if l=='truth' else LABELS[l],f"{fit['best_all_stress']:.5f}",f"{disp['mean_km']:.1f}",f"{100*g['input_nearest_three_preservation']['mean_fraction']:.1f}",f"{100*g['fitted_nearest_three_preservation']['mean_fraction']:.1f}",f"{tri['mean_excess_violated_triples_km']:.1f}" if tri['mean_excess_violated_triples_km'] is not None else "---"])
    rows('geometry-table.tex',grows)
    rows('pairwise-table.tex',[[LABELS[c['a']]+' / '+LABELS[c['b']],f"{c['mean_absolute_median_disagreement_km']:.1f}",f"{c['mae_difference_b_minus_a_km']:+.1f}",f"{c['judgment_p_holm']:.4f}",f"{c['accuracy_p_holm']:.4f}"] for c in audit['comparisons']])
    rows('map-table.tex',[[LABELS[c['a']]+' / '+LABELS[c['b']],f"{c['observed_mean_capital_shift_km']:.1f}",f"{c['null_mean_capital_shift_km']:.1f}",f"{c['null_shift_95pct_interval_km'][0]:.1f}--{c['null_shift_95pct_interval_km'][1]:.1f}",f"{c['map_p_holm']:.3f}"] for c in maps['comparisons']])
    rows('local-table.tex',[[LABELS[c['language']],str(c['home_pairs']),f"{c['home_english_MAE_km']:.1f}",f"{c['home_language_MAE_km']:.1f}",f"{c['home']['gain_km']:+.1f}",f"{c['home']['p_holm_4']:.4f}",f"{c['interaction']['gain_km']:+.1f}",f"{c['interaction']['p_holm_4']:.4f}"] for c in local['results']])
    rows('balance-table.tex',[[LABELS[c['language']],str(c['one_endpoint']),str(c['both_endpoints']),f"{c['home_truth_median_km']:.0f}",f"{c['other_truth_median_km']:.0f}",f"{c['distance_balance']['standardized_home_gain_km']:+.1f}",f"{c['distance_balance']['standardized_interaction_km']:+.1f}"] for c in local['results']])
    rows('sensitivity-table.tex',[[LABELS[l],*[f"{qc['conditions'][l]['accuracy'][key]['pair_median_mae_km']:.2f}" for key in ['all_pairs_accepted','common_complete_case_accepted','all_pairs_numeric_range_retained']]] for l in runs])
    rows('dispersion-table.tex',[[LABELS[l],f"{qc['conditions'][l]['dispersion']['sample_sd_km']['mean']:.1f}",f"{100*qc['conditions'][l]['dispersion']['coefficient_of_variation']['mean']:.2f}",str(qc['conditions'][l]['dispersion']['ten_valid_pairs_all_ten_identical'])] for l in runs])
    rows('capitals-table.tex',[[esc(p['id']),esc(p['capital_name']),esc(p['country_name'])] for p in runs['en']['places']])
    rows('experiments-table.tex',[[LABELS[l],r'\texttt{'+r['experiment']['id']+'}',r'\texttt{'+r['analysis_id']+'}'] for l,r in runs.items()])
    # Separate distances and disparities: common target-normalized stress only for metric methods.
    arows=[]
    for l,r in runs.items():
        order=[p['id'] for p in r['places']]; lookup={p:i for i,p in enumerate(order)};d=np.zeros((100,100))
        for p in r['pairs']:
            i,j=lookup[p['place_a_id']],lookup[p['place_b_id']];d[i,j]=d[j,i]=p['median']
        rec=r['layers']['median']['reconstructions']
        arows.append([LABELS[l],f"{stress(squareform(pdist(np.array(rec['classical']['raw_coordinates']))),d):.4f}",f"{stress(squareform(pdist(np.array(rec['metric']['raw_coordinates']))),d):.4f}",f"{rec['spherical']['stress']:.4f}",f"{rec['nonmetric']['stress']:.4f}"])
    rows('algorithms-table.tex',arows)
    provenance={'release':'100-capital-2026-09-09','input_lock_sha256':sha(PAPER/'input-lock.json'),'release_lock_sha256':sha(PAPER/'release-lock.json'),'source_exports':EXPORTS,'valid':sum(r['quality']['valid'] for r in runs.values()),'attempts':sum(r['quality']['attempts'] for r in runs.values()),'complete_pairs':audit['complete_pairs'],'estimated_cost_usd':sum(r['quality']['estimated_cost_usd'] for r in runs.values())}
    (PAPER/'results/provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    # Three full maps; capital positions and coastlines both shown at actual displacement.
    fig,axes=plt.subplots(3,1,figsize=(7.05,8.0),layout='constrained')
    for ax,(l,r) in zip(axes,runs.items()):
        for country in r['layers']['median']['countries']:
            for ring in country['rings']:
                src=np.array(ring['source']);dst=np.array(ring['target'])
                ax.plot(src[:,0],-src[:,1],color='#c9cdd2',lw=.35)
                ax.plot(dst[:,0],-dst[:,1],color=COLORS[l],lw=.4,alpha=.75)
        actual=np.array([[p['latitude'],p['longitude']] for p in r['places']]); inferred=np.array(r['layers']['median']['reconstructions']['spherical']['inferred_latlon'])
        ax.scatter(actual[:,1],actual[:,0],s=5,color='#353535',zorder=4,label='Reference capital')
        ax.scatter(inferred[:,1],inferred[:,0],s=12,facecolors='none',edgecolors=COLORS[l],lw=.7,zorder=5,label='Fitted capital')
        ax.set(xlim=(-180,180),ylim=(-62,85),ylabel='Latitude',title=LABELS[l]+' instructions')
        ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.13)
    axes[-1].set_xlabel('Longitude (degrees; equirectangular display)')
    handles,labels=axes[0].get_legend_handles_labels();fig.legend(handles,labels,loc='outside lower center',ncol=2,frameon=False,fontsize=8)
    fig.savefig(PAPER/'figures/reconstructed-worlds.pdf');plt.close(fig)
    fig,axes=plt.subplots(1,3,figsize=(7.05,2.65),layout='constrained')
    for ax,(l,r) in zip(axes,runs.items()):
        t=[p['true_distance_km']/1000 for p in r['pairs']];x=[p['median']/1000 for p in r['pairs']]
        ax.scatter(t,x,s=1.2,alpha=.18,color=COLORS[l],rasterized=True)
        ax.plot([0,20],[0,20],color='black',lw=.7,ls='--');ax.set(xlim=(0,20.5),ylim=(0,20.5),title=LABELS[l],xlabel='WGS84 distance (1000 km)');ax.set_aspect('equal')
    axes[0].set_ylabel('Pair median (1000 km)');fig.savefig(PAPER/'figures/distance-accuracy.pdf');plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(7.05,3.05),layout='constrained')
    for l,r in runs.items():
        dims=r['layers']['median']['dimensionality']; axes[0].plot([d['dimensions'] for d in dims],[d['stress'] for d in dims],color=COLORS[l],label=LABELS[l])
    truth=runs['en']['true_earth_dimensionality'];axes[0].plot([d['dimensions'] for d in truth],[d['stress'] for d in truth],color='black',ls='--',label='WGS84 reference')
    axes[0].set(xlabel='Euclidean dimensions',ylabel='Target-normalized stress',xticks=[1,2,3,5,10],title='Euclidean fit and reference');axes[0].legend(frameon=False,fontsize=7)
    for i,c in enumerate(maps['comparisons']):
        ax=axes[1]; ax.barh(i,c['observed_mean_capital_shift_km'],color=COLORS[c['b']],alpha=.75)
        lo,hi=c['null_shift_95pct_interval_km'];mu=c['null_mean_capital_shift_km'];ax.errorbar(mu,i,xerr=[[mu-lo],[hi-mu]],fmt='|',color='black',capsize=3)
    axes[1].set(yticks=range(3),yticklabels=['EN / AR','EN / ZH','AR / ZH'],xlabel='Mean aligned capital shift (km)',title='Observed fits and shuffled baseline');axes[1].invert_yaxis()
    fig.savefig(PAPER/'figures/structure-and-language.pdf');plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(7.05,2.65),layout='constrained')
    for ax,key,title in zip(axes,['home','interaction'],['Gain on associated pairs','Gain relative to other pairs']):
        for i,c in enumerate(local['results']):
            value=c[key]['gain_km'];lo,hi=c[key]['ci95_km'];ax.errorbar(value,i,xerr=[[value-lo],[hi-value]],fmt='o',color=COLORS[c['language']],capsize=3)
        ax.axvline(0,color='gray',ls='--',lw=.7);ax.set(yticks=range(2),yticklabels=['Arab States','Beijing / Singapore'],xlabel='Gain (km; positive = lower error)',title=title,ylim=(-.6,1.6));ax.invert_yaxis()
    fig.savefig(PAPER/'figures/local-language-effects.pdf');plt.close(fig)
    print(json.dumps(provenance))


if __name__=='__main__':main()
