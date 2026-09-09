# Validation record

Validated locally on 9 September 2026. The manuscript uses only the three
100-capital Gemini 3.5 Flash conditions: English, Arabic, and written Chinese.

## Data and numerical evidence

- Verified all 42 frozen input hashes, including the three unmodified experiment
  exports, raw observations, geographic inputs, and global statistical audits.
- Verified the 38-file release contract covering manuscript, analysis code,
  computed evidence, source dependencies, and input identities. A deliberate
  input modification is rejected by the build contract in the test suite.
- Replayed the recorded parser against saved responses: zero classification or
  value mismatches. Reconciled 148,500 completed slots, 148,504 attempts, 148,491
  valid answers, and the 4,948-pair complete-case subset.
- Computed QC and range-retained sensitivities, WGS84 reference fits, 12-start
  spherical-fit diagnostics, nearest-neighbor and metric-validity checks,
  regional error contrasts, distance balance, and capital-omission checks.
- Checked the frozen distance and map randomization results, their exact null
  hypotheses, Monte Carlo resolution, and separate multiplicity families.
- Calibrated the regional bootstrap in explicitly synthetic method checks.
  Reported its severe rare-tail failure rather than claiming general coverage.
- Completed an independent agent reading of the final numerical claims against
  their source reports. The response document tracks all ten reviews, including
  requests requiring new data, additional methods, or human review.

## Software and document checks

- `pytest -q`: 78 Python tests passed.
- Frontend tests: 6 passed.
- Python lint and frontend type checking passed.
- Built the LaTeX source with pdfTeX / TeX Live 2026 and BibTeX. The final log has
  no undefined references or citations, overfull boxes, or oversized floats.
- Rendered and visually inspected all 15 pages, including figures, captions,
  bibliography, protocol details, and the complete capital list.
- Verified extracted PDF text and the absence of unresolved reference markers.

The public reproduction bundle includes this source, observed data, computed
reports, and checksums. Its publication manifest separately records the PDF and
bundle SHA-256 digests. Public deployment verification is recorded in hosting
build metadata rather than being inferred from a local build.

These checks establish implementation and document consistency. They do not
constitute independent human peer review, native-speaker validation,
preregistration, or evidence that provider responses are independent. No new
model calls were made while revising the paper. GitHub Actions execution is not
claimed: account billing prevented ordinary workflow runs, so validation was
performed locally.
