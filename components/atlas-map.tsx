'use client';
import {useMemo, useState} from 'react';
import {Minus, Plus, RotateCcw} from 'lucide-react';
import {interpolate, pathFor, type Algorithm, type Layer, type MapView, type Place, type XY} from '@/lib/research';

interface Props { places: Place[]; layer: Layer; algorithm: Algorithm; amount: number; view: MapView; region: string; selection: string[]; onSelect: (id: string) => void; onHover: (id: string) => void; actual?: boolean; compact?: boolean }
export default function AtlasMap({places, layer, algorithm, amount, view, region, selection, onSelect, onHover, actual=false, compact=false}: Props) {
  const [zoom, setZoom] = useState(1);
  const [center, setCenter] = useState<XY>([0, 0]);
  const t = actual ? 0 : amount;
  const isPlanar = algorithm !== 'spherical' && !actual;
  const coastT = isPlanar || view !== 'warped' ? 0 : t;
  const paths = useMemo(() => layer.countries.map(c => ({name:c.name, d:c.rings.map(r=>pathFor(r.source,r.target,coastT)).join('')})), [layer,coastT]);
  const rec = layer.reconstructions[algorithm];
  const xy = places.map((p,i) => interpolate([p.longitude,-p.latitude],rec.coordinates[i],t));
  const maxError = Math.max(...layer.capital_metrics.map(p=>p.mae_km),1);
  const maxCV = Math.max(...layer.capital_metrics.map(p=>p.mean_cv),.001);
  const visible = (p: Place) => region === 'All regions' || p.continent === region;
  const colors = (i: number) => view==='error' ? `hsl(${110-105*layer.capital_metrics[i].mae_km/maxError} 85% 65%)` : '#aaf078';
  return <div className={'map-wrap '+(compact?'compact':'')}>
    <div className="map-caption"><span className="live-dot"/>{actual?'Actual Earth':isPlanar?'Reconstructed capital geometry':t===0?'Actual Earth':'Model-implied Earth'}<span className="map-projection">{isPlanar?'Planar MDS · aligned globally':'Equirectangular projection'}</span></div>
    <svg className="map-svg" viewBox={`${center[0]-190/zoom} ${center[1]-95/zoom} ${380/zoom} ${190/zoom}`} role="group" aria-label={actual?'Actual capital locations':'Interactive reconstructed capital map'}>
      <defs><clipPath id={'clip-'+(actual?'actual':'model')}><rect x="-180" y="-90" width="360" height="180"/></clipPath><marker id={'arrow-'+(actual?'actual':'model')} viewBox="0 0 8 8" refX="7" refY="4" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M 0 0 L 8 4 L 0 8 z" fill="#aaf078"/></marker></defs>
      <g stroke="#253247" strokeWidth=".2" fill="none">{Array.from({length:13},(_,i)=><path key={'v'+i} d={`M${-180+i*30},-90 V90`}/>)}{Array.from({length:7},(_,i)=><path key={'h'+i} d={`M-180,${-90+i*30} H180`}/>)}</g>
      {!isPlanar && view!=='capitals' && <g clipPath={`url(#clip-${actual?'actual':'model'})`} fill="#1b2b3e" stroke="#53657b" strokeWidth=".22" fillRule="evenodd">{paths.map(c=><path key={c.name} d={c.d}><title>{c.name} · coastline interpolation is illustrative</title></path>)}</g>}
      {!actual && view==='displacement' && <g stroke="#aaf078" strokeWidth=".4" opacity=".75">{places.map((p,i)=>visible(p)&&<path key={p.id} d={`M${p.longitude},${-p.latitude}L${xy[i][0]},${xy[i][1]}`} markerEnd="url(#arrow-model)"/>)}</g>}
      {places.map((p,i)=>visible(p)&&<g key={p.id} opacity={selection.includes(p.id)?1:.9} onMouseEnter={()=>onHover(p.id)}>
        {!actual && view==='uncertainty' && <circle cx={xy[i][0]} cy={xy[i][1]} r={2+9*layer.capital_metrics[i].mean_cv/maxCV} fill="#9ab5ff" opacity=".15" stroke="#9ab5ff" strokeWidth=".25"/>}
        {selection.includes(p.id)&&<circle cx={xy[i][0]} cy={xy[i][1]} r="2.5" fill="none" stroke="#e7fbd9" strokeWidth=".35"/>}
        <circle className="capital-point" tabIndex={0} role="button" aria-label={`Select ${p.capital_name}`} onFocus={()=>onHover(p.id)} onClick={()=>onSelect(p.id)} onKeyDown={e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();onSelect(p.id)}}} cx={xy[i][0]} cy={xy[i][1]} r={(view==='error'&&!actual?1.2+2*layer.capital_metrics[i].mae_km/maxError:1.2)} fill={actual?'#8da0b9':colors(i)} stroke="#080f19" strokeWidth=".4"><title>{p.capital_name}, {p.country_name}</title></circle>
        {(selection.includes(p.id)||(!compact&&zoom>1))&&<text x={xy[i][0]+3} y={xy[i][1]+1} className="city-label">{p.capital_name}</text>}
      </g>)}
      {!isPlanar && <g className="coordinate-label"><text x="-178" y="88">180°W</text><text x="-3" y="88">0°</text><text x="166" y="88">180°E</text></g>}
    </svg>
    <div className="map-controls"><button aria-label="Zoom in" onClick={()=>{setZoom(z=>Math.min(4,z*1.5));const index=places.findIndex(p=>p.id===selection[0]);if(index>=0)setCenter(xy[index])}}><Plus size={16}/></button><button aria-label="Zoom out" onClick={()=>setZoom(z=>Math.max(1,z/1.5))}><Minus size={16}/></button><button aria-label="Reset map" onClick={()=>{setZoom(1);setCenter([0,0])}}><RotateCcw size={15}/></button></div>
    <div className="map-legend">{view==='uncertainty'?'Larger halo = greater variation across responses':view==='error'?'Green → amber → red: increasing distance error':isPlanar?'Coordinates fit distances; global Procrustes alignment only':'Select two capitals to inspect their distance estimates'}</div>
  </div>
}
