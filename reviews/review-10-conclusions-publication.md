# Academic review 10: conclusions, limitations, and publication readiness

**Recommendation: major revision before journal submission; retain as an explicitly exploratory research draft.** The observations and much of the cautious interpretation are useful. The principal correction is to align the concluding statistical claim with the null hypothesis actually tested. A second revision should make the reconstruction results quantitatively assessable. Neither requires discarding the historical observations or silently replacing them with later experiments.

Reviewed independently on 9 September 2026, without reading the other reviewers' reports. Scope: the entire `paper/main.tex`, its generated result tables, global and local inference implementations, and selected frozen numerical exports. Source checkout: `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`; manuscript SHA-256: `5f48fffc573f56005f8074bdb7e73514e3fc1671575de2be6b379b3622eb7fa4`. Line references below refer to that manuscript. This is an automated academic review, not independent human peer review.

## Ranked findings

### 1. Major: the concluding claim about changed distance matrices is stronger than the tested hypothesis

**Evidence.** Methods lines 89–95 correctly define a strong null: the entire distributions of answers are exchangeable between conditions within each pair. The implementation pools twenty observations, splits them into groups of ten, and recomputes median disagreement (`paper/scripts/check_language_differences.py:103–133`). Yet the conclusion at line 204 says that “all instruction languages change the distance matrix detectably.” Results line 153 moves from rejection of the shuffled-label baseline to “Languages can change the pattern of mistakes.” The second claim can describe the observed samples, but the concluding wording invites an inference about different underlying median-distance matrices or a language effect isolated from prompt wording.

**Why this matters.** The statistic depends on both location and the sampling behavior of the median. Equal population medians with different response dispersions can reject this strong null. A rejection is valid evidence against exchangeability; it is not, by itself, a test that the population median matrix changes. Nor does this design separate language from the particular translation, as the manuscript itself correctly states at lines 47 and 186.

**Independent diagnostic.** I reproduced the same pooling-and-splitting logic using deliberately constructed data, not model measurements: condition A always returns 100; condition B returns 50, 100, or 150 with probabilities 0.49, 0.02, and 0.49. Both distributions have the same unique population median, 100. With 1,223 pairs, ten draws per condition, seed 10, and 999 permutations, observed median disagreement was 36.94, the shuffled mean was 6.66, and the upper-tail Monte Carlo p-value was 0.001. This demonstrates the logical distinction; it does not show that dispersion explains the real language results.

**Required revision.** Use a conclusion such as: “For every comparison of the five prompt conditions, observed median-distance disagreement exceeded a within-pair permutation baseline under a common-response-distribution null. This establishes conditional distributional differences, but does not isolate changes in population medians from changes in response dispersion.” Describe observed matrices and their differences separately. If a population-median-map claim is retained, define that estimand and provide a procedure justified for unequal response distributions and the strong ties present here. Simply running more permutations of the current statistic does not solve this problem.

### 2. Moderate: the central reconstruction contribution needs quantitative interpretation, not only recognizable maps and stress tables

**Evidence.** The introduction distinguishes accuracy from geometric compatibility and asks whether the answers admit a useful reconstruction (lines 30–36). Methods promise neighbor preservation, geometric diagnostics, multiple embeddings, and alignment (lines 66–83). The results primarily establish high distance correlations, show spherical stress, display maps, and report a dimensionality figure (lines 123–158). Table 2 reports triangle violation rates around 10%, but the text does not explain their magnitudes or how low stress coexists with these violations. There is no numerical reference-fit comparison or reported capital displacement in the manuscript results.

**Why this matters.** A reader cannot assess “useful reconstruction” from recognizability alone. Correlation across global distances is an accuracy summary; it does not quantify whether regional neighborhoods survive or how far fitted capitals move. A nonzero spherical residual also has a reference floor because the target distances are ellipsoidal. The manuscript acknowledges that issue at line 83, but does not quantify it in the presented results.

**Checked evidence.** The frozen matched-English export `public/data/d6bebef0249ad510ccd3d650-6b21e1546415d329/result.json` already contains:

| Quantity | Value |
|---|---:|
| Spherical stress | 0.0260530 |
| Mean aligned capital displacement | 113.04 km |
| Three-neighbor preservation | 0.9667 |
| Triangle violation rate | 10.0459% |
| Largest triangle excess | 2,120 km |

