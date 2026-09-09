# Academic review reports

Ten distinct review agents assessed the manuscript on 9 September 2026, with separate assignments covering empirical claims, methods, writing, and conclusions. The runtime allowed three reviewers alongside the coordinator, so the reviews ran in overlapping batches rather than ten simultaneously. These are AI-assisted critical reviews, not journal peer review or independent human certification.

The reports refer to the source revision identified in each report. The current paper incorporates their feedback and uses only the 100-capital study. See the [finding-by-finding response](../paper/REVIEW-RESPONSE.md) for completed changes and explicit future-work limitations. Prior manuscript versions remain in Git history.

| Review | Scope and report | Agent | GitHub issue |
|---|---|---|---|
| 01 | [Empirical claims and numerical verification](review-01-empirical-claims.md) | `review_01_claims` | [#3](https://github.com/timini/cognitive-atlas/issues/3) |
| 02 | [Statistical inference](review-02-statistical-inference.md) | `review_02_inference` | [#1](https://github.com/timini/cognitive-atlas/issues/1) |
| 03 | [Writing, structure, and terminology](review-03-academic-writing.md) | `review_03_writing` | [#2](https://github.com/timini/cognitive-atlas/issues/2) |
| 04 | [Geometric methods](review-04-geometric-methods.md) | `review_04_geometry` | [#4](https://github.com/timini/cognitive-atlas/issues/4) |
| 05 | [Multilingual experimental design](review-05-multilingual-design.md) | `review_05_multilingual` | [#5](https://github.com/timini/cognitive-atlas/issues/5) |
| 06 | [References and source fidelity](review-06-references.md) | `review_06_references` | [#6](https://github.com/timini/cognitive-atlas/issues/6) |
| 07 | [Computational reproducibility](review-07-reproducibility.md) | `review_07_reproducibility` | [#7](https://github.com/timini/cognitive-atlas/issues/7) |
| 08 | [Sampling and quality control](review-08-sampling-quality-control.md) | `review_08_sampling_qc` | [#8](https://github.com/timini/cognitive-atlas/issues/8) |
| 09 | [Novelty and theoretical framing](review-09-novelty-framing.md) | `review_09_novelty` | [#9](https://github.com/timini/cognitive-atlas/issues/9) |
| 10 | [Conclusions and publication readiness](review-10-conclusions-publication.md) | `review_10_conclusions` | [#10](https://github.com/timini/cognitive-atlas/issues/10) |

## Main revision priorities

The publication-readiness reviewer requested major revision; the current manuscript addresses those reporting and interpretation findings. The numerical and provenance audits reproduced the checked historical results. The reports identify interpretation and reporting problems that informed the revision:

- Narrow significance claims to the response-distribution null actually tested. Different variability can produce rejection even when underlying median judgments agree.
- Separate effects of the particular translated prompts from general effects of language. Report geographic imbalance and sensitivity in the exploratory local-language analysis.
- Quantify the influence of response exclusions. Retaining readable over-range estimates reverses the tiny descriptive English–Chinese accuracy ordering in the older study.
- Make the scientific contribution explicit relative to prior prompted-distance reconstruction work. Lead with effect sizes and the distinction between accuracy and consistency.
- Strengthen source provenance, bootstrap justification, and reporting of geometric reference controls. Update the paper’s data-availability statement for the public atlas.

The current manuscript, README, and website explanations reflect the response document. Review records remain open where requested work requires new data or human assessment. Each report records its own scope and verification limits, and overlapping findings are retained rather than suppressed.
