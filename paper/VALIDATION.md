# Validation record

Validated locally on 8 September 2026.

- Recomputed the city-label permutation audit for the original three models.
- Recomputed all ten matched language comparisons (4,999 permutations each).
- Recomputed the local-language bootstrap (9,999 replicates per language).
- Checked bootstrap standard errors against independent analytic variance calculations.
- `pytest -q`: 48 tests passed, including five new paper audit tests.
- `ruff check atlas tests scripts paper/scripts`: passed.
- `git diff --check`: passed.
- Built the LaTeX source with pdfTeX / TeX Live 2026 and BibTeX.
- The final log has no undefined references, undefined citations, or overfull boxes.
- Rendered and visually inspected all 12 pages; revised figure legends and float spacing.
- Verified PDF text extraction and the absence of unresolved `??` references.
- Confirmed result-file SHA-256 hashes against the original experiment exports and
  analysis script hashes against the recomputed audit artifacts.

These checks validate the implementation and document consistency. They do not
constitute independent scientific peer review, native-speaker validation, a
preregistered confirmatory study, or a test of the independence of API responses.
No new model calls were made while producing this paper. GitHub Actions execution
is not claimed by this local validation record.
