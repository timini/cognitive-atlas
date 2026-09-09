# Reviewer 02 — statistical inference

**Scope:** the frozen 50-capital paper, its global permutation tests, local-language bootstrap, multiple testing, and inferential conclusions. Reviewed 9 September 2026 against repository HEAD `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`. Later 100-capital analyses and map-inference extensions are not evidence for this manuscript. Implementation and data were read only; no model requests were made.

**Recommendation:** revise inferential wording and add sensitivity/validation evidence before academic submission. I found no arithmetic defect in the reported local contrasts, their analytic standard errors, the permutation splits, or the Holm algorithm. The statistical limitations are unusually explicit in the methods. The principal issue is keeping the conclusion as narrow as the null actually tested.

## 1. Moderate — a distributional rejection does not establish a changed population median map

**Evidence:** `paper/main.tex:88–95` correctly defines a strong common-response-distribution null. `paper/scripts/check_language_differences.py:103–133` pools all twenty answers within each pair and permutes their labels. However, the conclusion at `paper/main.tex:204` says that all instruction languages “change the distance matrix detectably.” The abstract is more careful: it describes observed median-distance disagreement relative to a permutation baseline.

The test can reject because response dispersions differ even when the population medians, and hence the population median-distance matrices, agree exactly. The paper explicitly recognizes the corresponding strong-null limitation for MAE at line 95, but does not spell it out for its principal median-matrix result.

**Independent diagnostic:** I used the existing generic permutation routine with 1,223 artificial pairs solely to check the interpretation of the test. Language A always returned 1,000; language B returned 900, 1,000, or 1,100 with probabilities 0.25, 0.50, and 0.25. Both have the unique population median 1,000. With ten draws per pair, data seed 417, permutation seed 21, and 999 permutations, the test returned disagreement 10.9567, shuffled mean 0.6775, and `judgment_p=0.001`. This is a valid rejection of the common-distribution null, not evidence of different population medians. These simulated values are a method counterexample and are not experimental LLM measurements.

**Correction:** replace the conclusion with wording such as “all ten comparisons depart from a common response-distribution baseline, as measured by disagreement between the sampled median matrices.” Add one sentence noting that dispersion changes can contribute to this rejection. To claim a stable change in central geographic judgments, add independent repeated batches, report dispersion separately, and specify an estimand/test targeting the central relationship matrix. Do not relabel the current test as a test of equal medians.

The distinction agrees with the null documented for independent-sample permutation tests in the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html).

## 2. Moderate design limitation — request-level uncertainty is not independently replicated language-condition uncertainty

**Evidence:** `paper/main.tex:47,51,190` acknowledges one unvalidated translation, one collection period, concurrent rather than randomized scheduling, a mutable model alias, and assumed request independence. `atlas/runner.py:104–114` queues all repeats for one pair consecutively before moving to the next. `paper/scripts/check_language_differences.py:112–115` and `paper/scripts/local_language.py:93–98` independently exchange/resample observations by pair and language.

These methods are coherent under the stated independence model. Shared capital endpoints alone do **not** invalidate a fixed-pair, independent-request analysis. Nevertheless, provider time effects, caching, or other common request-level disturbances could create dependence or condition differences the saved design cannot separate from language. The current result is conditional rather than a replicated demonstration of a general language effect. This is already a limitation in the manuscript, not an undisclosed statistical coding error.

**Correction:** keep this qualification in the abstract/conclusion whenever summarizing significance. For the next confirmatory collection, randomize language order within independently repeated time blocks and repeat across dates and translations. Save the assigned block identifiers, not only timestamps. Analyze variation across those independently replicated conditions. On current data, add a descriptive timestamp/order sensitivity check; do not present a post hoc block bootstrap as a substitute for missing replication.

## 3. Moderate validation gap — matching bootstrap variance is not a coverage or type-I-error validation

**Evidence:** `paper/scripts/local_language.py:44–51,93–102` forms a basic bootstrap interval and an approximate two-sided test from centered, variance-corrected deviations. The manuscript accurately calls the p-values approximate at `paper/main.tex:117`. The `sqrt(10/9)` correction matches the unbiased independent-sample variance for this linear contrast. The analytic variance assertion verifies the resampling implementation's variance; it does not verify interval coverage or p-value calibration for the actual finite-sample distributions.

The chosen mean absolute-error estimand is substantially easier to bootstrap than a heavily tied median. Aggregation over many independent pairs also helps. Still, ten observations per pair cannot reveal unseen rare response modes, and a pair with identical observed answers contributes zero empirical variance. No finite-sample null/coverage calibration is included for the complete procedure, including selection of complete pairs and Holm correction.

