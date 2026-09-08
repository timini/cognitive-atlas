export type XY = [number, number];
export interface Place { id: string; capital_name: string; country_name: string; latitude: number; longitude: number; continent: string; region: string; decision: string }
export interface Pair { id: string; place_a_id: string; place_b_id: string; true_distance_km: number; samples: number[]; n: number; mean: number; median: number; trimmed_mean: number; robust: number; std: number | null; variance: number | null; cv: number | null; mad: number; min: number; max: number; iqr: number; outliers: number; missing_samples: number; mean_ci_low: number | null; mean_ci_high: number | null }
export type Aggregation = 'mean' | 'median' | 'trimmed_mean' | 'robust';
export type Algorithm = 'spherical' | 'classical' | 'metric' | 'nonmetric';
export type MapView = 'warped' | 'displacement' | 'error' | 'uncertainty' | 'capitals';
export interface Reconstruction { coordinates: XY[]; raw_coordinates?: XY[]; inferred_latlon?: XY[]; stress: number; stress_definition: string; displacement_km?: number[]; mean_displacement_km?: number; converged?: boolean }
export interface Country { name: string; rings: {source: XY[]; target: XY[]}[] }
export interface Layer {
  metrics: Record<string, number | string>;
  reconstructions: Record<Algorithm, Reconstruction>;
  dimensionality: {dimensions: number; stress: number}[];
  capital_metrics: {place_id: string; mae_km: number; mean_cv: number; mean_std_km: number}[];
  countries: Country[];
  mesh: {foldovers: number; source: XY[]; target: XY[]; triangles: number[][]};
}
export interface Research {
  experiment: {id: string; model: string; model_label?: string; provider: string; created_at: string; language: string; language_label?: string; prompt_family?: string; sampling_count: number; prompt_template: string; parameters: {temperature: number; top_p: number; max_tokens: number; thinking_budget?: number; thinking_level?: string}; dataset_sha256: string; code_revision: string; sampling_strategy: string};
  analysis_id: string; places: Place[]; pairs: Pair[]; layers: Record<Aggregation, Layer>;
  quality: {attempts: number; valid: number; invalid_attempts: number; estimated_cost_usd: number};
  limitations: string[];
}
export interface ExperimentIndex {id: string; model: string; model_label?: string; capital_count?: number; language: string; language_label?: string; prompt_family?: string; created_at: string; url: string}
export const formatNumber = (n: number | null | undefined, digits = 0) => n == null || !Number.isFinite(n) ? '—' : new Intl.NumberFormat('en-GB', {maximumFractionDigits: digits}).format(n);
export const interpolate = (a: XY, b: XY, t: number): XY => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];
export const pathFor = (ring: XY[], target: XY[], t: number) => 'M' + ring.map((p,i) => interpolate(p, target[i], t).map(v => v.toFixed(3)).join(',')).join('L') + 'Z';
export function histogram(samples: number[], count = 5) {
  if (!samples.length) return [];
  const min = Math.min(...samples), max = Math.max(...samples);
  if (min === max) return [{low: min, high: max, count: samples.length}];
  const width = (max - min) / count;
  const bins = Array.from({length: count}, (_,i) => ({low: min + i * width, high: min + (i+1) * width, count: 0}));
  for (const x of samples) bins[Math.min(count - 1, Math.floor((x - min) / width))].count++;
  return bins;
}

export const languageNames: Record<string, string> = {en: 'English', fr: 'French', es: 'Spanish', ar: 'Arabic', zh: 'Mandarin Chinese'};
export function renderPrompt(template: string, a: Place, b: Place) {
  const values: Record<string,string> = {city_a: a.capital_name, country_a: a.country_name, city_b: b.capital_name, country_b: b.country_name};
  return template.replace(/\{(city_a|country_a|city_b|country_b)\}/g, (_, name: string) => values[name]);
}

export function experimentLabel(entry: ExperimentIndex) {
  const model = entry.model_label ?? entry.model.replace('gemini-', 'Gemini ');
  const language = languageNames[entry.language] ?? entry.language;
  return entry.prompt_family
    ? `${language} · ${model} · Language study · ${entry.capital_count ?? 20} capitals`
    : `${model} · ${entry.capital_count ?? 20} capitals · ${language}`;
}
