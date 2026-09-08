'use client';
import LanguageEvidence, {type MapComparison} from '@/components/language-evidence';
import {publicAsset} from '@/lib/public-assets';
import {useEffect,useState} from 'react';
import {ArrowUpRight} from 'lucide-react';
import {Table,TableBody,TableCell,TableHead,TableHeader,TableRow} from '@/components/ui/table';
import {formatNumber as fmt,type Aggregation} from '@/lib/research';
interface Row {export_id:string;experiment_id:string;language:string;label:string;valid_samples:number;expected_samples:number;aggregations:Record<Aggregation,{mae_km:number;spearman:number;triangle_violation_rate:number;spherical_stress:number}>}
type Comparison = MapComparison;
interface Cohort {capital_count:number;model_label?:string;models:Row[];pairwise:Comparison[]}
interface Comparisons {cohorts:Cohort[];language_cohorts?:Cohort[]}
export default function ModelComparison({selected,aggregation,onSelect,dimension='model'}:{selected:string;aggregation:Aggregation;onSelect:(id:string)=>void;dimension?:'model'|'language'}){
 const [data,setData]=useState<Comparisons>({cohorts:[]});
 useEffect(()=>{const c=new AbortController();fetch(publicAsset('/data/comparisons.json'),{signal:c.signal}).then(r=>r.ok?r.json() as Promise<Comparisons>:null).then(r=>{if(r)setData(r)}).catch(()=>{});return()=>c.abort()},[]);
 const language=dimension==='language';
 const cohort=(language?data.language_cohorts??[]:data.cohorts).find(c=>c.models.some(m=>m.export_id===selected));
 if(!cohort||cohort.models.length<2)return null;
 const baseline=cohort.models.find(m=>m.language==='en');
 return <section className="panel model-comparison">
  <div className="panel-heading"><div><span className="kicker">{language?'Same model. Different prompt languages.':'Same capitals. Different models.'}</span><h2>{language?'Does language change the map?':'Compare the reconstructed worlds'}</h2></div><span className="pill">{cohort.capital_count} capitals each</span></div>
  <p>{language?`${cohort.model_label}. Same reported model version, settings, capitals and sampling depth. Click a language to explore its map.`:'Same prompt, language, sample count and entity set. Click a model to explore its map.'}</p>
  <Table><TableHeader><TableRow><TableHead>{language?'Prompt language':'Model'}</TableHead><TableHead>Mean error</TableHead><TableHead>Rank correlation</TableHead><TableHead>Triangle violations</TableHead><TableHead>Spherical stress</TableHead>{language&&<><TableHead>Map shift vs English</TableHead><TableHead>Valid responses</TableHead></>}</TableRow></TableHeader><TableBody>{cohort.models.map(m=>{
   const s=m.aggregations[aggregation];
   const comparison=cohort.pairwise.find(p=>p.aggregation===aggregation&&[p.experiment_a,p.experiment_b].includes(m.experiment_id)&&[p.experiment_a,p.experiment_b].includes(baseline?.experiment_id??''));
   const shift=m.experiment_id===baseline?.experiment_id?0:comparison?.mean_aligned_map_displacement_km;
   return <TableRow key={m.export_id} data-state={m.export_id===selected?'selected':undefined}><TableCell><button className="model-link" onClick={()=>onSelect(m.export_id)}>{m.label}<ArrowUpRight size={14}/></button></TableCell><TableCell>{fmt(s.mae_km)} km</TableCell><TableCell>{fmt(s.spearman,4)}</TableCell><TableCell>{fmt(s.triangle_violation_rate*100,2)}%</TableCell><TableCell>{fmt(s.spherical_stress,4)}</TableCell>{language&&<><TableCell>{fmt(shift)} km</TableCell><TableCell>{fmt(m.valid_samples)} / {fmt(m.expected_samples)}</TableCell></>}</TableRow>
  })}</TableBody></Table>
  <p className="small-note">{language?'City and country names stay in English; the complete instructions are translated. English was rerun with the same numeric-format rule. Map shift is the mean capital displacement after globally aligning the two spherical fits. These specific translations have not been independently validated by native speakers; differences may include translation effects. The statistical panel below reports separate tests on distance judgments.':'Gemini 2.5 uses a zero thinking budget; Gemini 3 and 3.5 use minimal thinking, which is not guaranteed to be zero. These are descriptive comparisons, not significance tests.'}</p>
  {language&&<LanguageEvidence models={cohort.models} pairwise={cohort.pairwise} selected={selected} aggregation={aggregation}/>}
  <a className="comparison-download" href={publicAsset('/data/comparisons.json')} download>Download {language?'language':'model'} correlations and map displacement</a>
 </section>
}