**Correction:** add a small statistical-method validation suite using known synthetic distributions: rounded/tied outputs, skewed rare errors, heterogeneous pair variances, and genuinely zero-variance strata. Clearly separate method-validation simulations from experimental observations. Report interval coverage and familywise rejection frequency under the corresponding null. Retain the current wording “approximate” and “pointwise”; do not describe the variance assertion as validating inferential coverage. A larger independent repeat batch on a prespecified subset would provide a useful empirical sensitivity check.

## 4. Minor — the bootstrap's Monte Carlo floor should be explained as explicitly as the permutation floor

**Evidence:** `paper/main.tex:153` explains why all adjusted disagreement p-values equal 0.004. The abstract and local results at lines 26 and 163 report adjusted bootstrap `p=0.0008` without the corresponding explanation. With 9,999 draws, `paper/scripts/local_language.py:49–50` has a raw minimum of 0.0001; Holm over eight tests yields the reported 0.0008 for the strongest results. Several substantially different effects therefore share that reported value.

**Correction:** add the raw exceedance counts and number of replicates to the local audit, and state that these are Monte Carlo estimates at the current resolution. Do not imply that 0.0008 is an exact underlying probability or that equal adjusted p-values indicate equal strength/effect size. Increasing replicates is optional; effect estimates and intervals deserve more emphasis than extra p-value digits.

## 5. Minor — state explicitly that multiplicity control is by analysis family, not for the entire exploratory research process

**Evidence:** `paper/scripts/check_language_differences.py:140–144` correctly applies Holm to twenty global tests; `paper/scripts/local_language.py:135–138` correctly applies Holm to eight local tests. `paper/main.tex:36,107` says that local hypotheses followed inspection of global results, which is appropriately transparent.

Separate scientific families can be defensible, particularly in an exploratory report. Their corrections do not establish study-wide error control over all earlier inspection, choice of language-affinity definitions, aggregation methods, model comparisons, and later follow-ups.

**Correction:** add a single sentence saying that Holm control applies separately to the two stated families and does not account for the preceding exploratory selection process. A future confirmatory protocol should fix its primary estimands, groups, families, and analysis decisions before collection. Do not retroactively call the existing tests preregistered or confirmatory.

## Independent numerical checks and sound features

I independently loaded the frozen source exports, recreated the 1,223 common complete pairs, computed absolute response errors, formed the home/other/interaction weights, and recomputed analytic standard errors. All four languages matched the saved local audit.

| Language | Home gain, km | Interaction, km | Home analytic SE, km | Interaction analytic SE, km |
|---|---:|---:|---:|---:|
| French | -5.000842 | -11.027976 | 3.837028 | 4.149352 |
| Spanish | +17.358247 | +24.522612 | 3.974836 | 4.274642 |
| Arabic | -22.696178 | +0.280602 | 3.097172 | 3.579309 |
| Mandarin | -10.536281 | -6.342536 | 3.941907 | 4.271044 |

A normal approximation used only as a sensitivity calculation gave the same substantive pattern: Spanish positive home and interaction contrasts; Arabic negative home contrast and negligible interaction; French negative interaction; Mandarin negative home contrast. This check does not establish Gaussian raw responses and is not a replacement for the recorded bootstrap.

Other sound choices:

- The common complete-pair rule is shared across all five languages; the manuscript discloses both excluded pairs and the accepted-output selection limitation (`main.tex:54–56`).
- Replicate numbers are not falsely treated as matched observations across languages.
- The permutation implementation preserves ten observations per group and the pooled observations exactly; its plus-one tail calculation avoids zero Monte Carlo p-values.
- Holm adjustment uses the correct monotone step-down formula and does not require independence between tests.
- The paper clearly distinguishes mean single-response absolute error from error of the median, and distinguishes an absolute local gain from a home-versus-other interaction.
- The local bootstrap uses independent within-language draws, the appropriate linear contrast weights, and an independently derived variance check.
- Pointwise confidence intervals, descriptive leave-one-capital-out ranges, and conditional p-values are not conflated.
- No statistically significant test of whole-map shape is claimed in this frozen paper (`main.tex:190`). Later `atlas/map_inference.py` output must remain a separately identified extension unless the paper is explicitly revised with its methods and results.

**Checks not claimed:** I did not rerun all 49,990 original global permutations or all 39,996 local bootstrap replicates, collect any model outputs, validate native-language translations, or prove provider-side independence. The review inspected the saved numerical audits and performed the independent contrast/variance calculations and explicit equal-median diagnostic above.
