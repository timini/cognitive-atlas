'use client';
import {useEffect,useState} from 'react';
import {ArrowUpRight} from 'lucide-react';
import {Table,TableBody,TableCell,TableHead,TableHeader,TableRow} from '@/components/ui/table';
import {formatNumber as fmt,type Aggregation} from '@/lib/research';
interface Row {export_id:string;label:string;valid_samples:number;aggregations:Record<Aggregation,{mae_km:number;spearman:number;triangle_violation_rate:number;spherical_stress:number}>}
interface Cohort {capital_count:number;models:Row[]}
export default function ModelComparison({selected,aggregation,onSelect}:{selected:string;aggregation:Aggregation;onSelect:(id:string)=>void}){
 const [cohorts,setCohorts]=useState<Cohort[]>([]);
 useEffect(()=>{const c=new AbortController();fetch('/data/comparisons.json',{signal:c.signal}).then(r=>r.ok?r.json():null).then(r=>{if(r)setCohorts((r as {cohorts:Cohort[]}).cohorts)}).catch(()=>{});return()=>c.abort()},[]);
 const cohort=cohorts.find(c=>c.models.some(m=>m.export_id===selected));
 if(!cohort||cohort.models.length<2)return null;
 return <section className="panel model-comparison"><div className="panel-heading"><div><span className="kicker">Same capitals. Different models.</span><h2>Compare the reconstructed worlds</h2></div><span className="pill">{cohort.capital_count} capitals each</span></div><p>Same prompt, language, sample count and entity set. Click a model to explore its map.</p><Table><TableHeader><TableRow><TableHead>Model</TableHead><TableHead>Mean error</TableHead><TableHead>Rank correlation</TableHead><TableHead>Triangle violations</TableHead><TableHead>Spherical stress</TableHead></TableRow></TableHeader><TableBody>{cohort.models.map(m=>{const s=m.aggregations[aggregation];return <TableRow key={m.export_id} data-state={m.export_id===selected?'selected':undefined}><TableCell><button className="model-link" onClick={()=>onSelect(m.export_id)}>{m.label}<ArrowUpRight size={14}/></button></TableCell><TableCell>{fmt(s.mae_km)} km</TableCell><TableCell>{fmt(s.spearman,4)}</TableCell><TableCell>{fmt(s.triangle_violation_rate*100,2)}%</TableCell><TableCell>{fmt(s.spherical_stress,4)}</TableCell></TableRow>})}</TableBody></Table><p className="small-note">Gemini 2.5 uses a zero thinking budget; Gemini 3 and 3.5 use minimal thinking, which is not guaranteed to be zero. These are descriptive comparisons, not significance tests.</p><a className="comparison-download" href="/data/comparisons.json" download>Download model-to-model correlations and map displacement</a></section>
}
