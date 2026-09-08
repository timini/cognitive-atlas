# Cognitive Atlas research paper

`cognitive-atlas-paper.pdf` is the compiled research draft. `main.tex` and
`references.bib` are the editable LaTeX source and bibliography. No author identity
or affiliation has been assigned; this is not a journal submission or a peer-reviewed paper.

The paper covers the 50-capital model comparison, the matched five-language
Gemini 3.5 Flash study, and exploratory tests of a local-language advantage.
Its input exports are frozen in `experiment-index.json`; later 100-capital cohorts do not alter this historical study.
It does not claim a literal measurement of hidden model representations.

## Build the paper

From the repository root, install the locked research and plotting environment:

```sh
uv sync --frozen --group paper
make -C paper
```

A TeX installation providing `pdflatex` and `bibtex` is required, along with
standard packages including `lmodern`, `geometry`, `booktabs`, `amsmath`,
`microtype`, `graphicx`, and `hyperref`. With BasicTeX on macOS:

```sh
make -C paper PDFLATEX=/Library/TeX/texbin/pdflatex BIBTEX=/Library/TeX/texbin/bibtex
```

The default build regenerates all figures and numeric table rows from the saved
measurements and inferential results. It performs no LLM calls, needs no API key,
and does not change published experiment files.

## Recompute every inferential analysis

Run from the repository root:

```sh
uv run --frozen --group paper python paper/scripts/check_distance_structure.py
uv run --frozen --group paper python paper/scripts/check_language_differences.py
uv run --frozen --group paper python paper/scripts/local_language.py
make -C paper
uv run --frozen --group paper pytest -q tests/test_paper.py
```

The numerical audit scripts require the repository root as their working directory.
`make -C paper analyze` runs those three scripts in order. Reanalysis takes several
minutes and writes only under `paper/results/`. All randomization seeds are fixed.
Matplotlib creates vector PDF figures; no model-generated graphics or synthetic
scientific observations are used. Figures are not screenshots of the website.

## What is measured

- Global language tests use the median of ten estimates per pair. Each comparison
  shuffles language labels independently within each fixed pair. The null is
  exchangeability of the entire response distributions, not merely equal MAE.
  Holm adjustment covers 20 tests: ten matrix-disagreement and ten MAE-contrast
  statistics. These tests are conditional on independent API responses.
- Local-language tests use **mean single-response absolute error**, not error of
  the ten-response median. Positive gain means lower error than English. A pair
  belongs to the language group when at least one endpoint is included. The
  interaction subtracts the gain on the remaining pairs.
- The local bootstrap independently resamples observations within each pair and
  language. Centered deviations have a sqrt(10/9) correction to match unbiased
  sample-variance estimates. Basic 95% intervals are pointwise; only p-values are
  Holm-adjusted (eight tests). The analytic standard error cross-check is recorded.
- The 1,223 common complete pairs exclude Buenos Aires–Hanoi and Seoul–Moscow,
  which have invalid responses in at least one language. Invalid observations
  remain in the raw research exports. All-pair descriptive metrics are separately
  reported; they must not be mixed with complete-case inference.
- Small conditional p-values concern sampling calls on the fixed city set. They
  do not estimate uncertainty over new countries, translations, dates, or models.
  Country-language affiliation is a documented coarse proxy. This analysis is
  exploratory, not preregistered and not causally identified.

## Supplement files

- `results/provenance.json`: every experiment/export ID, raw result SHA-256,
  collection source revision, date, and model condition.
- `results/exact-language-prompts.json`: byte-preserving Unicode prompt strings
  from the five manifests, including the shared numeric-format instruction.
- `results/language-difference-audit.json`: 4,999 within-pair permutations per
  language comparison, all effect sizes and adjusted p-values.
- `results/local-language-audit.json`: country groups, 9,999 bootstrap replicates,
  intervals, corrected p-values, analytical variance validation, and each
  leave-one-associated-capital-out result.
- `results/distance-structure-audit.json`: the original three-model geographic
  signal audit using 9,999 city-label permutations and repeated-response counts.
- `results/manuscript-checks.json`: cross-checks for totals and the Spanish effect.
- `generated/*.tex`: data-generated table bodies; edit data or scripts, not rows.
- `figures/*.pdf`: reproducible vector figures.

All original responses, manifests, distances and reconstructions remain under
`public/data/<export-id>/`. The repository is private; the manuscript does not
claim publicly archived data or a DOI. References identify related earlier work,
including prior MDS reconstructions and multilingual distance-estimation studies.
