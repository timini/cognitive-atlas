# The 100-capital paper

The revised [paper](cognitive-atlas-paper.pdf) examines **Gemini 3.5 Flash across 100 capitals**, with ten distance estimates per pair under English, Arabic, and written Chinese instructions. It contains 148,500 completed answers. The main conclusions distinguish observed geometry, metric consistency, and response-distribution differences.

The [response to reviews](REVIEW-RESPONSE.md) tracks all 45 numbered findings and four publication-readiness requirements. The revised paper incorporates new quality-control sensitivities, geometric reference fits, optimizer diagnostics, regional distance balancing, and bootstrap calibration. Independent human scientific and language review remain outstanding; this is a completed manuscript revision, not a peer-reviewed publication. No author identity or affiliation has been assigned.

## Read and explore

- [Public atlas](https://timini.github.io/cognitive-atlas/)
- [Public PDF](https://timini.github.io/cognitive-atlas/paper/cognitive-atlas-paper.pdf)
- [Complete public reproduction package](https://timini.github.io/cognitive-atlas/paper/reproduction.zip)
- [LaTeX source](main.tex) and [bibliography](references.bib)

The source GitHub repository is private. The public website serves the paper, supporting reports, and downloadable experiment data. No archival DOI is assigned. The paper concerns this single model and its three instruction conditions; schema-constrained integration checks are not research observations in this study.

## Build and verify

From the repository root:

```sh
uv sync --frozen --group paper
make -C paper
make -C paper verify
uv run pytest -q
```

A TeX installation with `pdflatex`, `bibtex`, and the packages named in `main.tex` is required. On macOS with BasicTeX:

```sh
make -C paper PDFLATEX=/Library/TeX/texbin/pdflatex BIBTEX=/Library/TeX/texbin/bibtex
```

The normal build checks **expected** input and release hashes before generating figures or tables. It never refreshes those expectations automatically. `input-lock.json` freezes the three exports, raw responses, geographic inputs, and dependency lock. `release-lock.json` additionally freezes the revised analysis code, computed evidence, manuscript, and relevant source dependencies. A mismatch stops the build.

Recompute the new QC, local contrasts, geometry, calibration, and range-retained geometry with `make -C paper analyze`. This explicitly regenerates reports. On the recorded runtime, deterministic results should agree; platform or dependency differences may change optimizer details or environment metadata. Compare against the committed reports, including numerical tolerances, before considering a new release. An intentional release update uses `uv run python -m paper.revision100.freeze`; this is an authoring operation, not part of reproduction. The two expensive global audits are frozen published inputs: their reproducible entry points are `scripts/audit_language_group.py` and `scripts/audit_map_group.py`, supplied with the three exact `result.json` paths in `experiment-index.json`.

No paper build or analysis makes model calls or requires an API key. Synthetic values appear only in the explicitly separate bootstrap method-calibration report and never enter experiment results.

## Evidence and interpretation

| Evidence | Location |
|---|---|
| Raw source contract and selected three exports | `input-lock.json`, `experiment-index.json` |
| Global 4,999-permutation distance audit | `results/language-difference-audit.json` |
| 999-permutation map audit, including all null statistics | `results/map-difference-audit.json` |
| Parser replay, exclusions, variability and scheduling | `revision100/qc.py`, `revision100/qc.json` |
| WGS84 control, 12-start fits, spectra and neighbors | `revision100/geometry.py`, `revision100/geometry.json` |
| Regional contrasts, distance balance, capital omissions | `revision100/local.py`, `revision100/local.json` |
| Range-retained geometry sensitivity | `revision100/range_geometry.py`, `revision100/range_geometry.json` |
| Bootstrap coverage and failure diagnostics | `revision100/calibration.py`, `revision100/calibration.json` |
| Primary references and operational group definitions | `revision100/reference-notes.md`, `revision100/groups.json` |
| Exact prompt strings and release provenance | `results/` |
| Tables and vector figures | `generated/`, `figures/` |

Distance and map randomization use a strong response-distribution exchangeability null. Rejection does not establish unequal population medians or isolate a language effect. Regional summaries evaluate individual-response error, rather than error of pair medians. Associated pairs usually have only one endpoint in the operational group. The regional bootstrap is an empirical approximation: calibration works reasonably in regular scenarios but fails severely for unseen rare tails. Its intervals do not quantify uncertainty over new capitals, prompts, dates, or model releases.
