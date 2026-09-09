# Response to the ten academic reviews

**Completed manuscript revision and response to review, 9 September 2026.** This document maps all **45 numbered findings** and four publication-readiness requirements to the current 100-capital paper. The reports refer to the earlier reviewed source at commit `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`; previous versions remain recoverable through Git history. The current paper and atlas include only the 100-capital English, Arabic, and written-Chinese conditions.

“Addressed” means that the stated reporting, calculation, or presentation change is included in this release. “Partial / future work” identifies an explicit limitation or a request that requires new observations, methods, or human review. Such items are not claimed completed. The issue records are retained, and AI-assisted review is not independent human peer review.

## Review 1 — empirical claims ([issue #3](https://github.com/timini/cognitive-atlas/issues/3))

Source: [review-01-empirical-claims.md](../reviews/review-01-empirical-claims.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R1.1 | Availability statement describes an access-controlled atlas despite public deployment. | **Addressed:** distinguish private source repository from the public GitHub Pages atlas and its public downloadable exports; give the frozen release and actual access routes. Check the deployed routes when publishing. Evidence: `paper/main.tex` availability section, `paper/README.md`, `paper/input-lock.json`, and the final release verification record. |
| R1.2 | Abstract calls differences substantial without an effect size. | **Addressed:** give observed 100-capital median disagreement, accuracy contrast, and/or fitted map displacement in kilometres before p-values; avoid an undefined adjective. Evidence: `paper/main.tex` abstract and results, `paper/revision100/qc.json`, `paper/revision100/geometry.json`, and the frozen language/map audit files. |

## Review 2 — statistical inference ([issue #1](https://github.com/timini/cognitive-atlas/issues/1))

Source: [review-02-statistical-inference.md](../reviews/review-02-statistical-inference.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R2.1 | Rejection of equal response distributions does not prove changed population median maps. | **Addressed:** state the strong within-pair exchangeability null for both distance and refitted-map tests. Describe differences between observed fitted maps separately. Explain that changes in dispersion can cause rejection even with equal population medians. Evidence: `paper/main.tex` inference methods, results, and conclusion; frozen 100-capital distance/map audits. **Requires future data/methods** for a general claim about stable language-specific central maps. |
| R2.2 | Request-level uncertainty lacks independent replication of language conditions. | **Partial / requires future data:** report consecutive within-pair scheduling, concurrent condition collection, one translation per language, one collection period, and unverified provider independence. Do not call a post hoc timestamp check independent replication. Randomized recorded blocks, repeated dates, and multiple translations remain future work. Evidence: `paper/main.tex` sampling/limitations, frozen manifests and response timestamps. The added `revision100/qc.json` reports dispatch spans, timestamp coverage, and canonical order. This is a descriptive scheduling audit, not a deconfounded estimate of time effects; repeated randomized blocks still require new data. |
| R2.3 | Variance matching is not validation of bootstrap coverage or type-I error. | **Addressed:** derive the variance multiplier and distinguish analytic-SE agreement from coverage. Added a clearly separate method-calibration simulation covering ties, unequal variances, skew/rare errors, zero-variance cells, and the tested family where feasible; report observed coverage/rejection with Monte Carlo uncertainty and its limited scope. Evidence: `paper/revision100/reference-notes.md`, `paper/revision100/local.py`, `paper/revision100/local.json`; `revision100/calibration.py` and `calibration.json` are complete. Their rare-tail scenario fails severely; the paper reports that failure and does not claim general coverage. Do not present simulated method checks as model measurements or proof of actual-data coverage. |
| R2.4 | Explain the bootstrap Monte Carlo floor. | **Addressed:** report replicate count, exceedance counts, plus-one convention, and the family-size-dependent adjusted resolution for the new four-test local family. Do not copy the old eight-test floor. Evidence: `paper/revision100/local.py`, `paper/revision100/local.json`, `paper/main.tex` inference notes. |
| R2.5 | Holm adjustment is by family, not across all exploration. | **Addressed:** enumerate the new distance, map, and local test families separately, and explicitly exclude earlier analysis selection from the error-control claim. Distance-balanced and leaveout summaries remain descriptive. Evidence: frozen distance/map audits, `paper/revision100/local.json`, `paper/main.tex` methods/limitations. **Requires future data:** preregistered confirmatory primary estimands and analysis families. |

## Review 3 — writing and organization ([issue #2](https://github.com/timini/cognitive-atlas/issues/2))

Source: [review-03-academic-writing.md](../reviews/review-03-academic-writing.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R3.1 | Lead with research rather than storage/infrastructure. | **Addressed:** frame the abstract/introduction around accuracy, coherence, and repeated prompt-condition sensitivity. Move implementation inventory to reproducibility documentation. Evidence: revised `paper/main.tex`, repository `README.md`, `docs/development.md`. |
| R3.2 | Put effect sizes before significance. | **Addressed:** lead abstract, results, and conclusion with the new observed error/displacement magnitudes and interval estimates; use p-values to qualify the specified comparisons. Evidence: `paper/main.tex` and generated 100-capital tables. |
| R3.3 | Give the geometry question an explicit results answer. | **Addressed:** report capital displacement, neighborhood preservation, triangle-excess magnitude, spherical stress, and true-Earth controls; distinguish in-sample approximation from an identified internal geometry. Evidence: `paper/revision100/geometry.json`, `paper/main.tex` geometry results and figures. |
| R3.4 | Update data availability. | **Addressed:** reconcile manuscript, paper guide, downloadable data, and final deployed access. Evidence: the same release/access checks as R1.1. |
| R3.5 | Make switches between median error and single-response error visible. | **Addressed:** name the estimand in every relevant heading/table caption; identify local effects as equal-pair-weight mean single-response absolute errors and global median accuracy as error of pair medians. Evidence: `paper/main.tex`, `paper/revision100/qc.json`, `paper/revision100/local.json`. |
| R3.6 | Reduce repetitive defensive prose. | **Addressed:** consolidate limitations without deleting substantive qualifications; remove storage slogans and development-chat framing. Evidence: revised `paper/main.tex`; final text/PDF read-through remains required. |
| R3.7 | Narrow language/local-advantage wording. | **Revision / requires future data:** use “these translated prompt conditions” and explicit associated-endpoint groups. Do not infer a causal language/cultural effect; replication remains future work. Evidence: `paper/main.tex` abstract/results/conclusion and group documentation. |

## Review 4 — geometric methods ([issue #4](https://github.com/timini/cognitive-atlas/issues/4))

Source: [review-04-geometric-methods.md](../reviews/review-04-geometric-methods.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R4.1 (G1) | Website uses one label for different stress normalizations. | **Addressed in website:** expose the stored stress definition beside each value, or provide a common target-normalized residual separately from optimizer Stress-1. Preserve nonmetric disparity stress as a different quantity. Evidence: `app/page.tsx`, `atlas/analysis.py` exports, frontend tests and final site checks. Do not alter historical stored stress values merely to unify labels. |
| R4.2 (G2) | Website omits stored true-Earth dimensionality reference. | **Addressed in website:** draw the WGS84 reference curve on the same axes with a legend and retain arc-versus-chord interpretation. Evidence: `app/page.tsx`, stored `true_earth_dimensionality`, final frontend verification. |
| R4.3 (G3) | Quantify spherical/ellipsoidal reference mismatch. | **Addressed:** include a 100-capital WGS84-to-sphere reference fit and aligned displacement, and define Procrustes as an extrinsic chord-norm alignment. Do not subtract a mean baseline displacement from every city. Evidence: `paper/revision100/geometry.py`, `paper/revision100/geometry.json`, manuscript geometry methods/results. |
| R4.4 (G4) | Negative cosine eigenmass does not establish rank-three spherical validity. | **Addressed:** report the cosine spectrum, positive mass beyond rank three, tolerance/domain convention, and the distinction between PSD and rank constraints. Evidence: `paper/revision100/geometry.py`, `paper/revision100/geometry.json`, manuscript/supplement diagnostic definitions. |
| R4.5 (G5) | Save per-start optimizer diagnostics. | **Partial / future implementation:** the completed 12-start sensitivity audit records per-start outcomes and comparison with saved fits. Evidence: `paper/revision100/geometry.py`, `paper/revision100/geometry.json`. Preserve the limitation that historical four-start exports retained only the winner; do not claim to recover their unsaved diagnostics. Permanent runner-wide per-start provenance and robustness on future difficult matrices remain implementation work unless separately completed. No finite set of starts proves global optimality. |

## Review 5 — multilingual design ([issue #5](https://github.com/timini/cognitive-atlas/issues/5))

Source: [review-05-multilingual-design.md](../reviews/review-05-multilingual-design.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R5.1 | Language and surface-distance explanation are confounded. | **Revision / requires future data:** document exact English/Arabic/Chinese instructions and the differing disambiguation; summarize target geometry, output restriction, and entity-name policy. Narrow all conclusions to prompt conditions. Crossed independently reviewed phrasings require new collection; historical prompts remain unchanged. Evidence: frozen manifests/prompts, `paper/main.tex` methods and appendix. |
| R5.2 | Specify English entity names and Chinese script/register. | **Addressed:** define the Chinese condition as written standard Chinese in simplified characters, conventionally labeled Mandarin, with canonical English city/country names. This is not a spoken-language test. Evidence: `paper/main.tex` condition definitions/captions, `paper/revision100/reference-notes.md`, exact prompts. |
| R5.3 | Geographic and distance imbalance can explain local interaction. | **Revision / partial:** add observed group distance balance and an explicitly descriptive distance-quintile-standardized sensitivity. It is not causal adjustment for all regional/composition differences. Evidence: `paper/revision100/local.py`, `paper/revision100/local.json` distance-balance fields, manuscript local-results table. A richer regional or distance-matched confirmatory design requires future data. |
| R5.4 | “Local” mainly means one associated endpoint in a global pair. | **Addressed:** call these pairs involving at least one group capital; report exactly-one and both-endpoint counts. Evidence: `paper/revision100/local.json` `one_endpoint`/`both_endpoints`, manuscript group table/captions. Do not describe the pooled estimate as exclusively within-region accuracy. |
| R5.5 | Affinity classification needs a source trail and sensitivity. | **Revision / partial:** use a dated 22-member UN/ITU regional list intersected with the dataset (15 capitals) and an explicitly named Beijing–Singapore case group. Record all IDs, sources, dataset hash, exclusion rationale, and post hoc status. Evidence: `paper/revision100/reference-notes.md`, `paper/revision100/local.py`, `paper/revision100/local.json`, `paper/revision100/groups.json` and the generated group table. Leaveout checks examine membership sensitivity, but an alternate substantive definition is not complete unless separately specified. Do not claim the new rule was fixed before data collection. |
| R5.6 | Show the fragility of the two-city Chinese subgroup alongside its estimate. | **Addressed:** put the two-city count and Beijing/Singapore omission results beside the pooled estimate; report current directions rather than importing the older study's signs. Evidence: `paper/revision100/local.json` leave-one-capital-out results and manuscript local-results discussion. |

## Review 6 — references ([issue #6](https://github.com/timini/cognitive-atlas/issues/6))

Source: [review-06-references.md](../reviews/review-06-references.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R6.1 | Bespoke bootstrap lacks derivation and citation. | **Addressed:** cite a bootstrap reference, derive the empirical-mean variance correction, state the basic-interval inversion and approximate centered-tail procedure, and separate those facts from coverage. Evidence: `paper/revision100/reference-notes.md`, `paper/references.bib`, manuscript/supplement; completed calibration and its diagnosed failure cases are documented under R2.3. |
| R6.2 | Country-language classification lacks full source provenance. | **Addressed:** provide source/date/rule/ID mapping for the new two operational groups, without conflating institutional status with prevalence or exclusive language identity. Evidence: `paper/revision100/reference-notes.md`, `paper/revision100/groups.json` and the generated membership table, `paper/references.bib`. Earlier definitions remain recoverable in Git history. |
| R6.3 | Clarify Karimi's limited multilingual antecedent. | **Addressed:** identify a two-page conference abstract with illustrative English/Persian routing-distance comparisons, not a matched repeated geodesic benchmark. Evidence: source verification in `paper/revision100/reference-notes.md`, related-work paragraph, bibliography. |
| R6.4 | Cite randomized-permutation principle and pin software documentation. | **Addressed:** add Phipson–Smyth for nonzero Monte Carlo p-values after source verification; retain the actual custom stratified algorithm and absolute-statistic tail convention. Cite versioned software documentation where available and record runtime versions separately. Evidence: `paper/references.bib`, manuscript inference methods, final analysis environment/release records. |
| R6.5 | Improve dataset citation identity and proper-name protection. | **Addressed:** separate Natural Earth layer/source and terms-of-use links, distinguish retrieval date from release identity, surface exact dataset/source hashes, and protect proper nouns in BibTeX. Evidence: `data/capitals-100-v3.sources.json`, `paper/revision100/reference-notes.md`, `paper/references.bib`. Do not invent a source release/version absent from recoverable records. |

## Review 7 — computational reproducibility ([issue #7](https://github.com/timini/cognitive-atlas/issues/7))

Source: [review-07-reproducibility.md](../reviews/review-07-reproducibility.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R7.1 | Analysis ID omits some external inputs and runtime. | **Partial:** give the new paper release a frozen input checksum contract including geometry and result artifacts, plus analysis source/settings/runtime records. Supplemental geometry records its environment. Evidence: `paper/input-lock.json` (42 input files at initial freeze), `paper/revision100/geometry.json`, `paper/release-lock.json`. This release-level protection does not retroactively strengthen historical analysis IDs or fix the general application's cache identity; retain that limitation until explicitly changed/tested. |
| R7.2 | Recorded HEAD does not prove the collector bytes executed on each attempt. | **Documented limitation / future implementation:** preserve historical manifests and state the dirty-working-tree/resume source-snapshot gap. Do not certify or reconstruct missing per-session execution provenance from HEAD alone. Evidence: manuscript reproducibility limitations, frozen manifests, `paper/VALIDATION.md`. Future collection should snapshot recoverable source and track/enforce it on resume. New analysis locks do not repair this collection gap. |
| R7.3 | Default paper rebuild re-certifies inputs instead of checking frozen hashes. | **Addressed:** verify the frozen input lock before generation, freeze script/output evidence separately, and make release-lock refresh an explicit operation rather than ordinary rebuild behavior. Evidence: `paper/input-lock.json`, `paper/revision100/verify.py` and `paper/release-lock.json`, revised `paper/Makefile`, `paper/VALIDATION.md`. A failed-tamper test and a clean successful rebuild both passed locally. Earlier releases remain in Git history; the active index contains only three 100-capital exports. |

## Review 8 — sampling and quality control ([issue #8](https://github.com/timini/cognitive-atlas/issues/8))

Source: [review-08-sampling-quality-control.md](../reviews/review-08-sampling-quality-control.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R8.1 | Quantify censoring of readable but impossible distances. | **Addressed:** primary accepted-output results and finite-positive numeric range-retained sensitivities are reported separately, preserving raw strings without clipping. Evidence: `paper/revision100/qc.py`, `paper/revision100/qc.json`, new manuscript QC/error table; local sensitivity in `paper/revision100/local.json`. Completed range-retained reconstruction and structural refits are in `paper/revision100/range_geometry.json`: observed between-condition map displacements change by at most 0.16 km. |
| R8.2 | Complete-case selection discards additional valid answers; test local sensitivity. | **Revision / partial:** report the new flow: 4,948 complete pairs, excluded `AR--VN` and `BE--FR`, and 51 otherwise valid omitted observations. The all-available-pair local effect-size sensitivity is reported; range-retained accuracy and geometry are reported separately in the QC and range-geometry supplements. Evidence: `paper/revision100/qc.json` common exclusions, `paper/revision100/local.json`. No new format adjudication is silently applied. These sensitivity results are descriptive unless their uncertainty is separately recomputed; the review's request for inferential sensitivity is not automatically satisfied by stable signs. Formal uncertainty for the QC sensitivity contrasts has not been recomputed, so that part of the review remains outstanding. |
| R8.3 | QC descriptions cover languages more fully than the original model comparison. | **Superseded scope:** the principal revised experiment is one model and three 100-capital prompt conditions; give each its own attempts/completions/valid/range/format/retry table. Evidence: `paper/revision100/qc.json`, manuscript design/QC. The superseded model comparison is excluded from the current release and remains in Git history; its results are not presented in this paper. |
| R8.4 | Independent requests are not demonstrated independent samples; scheduling is clustered. | **Revision / requires future data:** disclose canonical pair ordering and temporally clustered repeats, distinguish separate single-turn calls from assumed statistical independence, and avoid assertions of actual caching. Evidence: manuscript methods/limitations, frozen response timestamps/runner source. Randomized interleaved blocks and repeated dates require new data. |
| R8.5 | Historical generation was not provider-schema-constrained. | **Addressed:** state explicitly that these 100-capital observations, like the reviewed language study, used prompt-specified numeric formatting and strict whole-response validation, not a provider output schema. Later schema-constrained calls are a distinct condition and cannot relabel these observations. Evidence: frozen 100-capital manifests, `paper/main.tex`, `paper/revision100/qc.json`; future schema implementation is not evidence of historical enforcement. |

## Review 9 — novelty and theoretical framing ([issue #9](https://github.com/timini/cognitive-atlas/issues/9))

Source: [review-09-novelty-framing.md](../reviews/review-09-novelty-framing.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R9.1 | Explain the advance beyond Bhandari instead of listing software features. | **Addressed:** contrast the previous 93-US-city prompted-distance/MDS study with repeated numeric sampling, global spherical fitting, and matched prompt-condition comparisons here. Do not claim MDS priority or compare their coordinate error to this paper's distance MAE. Evidence: `paper/revision100/reference-notes.md`, related-work paragraph, `paper/references.bib`. |
| R9.2 | Bring accuracy versus consistency into the contribution. | **Addressed:** interpret high geographic rank correlation alongside triangle violations and their magnitudes, residual fit, neighborhood preservation, and reference controls. Evidence: `paper/revision100/geometry.json`, revised geometry results. A small violation and a large violation must not be rhetorically treated as equivalent. |
| R9.3 | Tie language claims to observed prompt conditions. | **Revision / requires future data:** use condition-specific wording throughout, retaining the translated-wording confound and strong-null interpretation. Evidence: `paper/main.tex` abstract, results, and conclusion. General language effects need independently varied phrasings/conditions. |
| R9.4 | Distinguish the English–Persian routing antecedent. | **Addressed:** make the target-distance and evidential-scale differences explicit. Evidence: verified source note and related-work paragraph, as R6.3. |
| R9.5 | Position cognitive geometry against behavioral planning evaluations. | **Addressed:** cite CogEval and distinguish a fitted behavioral geometry from a model's use of a map in planning/navigation; retain the separation from activation studies and hidden-representation claims. Evidence: `paper/revision100/reference-notes.md`, `paper/references.bib`, introduction/limitations. |

## Review 10 — conclusions and readiness ([issue #10](https://github.com/timini/cognitive-atlas/issues/10))

Source: [review-10-conclusions-publication.md](../reviews/review-10-conclusions-publication.md).

| ID | Finding | Disposition and evidence |
|---|---|---|
| R10.1 | Conclusion exceeds the tested common-distribution hypothesis. | **Addressed:** narrow both matrix and map significance statements to departures from exchangeability conditional on fixed pairs and independent calls. Distinguish observed shifts from population-median changes and translation effects from language effects. Evidence: revised inference/conclusion, frozen 100-capital distance/map audits. Same substantive response as R2.1; more permutations alone are not a remedy. |
| R10.2 | Reconstruction needs quantitative interpretation and reference comparison. | **Addressed:** report fitted-capital displacements, neighbor preservation, triangle magnitudes, common stress definitions, and WGS84 spherical controls. Identify these as in-sample descriptive reconstructions and finite-start diagnostics. Evidence: `paper/revision100/geometry.json`, main results and figures. |

The same report also lists four numbered publication-readiness requirements. They are tracked separately so they are not confused with its two ranked findings:

| ID | Readiness requirement | Disposition and evidence |
|---|---|---|
| R10.P1 | Correct statistical conclusion and add substantive geometry results. | **Addressed:** see R10.1–R10.2. The final independent agent read and release verifier checked the numerical claims against the cited audits and tables; this is AI-assisted verification, not independent human peer review. |
| R10.P2 | State exact data access and frozen release without mixing historical/new studies. | **Addressed:** explicitly identify the new 100-capital cohort, enforce release locks, and verify public URLs. Evidence: Git history, `paper/input-lock.json`, final release lock/verifier, `paper/README.md`, manuscript availability section. |
| R10.P3 | Named human scientific and independent language review; authorship metadata. | **Requires human review:** the ten agents are AI reviewers and do not satisfy this condition. Do not invent author identities, affiliations, native-speaker validation, journal acceptance, or independent human certification. Evidence: manuscript disclosure and this response. |
| R10.P4 | Repeated dates, randomized blocks, multiple translations, prespecified groups; geographic sensitivity. | **Partial / requires future data:** the new distance-quintile and leaveout analyses respond to sensitivity concerns, but the 100-capital expansion does not provide the missing independent date/wording replication or retrospective preregistration. Evidence: `paper/revision100/local.json`, manuscript future-work section. |

## Verification record

Numerical correspondence, release contracts, local tests, typesetting, and deployed checksums are recorded in `paper/VALIDATION.md`. A successful PDF build alone is not treated as evidence for the scientific claims. Review issues are retained; requests requiring new data or human assessment remain explicit limitations.

## Final correspondence and scope

- The abstract, every numerical results section, all generated tables, and all figures now use only the 100-capital inputs. A final independent agent read checked their numerical correspondence and statistical interpretation.
- Range-retained geometry was additionally computed in `revision100/range_geometry.json`: mean within-condition map changes are 0.90 km (English), 0.055 km (Arabic), and effectively zero (Chinese). No malformed text was repaired and no new significance claim was added.
- `input-lock.json` and `release-lock.json` prevent ordinary paper builds from silently updating their evidence contracts. Historical collector execution state and original cache design cannot be retroactively certified; the paper explicitly states those limits.
- The public atlas now shows the stored WGS84 dimensionality curve and uses distinct labels for target-normalized residuals, metric Stress-1, and non-metric disparity Stress-1.
- Human scientific review, native-speaker validation, randomized collection blocks, repeated collection dates, and population-median-specific inference remain future work. They are not prerequisites that have been silently waived or represented as completed.
- Exclusion and regional sensitivities are descriptive; this revision does not turn post hoc subsets into confirmatory experiments. The calibration exercises are synthetic method checks kept separate from the observed model data.