The stored mean triangle excess is 30.9168 km **over all triples**, not only violated triples (`atlas/statistics.py:35–40`). As a separate reference-control calculation, I fitted the same 50-capital WGS84 distance matrix using `atlas.reconstruct.spherical`, seed 42, and four starts. It converged with stress 0.000371066 and mean aligned displacement 9.69 km. This is a calculation on geographic ground truth, not an additional LLM experiment. Its script version should be pinned if adopted into the manuscript.

**Required revision.** Add a compact reconstruction-results paragraph/table giving comparable reference and judgment fits, capital displacement, and neighborhood preservation. Explain violation magnitudes alongside their rates. State explicitly that these are in-sample descriptive fits and that good global fit does not establish uniqueness, out-of-sample performance, or a discovered neural representation. Those qualifications are already largely present in the limitations; the missing element is substantive interpretation of the available results. Claims comparing different algorithms should remain absent unless corresponding outcomes are actually reported.

## Broad-claim assessment

| Claim | Assessment |
|---|---|
| Responses contain geographic signal rather than behaving like random city relabelings (line 123) | Supported for the specified baseline. The paragraph correctly avoids treating this as a distributional normality test or a definitive model ranking. |
| Repeated answers are not appropriately treated as unrounded continuous Gaussian draws (line 133) | Defensible with the explicit “unrounded” qualification. Rounded or discretized latent distributions remain possible; the paper does not claim to have excluded them. |
| Every language comparison exceeds the specified permutation disagreement baseline (lines 26, 153) | Consistent with the saved table and the implemented test. Interpretation must remain about that strong null; see finding 1. |
| Similar aggregate accuracy can coexist with different observed pairwise estimates (line 153) | Supported descriptively. Similar MAE is not equivalence of underlying accuracy, and no equivalence test is claimed. |
| Spanish shows an exploratory associated-pair advantage in this collection (lines 163, 183) | Supported by the reported estimand and tables. The local script computes mean single-response absolute error and an associated-minus-other interaction, rather than silently substituting median error. |
| A general local-language advantage is unsupported (lines 165, 204) | An appropriately restrained conclusion. It should not be changed into evidence that such an advantage never exists. |
| The experiment reveals hidden neural maps or cultural mechanisms | Correctly rejected at lines 26, 34, 186, and 188. The title is acceptable with the existing behavioral framing. |
| Whole reconstructed maps have been compared inferentially | The historical manuscript explicitly says they have not (line 190). Later website/map audits and the 100-capital extension are separate evidence and should not be retroactively attributed to this paper. |

## Strengths that should survive revision

- The distinction between repeated-call uncertainty and uncertainty across cities, prompts, or dates is explicit. Shared endpoints are not incorrectly presented as independently sampled countries (lines 119 and 190).
- The local analysis is disclosed as post hoc; the manuscript reports adverse and null results, distinguishes absolute gain from interaction, and supplies capital-omission sensitivity checks.
- Language/translation confounding, English entity names, mutable model aliases, unequal thinking settings, and unverified provider independence are all acknowledged directly.
- Excluded outputs remain recorded. The paper states that upper-bound censoring can make accepted-answer accuracy optimistic, rather than claiming that a parser eliminates scientific uncertainty.
- It does not claim that additional Euclidean dimensions prove semantic distortion, that four starts establish a global optimum, or that interpolated coastlines are directly elicited beliefs.

## Publication-readiness requirements and extensions

1. Correct finding 1 and supply the substantive geometry results in finding 2. The exploratory paper can be improved without another paid collection.
2. At submission, state the exact data-access arrangements and frozen release being reviewed. Line 201 describes an access-controlled atlas; the availability section and `paper/README.md` should be reconciled with the actual release status at that time. Do not silently make a historical manuscript appear to contain later 100-capital or structured-output experiments.
3. Obtain named human scientific review and independent language review before submission. The manuscript already discloses their absence; this is a readiness condition, not evidence of a numerical error. Authorship and affiliations also remain unassigned.
4. Treat repeated dates, randomized collection blocks, several translations per language, and prespecified language-affinity definitions as the next confirmatory study, as proposed at line 194. The present conditional p-values cannot substitute for that replication. Distance-range or regional sensitivity analyses would help assess the Spanish interaction, but their absence does not make the explicitly conditional descriptive result false.

## Review limits

I read the full manuscript and checked the inference logic and selected saved numerical outputs. I did not independently regenerate every table, verify every bibliographic source, inspect the compiled PDF layout, or test provider-side independence. I made no model calls and changed no research source or data. The only constructed observations were the clearly labeled statistical diagnostic above; they are not research measurements and must not be added to the experiment dataset. The recommendation reflects interpretation and reporting readiness, not a finding that the collected LLM responses are fabricated or the overall project is invalid.
