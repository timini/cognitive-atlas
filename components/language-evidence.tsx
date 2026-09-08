'use client';
import {useEffect, useState} from 'react';
import {publicAsset} from '@/lib/public-assets';
import {formatNumber as fmt, type Aggregation} from '@/lib/research';

interface Model {experiment_id:string; export_id:string; language:string; label:string}
export interface MapComparison {
 experiment_a:string; experiment_b:string; aggregation:Aggregation;
 mean_aligned_map_displacement_km:number; max_aligned_map_displacement_km:number;
 capital_displacements?:{place_id:string;capital_name:string;displacement_km:number}[];
}
interface Test {
 a:string; b:string; mean_absolute_median_disagreement_km:number;
 mae_difference_b_minus_a_km:number; judgment_p_holm:number; accuracy_p_holm:number;
}
interface Audit {export_ids:string[]; complete_pairs:number; total_pairs:number; permutations:number; holm_family_size:number; comparisons:Test[]; report_url:string}

export default function LanguageEvidence({models,pairwise,selected,aggregation}:{models:Model[];pairwise:MapComparison[];selected:string;aggregation:Aggregation}) {
 const [audits,setAudits]=useState<Audit[]>([]);
 const [choice,setChoice]=useState('ar');
 useEffect(()=>{const c=new AbortController();fetch(publicAsset('/data/language-inference.json'),{signal:c.signal}).then(r=>r.ok?r.json() as Promise<{cohorts:Audit[]}>:null).then(r=>{if(r)setAudits(r.cohorts)}).catch(()=>{});return()=>c.abort()},[]);
 useEffect(()=>{const current=models.find(m=>m.export_id===selected);if(current&&current.language!=='en')setChoice(current.language)},[models,selected]);
 const baseline=models.find(m=>m.language==='en');
 const choices=models.filter(m=>m.language!=='en');
 const target=choices.find(m=>m.language===choice)??choices[0];
 if(!baseline||!target)return null;
 const map=pairwise.find(p=>p.aggregation===aggregation&&[p.experiment_a,p.experiment_b].includes(baseline.experiment_id)&&[p.experiment_a,p.experiment_b].includes(target.experiment_id));
 const audit=audits.find(a=>a.export_ids.includes(baseline.export_id)&&a.export_ids.includes(target.export_id));
 const test=audit?.comparisons.find(c=>[c.a,c.b].includes('en')&&[c.a,c.b].includes(target.language));
 const accuracy=test?(test.a==='en'?1:-1)*test.mae_difference_b_minus_a_km:0;
 const largest=[...(map?.capital_displacements??[])].sort((a,b)=>b.displacement_km-a.displacement_km).slice(0,8);
 return <div className="language-evidence">
  <div className="evidence-heading"><h3>Small on the map. Measurable in the answers?</h3><label>Compare English with <select value={target.language} onChange={e=>setChoice(e.target.value)}>{choices.map(m=><option key={m.language} value={m.language}>{m.label}</option>)}</select></label></div>
  <div className="evidence-cards">
   <div><span>Average capital shift</span><strong>{fmt(map?.mean_aligned_map_displacement_km)} <small>km</small></strong><p>After globally aligning the two spherical fits. A shift of tens of kilometres is subtle on a world map.</p></div>
   <div><span>Difference in distance judgments</span><strong>{fmt(test?.mean_absolute_median_disagreement_km)} <small>km</small></strong><p>{test?`Mean absolute difference between pair medians. Adjusted p = ${fmt(test.judgment_p_holm,4)}${test.judgment_p_holm<.05?': detectable under the within-pair exchangeability test.':': no detectable departure under this test.'}`:'No matched inferential audit has been published for this cohort.'}</p></div>
   <div><span>Change in distance error</span><strong>{test?`${accuracy>0?'+':''}${fmt(accuracy,1)}`:'—'} <small>km</small></strong><p>{test?`${target.label} minus English median-based MAE; positive means larger error. Adjusted p = ${fmt(test.accuracy_p_holm,4)} under the full-distribution exchangeability null.`:'Inference uses complete pairs and median estimates.'}</p></div>
  </div>
  {largest.length>0&&<details className="capital-differences"><summary>Which capitals move most between these two maps?</summary><ol>{largest.map(p=><li key={p.place_id}><span>{p.capital_name}</span><meter min={0} max={largest[0].displacement_km||1} value={p.displacement_km} aria-label={`${p.capital_name}: ${fmt(p.displacement_km)} kilometres`}/><b>{fmt(p.displacement_km)} km</b></li>)}</ol><p className="small-note">Descriptive shifts between fitted positions, in kilometres. These are not significance tests for individual cities.</p></details>}
  {audit&&<p className="small-note">Tests use {fmt(audit.complete_pairs)} common complete pairs of {fmt(audit.total_pairs)}, {fmt(audit.permutations)} within-pair permutations, and Holm correction across {audit.holm_family_size} tests. P-values concern response distributions for these fixed capitals, translations and model run, assuming independent calls. They do not test map shape or establish a causal language effect. The MAE test is not a general test of equal average accuracy under otherwise different distributions. Tests always use medians; map shifts follow the selected aggregation. <a href={publicAsset(audit.report_url)} download>Download full statistical audit</a>.</p>}
 </div>;
}
