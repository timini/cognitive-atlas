# Cognitive Atlas

A working 20-capital research pilot that reconstructs the geographic geometry implied by Gemini's observable distance judgments. **CSV files, no database. No synthetic model measurements.**

## Run locally

Requires Python 3.12, uv, and Node 22.13+ (Node 22.18+ for the built-in TypeScript tests).

```sh
uv sync --frozen
npm ci
cp .env.example .env
# Put GEMINI_API_KEY in .env. It is ignored by Git and never sent to the website.
uv run atlas create --samples 10 --rpm 120 --concurrency 4 --budget 1
# Use .venv/bin/atlas, or uv run atlas, if atlas is not on PATH.
uv run atlas estimate runs/EXPERIMENT_ID
uv run atlas run runs/EXPERIMENT_ID --max-jobs 4
uv run atlas run runs/EXPERIMENT_ID
uv run atlas status runs/EXPERIMENT_ID
uv run atlas analyze runs/EXPERIMENT_ID
uv run atlas export runs/EXPERIMENT_ID runs/EXPERIMENT_ID/analyses/ANALYSIS_ID
npm run dev
```

The second `run` resumes the same immutable condition. It does not repeat completed samples. Use a new experiment for another model condition, language, prompt, or date. A dataset CSV with more reviewed capitals uses exactly the same runner; 195 capitals × 10 samples produces 189,150 calls. Do not run that global condition until its input dataset and budget are reviewed.

## Architecture

| Module | Responsibility |
|---|---|
| `atlas/data.py` | CSV I/O, stable IDs, canonical pairs, WGS84 geodesics |
| `atlas/experiment.py` | Immutable manifests, prompts, pricing and preflight estimates |
| `atlas/providers.py` | Provider protocol; Google Gemini adapter with no tools/history |
| `atlas/runner.py` | Bounded queue, concurrency, rate limits, retries, append-and-fsync checkpoints |
| `atlas/validation.py` | Detect edits to condition, places, or ground-truth pairs |
| `atlas/statistics.py` | Robust aggregation, bootstrap intervals, accuracy and metric validity |
| `atlas/reconstruct.py` | Classical, metric, non-metric, and spherical fitting; Procrustes |
| `atlas/deformation.py` | Delaunay deformation and triangle foldover diagnostics |
| `atlas/analysis.py` | Versioned analysis artifacts and immutable web exports |
| `app/`, `components/atlas-map.tsx` | React/Vinext exploration UI hosted on Cloudflare through Sites |

The website serves precomputed files. There is no API key, live query endpoint, server database, database service, or background model job in the deployed site. The Python runner operates on your computer. Static JSON exports act as the read API; individual CSVs remain downloadable evidence. New exported experiments appear in a manifest-driven selector after the next deployment.

## File schema

Each `runs/<experiment-id>/` contains:

- `manifest.json`: hash-derived ID, UTC creation time, dataset hash, source revision, software versions, model, language, exact prompt template, parameters, pricing assumptions, retry policy, run ceiling.
- `places.csv`: IDs, country/capital names, latitude/longitude, continent/region, ISO code, alternate/localized names, decision notes and Natural Earth source IDs.
- `pairs.csv`: deterministic unordered pair ID, both place IDs, WGS84 distance in km.
- `responses.csv`: experiment/pair/sample/attempt IDs, timestamp, exact prompt, complete response text and provider JSON, parsed km, quality class, terminal/retryable flags, latency, usage, cost estimate, resolved model version and finish reason.
- `analyses/<analysis-id>/`: aggregate CSV, each distance matrix, coordinates CSV and a JSON analysis artifact. IDs include response contents, analysis settings and analysis source hash.

The append-only response file is the checkpoint. A per-experiment OS file lock prevents two runner processes from writing it simultaneously. Within that process, a bounded asynchronous queue runs independently sampled single-turn requests. Each completed attempt is flushed and fsynced. A crash between remote completion and local fsync can repeat a paid request on resume: Gemini does not offer exactly-once idempotency for these calls. A malformed final CSV row stops resume instead of silently dropping observations. Preserve and repair that row manually. File locking currently targets macOS/Linux; use a POSIX environment on Windows.

Retry only HTTP 408/429/5xx and transport/timeouts, at most four attempts with exponential backoff, jitter and Retry-After. Invalid content and refusals are terminal observations. All attempts remain recorded. Fatal configuration/authentication failures stop scheduling. The conservative per-attempt reservation uses UTF-8 prompt bytes, framing allowance, output ceiling and configured prices; timeout reservations stay charged to the run ceiling. Usage-derived cost is an estimate, not a provider invoice. Pricing is explicitly gated to the verified Gemini 2.5 Flash-Lite condition; adding a model must add reviewed pricing rather than reusing its rate.

