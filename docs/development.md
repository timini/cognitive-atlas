# Development and reproducibility

The [project overview](../README.md) explains the research. The [paper guide](../paper/README.md) documents the current study and its frozen analysis inputs.

## Local setup

Use Python 3.12 with uv and Node 22.18 or newer.

```sh
uv sync --frozen --group paper
npm ci
npm run dev
```

The website reads precomputed exports. The Python runner collects observations independently of the website; credentials are never included in published assets.

## New collections

Copy `.env.example` to `.env` and set `GEMINI_API_KEY`. Prepare a condition, inspect its call and cost estimate, then explicitly run it:

```sh
uv run atlas create --dataset data/capitals-100-v3.csv --model gemini-3.5-flash --protocol great-circle-json-object-v3 --samples 10 --budget 15
uv run atlas estimate runs/EXPERIMENT_ID
uv run atlas run runs/EXPERIMENT_ID --max-jobs 4
uv run atlas run runs/EXPERIMENT_ID
uv run atlas status runs/EXPERIMENT_ID
uv run atlas analyze runs/EXPERIMENT_ID
uv run atlas export runs/EXPERIMENT_ID runs/EXPERIMENT_ID/analyses/ANALYSIS_ID
uv run atlas compare
```

The second run resumes the same condition. Complete collection before publishing an analysis. Ten samples over 100 capitals require 49,500 completed responses per condition, plus any retries. A run stops at its recorded reservation ceiling. Reported token costs are estimates rather than invoices.

New command-line collections default to `great-circle-json-object-v3`: the Google request supplies `responseMimeType: application/json` and a JSON schema with one required numeric `distance_km` field. The manifest records the complete schema and translated prompt. The parser decodes JSON and rejects extra or duplicate keys, numeric strings, booleans, non-finite numbers, and malformed documents without regular-expression parsing. The schema contains no geographic range constraint; plausibility checking is separate.

A nine-call integration check using London, Cairo, and Beijing under English, Arabic, and Chinese instructions returned nine valid structured responses. Those integration checks are separate from the published numeric-text study and are not scientific comparison data. Resuming any existing condition uses its recorded protocol. Low-level library factories retain compatibility defaults, so library callers should specify the intended protocol explicitly.

For a new matched group:

```sh
uv run python scripts/run_languages.py prepare --group runs/new-language-condition.json --dataset data/capitals-100-v3.csv --languages en ar zh --protocol great-circle-json-object-v3 --budget 15
uv run python scripts/run_languages.py run --group runs/new-language-condition.json
uv run python scripts/analyze_group.py runs/new-language-condition.json
```

Budgets are per language. The shared process limiter pauses on rate limits and reduces dispatch rate. Transport, timeout, and eligible server failures are retried; invalid content is terminal and retained. A crash between remote completion and writing a checkpoint can repeat a paid request. File locking and checkpoint integrity checks target POSIX systems.

## Architecture

| Module | Responsibility |
|---|---|
| `atlas/data.py` | Canonical places, pair IDs, WGS84 distances |
| `atlas/experiment.py`, `atlas/response_schema.py` | Recorded experimental conditions and prompts |
| `atlas/providers.py` | Model adapter and structured requests |
| `atlas/runner.py`, `atlas/validation.py` | Queue, rate limits, retries, budgets, resume checks |
| `atlas/statistics.py`, `atlas/reconstruct.py` | Aggregation, consistency, embedding and alignment |
| `atlas/deformation.py` | Coastline interpolation and foldover diagnostics |
| `atlas/inference.py`, `atlas/map_inference.py` | Explicit matched-cohort randomization audits |
| `paper/revision100/` | Frozen manuscript analyses, sensitivities, calibration and release checks |
| `app/`, `components/` | Interactive atlas |

Each run records a manifest, canonical places and pairs, and append-only response attempts. Each attempt includes the exact prompt, raw answer and provider payload, parsed value, quality flag, timing, token usage, estimated cost, and returned model identifier. Exported results are preserved in Git. Changing prompts, schema, language, settings, or model creates a distinct condition.

The manuscript documents limits in historical execution provenance: a source revision does not prove a clean executed collector snapshot, and the original analysis identities omitted coastline/runtime inputs. Its current release locks bind the actual available files and analysis environment. They do not retroactively certify provider execution or reproduce future model weights.

## Validation and publication

```sh
uv run pytest -q
uv run ruff check atlas tests scripts paper/revision100
npm test
npm run typecheck
make -C paper
make -C paper verify
npm run build:pages
npm run verify:pages
```

Tests cover parsing, recorded schema requests, budget/resume behavior, geodesic and geometric controls, published-data invariants, and the paper’s locked inputs. Synthetic observations are limited to explicit implementation tests and method-calibration simulations. No browser-specific interaction testing is implied by a build check.

GitHub Pages serves the current static export under `/cognitive-atlas/`. After committing and pushing a validated checkout:

```sh
node scripts/deploy-pages.mjs
```

This updates the `gh-pages` branch without rewriting its history. Verify the Pages build and public `build-info.json` before considering publication complete. Only prepared public assets are deployed. Ordinary GitHub Actions can be unavailable because of account billing even when local validation and Pages publishing work.