## Scientific choices

- Natural Earth coordinates provide a documented city-point reference. The 20-capital pilot is geographically dispersed, purposive, and not globally representative. Six inhabited continents are covered; Antarctica has no national capital. Pretoria is South Africa's executive capital; Cape Town and Bloemfontein are excluded. This is not yet the reviewed 195-state canonical dataset.
- Ground truth is GeographicLib's WGS84 inverse geodesic, kept separate from judgments. Spherical fitting uses a fixed mean Earth radius of 6371.0088 km, so a small sphere-versus-ellipsoid discrepancy remains.
- Ten independent single-turn requests per unordered pair. No tools are supplied, no prior responses are fed back, and no answer cache is shared across sample numbers. Temperature 1, top-p 0.95, 32 output tokens, thinking budget zero, no fixed generation seed. The parser accepts one positive numeric value (optional km), never a conveniently extracted number from prose. English thousands separators are supported; decimal-comma parsing needs a separate protocol before broad multilingual runs.
- Aggregations: mean, median, 10% trimming **per tail**, and Huber location with scale `max(1.4826 MAD, 1 km)`. Variance and standard deviation use `ddof=1`; unavailable one-sample statistics are null. The website's default median is a navigation default, not a scientific claim of superiority.
- All 1,140 triangles are checked for the pilot. Larger problems sample at most 200,000 uniformly sampled triples with replacement and a recorded seed. Unordered symmetry is imposed, not empirically established.
- Accuracy: MAE, RMSE, median absolute error, absolute relative error, signed error, Pearson, Spearman, Kendall, and three-neighbour preservation. Negative eigenmass diagnostics do not by themselves establish a low-dimensional valid geometry.
- Classical MDS is spectral; metric/non-metric MDS use four seeded starts. The 1–10 dimension curve reports distance-normalized residual stress. Non-metric stress uses fitted monotone disparities, so it is **not numerically interchangeable** with metric stress.
- Spherical initialization is derived from the estimated matrix, never from true locations. Four optimization starts fit angular distances; only then is one global orthogonal transformation aligned to Earth's unit vectors. No individual geographic anchors enter fitting. Planar MDS is globally aligned to an explicitly labeled equirectangular reference, not confused with inferred latitude/longitude. A true-Earth dimensionality baseline is included in the JSON export.
- Coastlines use a continuous piecewise-affine Delaunay field with fixed frame pins, densified boundaries and nearest longitude branches. It is illustrative interpolation, not evidence that the model believes a particular coastline. Foldovers are counted and displayed; continuity does not guarantee topology preservation. Inspect the capital-only view separately.
- Bootstrap intervals resample observations **within a pair** (1,000 replicates, fixed analysis seed) for the mean. They are conditional on these ten observations; identical replies do not establish epistemic certainty. Positional bootstrap clouds, formal model/language comparisons, ordinal triplet experiments and embedding-based semantic geography remain later research stages.
- Historical API behavior cannot be reproduced exactly on demand. Raw outputs and downstream computations are reproducible from saved artifacts. Every response stores Google's returned `modelVersion`; this API returned an alias rather than a more specific frozen checkpoint. Mixed returned versions are rejected for aggregate analysis.

## Validation

```sh
uv run pytest -q
uv run ruff check atlas tests scripts
npm test
npm run typecheck
npm run build
```

Tests cover analytical ground truth, numeric rejection, robust summaries, known Euclidean and spherical recovery, global alignment, deformation continuity at control points, retry preservation, budget checks, idempotent resume, immutable input detection and raw-CSV-to-published-metric checks. Provider doubles exist only under `tests/`; the published pilot consists solely of real API results. Browser-specific interaction and visual QA are not claimed by these tests. Optional WebMCP tools are feature-detected; they require a supporting browser for full integration validation.

## Deployment

The Sites project is registered in `.openai/hosting.json`. It runs on Cloudflare Workers and serves the research exports as assets. The initial deployment uses owner-only access. GitHub and Sites source remotes are separate; credentials must be supplied per operation, never persisted in remote URLs. Build, package using the Sites packaging helper, save the exact committed version, then publish it. No secret needs to be configured on the hosted site.

## Sources

- [Natural Earth populated places](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/) and [public-domain terms](https://www.naturalearthdata.com/about/terms-of-use/). Imported input hashes and source URLs are in `data/sources.json`.
- [GeographicLib geodesic documentation](https://geographiclib.sourceforge.io/Python/doc/code.html).
- [scikit-learn MDS](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.MDS.html).
- [Google generateContent API](https://ai.google.dev/api/generate-content), [thinking controls](https://ai.google.dev/gemini-api/docs/thinking), and [pricing](https://ai.google.dev/gemini-api/docs/pricing).
