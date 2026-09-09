# Academic review 08: sampling, parsing, exclusions, and quality control

**Recommendation:** moderate revisions to reporting and sensitivity analysis. I found no evidence that a parser silently extracted a convenient number, altered an accepted numerical value, or replaced invalid answers until plausible ones appeared. The strongest concern is conditioning analysis on physically plausible output, followed by incomplete reporting of the model-comparison exclusions.

**Scope:** independently inspected the historical 50-capital paper and all eight corresponding response exports in `paper/experiment-index.json`; replayed parsing; counted terminal sample slots, failures and retries; recomputed median-based and single-response MAEs; examined a descriptive exclusion sensitivity. Reviewed paper/code baseline: `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`; collection code recorded in language manifests: `9e09f5f38f841ea9425a665b75fa00d8b20b76ec`. Code line references below refer to the baseline, avoiding simultaneous working-tree changes. The later 100-capital study and new JSON-schema condition are not evidence for the historical paper. No paid model calls were made.

## 1. Moderate: quantify the effect of excluding readable but physically implausible judgments

**Evidence:** `paper/main.tex:54–56` accurately acknowledges the 20,040 km cutoff and optimistic accepted-output accuracy. `atlas/parsing.py:30–34` converts an otherwise readable number and then discards its numerical value from the accepted-analysis stream when it exceeds the cutoff. These are observable judgments relevant to the central coherence question, rather than measurement failures. All eleven language-study range exclusions occur on **Buenos Aires–Hanoi (AR--VN)**: six English, four French, one Arabic. They are not scattered random missing observations. The true distance is 17,861.954 km; excluded estimates range from 20,075 to 20,170 km.

Recomputing the all-pair descriptive metrics while retaining every finite positive, otherwise readable numeric response gives:

| Condition | Published accepted-output median MAE, km | Median MAE with numeric range failures retained, km |
|---|---:|---:|
| Gemini 2.5 Flash-Lite, original English | 937.983 | 940.511 |
| Gemini 3 Flash Preview, original English | 163.223 | 163.223 |
| Gemini 3.5 Flash, original English | 159.045 | 159.045 |
| Matched English | 164.576 | 166.098 |
| Matched French | 157.783 | 158.418 |
| Matched Spanish | 167.396 | 167.396 |
| Matched Arabic | 186.847 | 186.858 |
| Matched Mandarin | 165.241 | 165.241 |

This sensitivity preserves model ordering but reverses the tiny English–Mandarin descriptive ordering: accepted English is about 0.665 km better; uncensored English is about 0.857 km worse. Neither is a new significance result. Pair medians use each pair's available readable samples, then MAE averages equally over all 1,225 pairs. Spanish's two malformed strings remain excluded in this table.

**Requested revision:** retain the prespecified accepted-output analysis, add this uncensored-numeric sensitivity and its exact inclusion rule, and distinguish format failure from a validly expressed impossible estimate. Also report how reconstruction and structural-coherence results respond to retaining those estimates; an impossible distance is directly relevant to coherence. Do not clip outliers to the cutoff or silently change historical exports.

## 2. Moderate: complete-case analysis deletes 87 acceptable observations beyond the 13 invalid outputs; show a sensitivity for the primary local claim

**Evidence:** `paper/main.tex:56` reports 61,237 valid outputs but only 61,150 used inferentially, hence **87 valid observations** are additionally omitted when both affected pairs are removed in every language. The two Spanish format failures are literally `6601` followed by a backtick, on **Seoul–Moscow (KR--RU)**, samples 1 and 6. The common exclusion set is correctly applied across languages, but it conditions the benchmark on outcomes from all five conditions. Buenos Aires is also in the Spanish-associated group, so the exclusion is pertinent to the local-language result, not merely the overall MAE.

As an explicitly post hoc descriptive check, retaining all numeric range failures and adjudicating those two exact trailing-backtick strings as 6601 gives **Spanish home gain 18.870 km and interaction 26.027 km** over all 1,225 pairs (279 home pairs), compared with the paper's approximately 17.358 and 24.523 km on the complete-case set. This check does **not** overturn the direction of the result, and I did **not** recalculate its confidence intervals or p-values. It is a sensitivity scenario, not authorization to repair raw observations.

**Requested revision:** add the complete-case flow count and a transparent sensitivity appendix: range failures retained; format failures separately handled through a documented adjudication or bounds scenario. Report effect sizes and rerun inferential uncertainty under clearly stated assumptions. Keep strict-parser primary results and original raw text unchanged. This would provide evidence for robustness instead of relying only on a qualitative caveat.

## 3. Minor: quality-control prose describes the language study much more fully than the three-model comparison

**Evidence:** `paper/main.tex:45` introduces three conditions, but `54–56` provides detailed exclusions only for the later language experiment. The three-model table reports valid counts without equally explicit failure categories. The raw model-comparison exports show:

| Model condition | Terminal sample slots | Valid estimates | Range failures | Retried transport/server attempts |
|---|---:|---:|---:|---:|
| 2.5 Flash-Lite | 12,250 | 12,241 | 9 | 0 |
| 3 Flash Preview | 12,250 | 12,250 | 0 | 1 HTTP 503 |
| 3.5 Flash | 12,250 | 12,250 | 0 | 2 HTTP 503 |

The nine 2.5 Flash-Lite range failures occur across eight pairs: AU--PE, CL--MY, CL--TZ, CO--NZ, IN--PE (twice), KE--PE, MY--PE, NZ--PE. Its single-response MAE rises from 1,027.467 to 1,031.650 km when those numeric judgments are included. The headline model difference is much larger than this change.

**Requested revision:** add a compact per-condition sampling/QC table covering both experiments, stating that original model comparisons used the legacy numeric parser and the matched-language study used `ascii_decimal_v2`. Include attempts, completed slots, accepted answers, range failures, format failures and retries. Do not imply every paper condition used identical format constraints.

## 4. Minor: separate “independent requests” from empirically established independent samples, and describe clustered scheduling

**Evidence:** `atlas/runner.py:104–114` enqueues all ten sample slots for one pair consecutively before moving to the next pair, in canonical pair order. The language manifests explicitly record `independent_single_turn_unordered_pairs_fixed_id_order`. For example, the ten English AR--VN dispatch timestamps lie within approximately 2.4 seconds. `paper/main.tex:45` correctly calls them separate single-turn requests; `190` already notes unverified provider dependence and one run per condition. That caveat is good, but readers should know the replicates were temporally clustered within pairs rather than dispersed across the collection window.

**Requested revision:** state the scheduling pattern in Methods. In a confirmatory replication, randomize/interleave pair, sample and language dispatch within recorded blocks, and collect independent date blocks. Do not claim evidence of actual caching or dependence from this schedule alone; neither can be established from the saved outputs. The current conditional inference can remain if its independence assumption stays explicit.

## 5. Minor: say explicitly that historical generation was not constrained by a provider output schema

**Evidence:** historical `atlas/providers.py:39–54` constructs generation configuration without `responseMimeType` or `responseJsonSchema`; frozen manifests contain no schema parameter. The historical v2 parser (`atlas/parsing.py:14–18`) requires a **whole-response** ASCII decimal match after stripping whitespace. It rejects prose, separators, exponent notation and stray punctuation; it does not search prose for a usable estimate. Its call into the legacy parser cannot reinterpret commas because commas have already been rejected. I replayed every completed STOP response in all eight 50-capital exports and found **zero quality-label or accepted-value mismatches**.

**Requested revision:** describe this as prompt-specified formatting followed by strict whole-response validation, not schema-constrained generation. If future experiments use JSON schema, label them as a new output-format condition and collect a new matched baseline; constrained generation can change responses. A schema would prevent some format failures but would not itself validate geographical correctness. The new working-tree schema implementation does not retroactively change this review's historical finding.

## Verified strengths

- The five language files contain exactly **61,250 unique terminal sample slots**, **61,237 accepted answers**, **13 terminal invalid answers**, and **one additional nonterminal timeout attempt**. No duplicate terminal slots were found. The three original model files likewise have exactly 12,250 unique terminal slots each.
- The timeout in French ET--PE sample 7 was retried. Invalid model content was terminal. Runner code at `atlas/runner.py:142–154` agrees with the documented policy; there is no accept-until-plausible retry selection in these data.
- Raw invalid output and successful provider payloads are preserved, enabling the sensitivity checks above.
- Paper counts, the two-pair common exclusion set, strict ASCII rule and accepted-output metrics match the data. The purposive sample, mutable model alias, unchanged English entity names, small repeated sample size and conditional scope are acknowledged.
- No Gaussian distribution is assumed by the numerical-format validator. Identical answers do not by themselves show caching, and the paper correctly avoids learning a response-distribution shape from ten samples.

## Reproduction and review limits

For each indexed 50-capital export I read `responses.csv`, grouped terminal rows by `(pair_id, sample_number)`, counted `quality`, and replayed the manifest-selected parser against every STOP response. For the table above I grouped accepted values by pair, recomputed the median and its absolute error against `pairs.csv`, then repeated with all finite positive raw numeric values, including those rejected only for range. No inference p-values, uncertainty intervals, geometry refits, or paid API queries were run for these sensitivity checks. The separate two-backtick adjudication was used only for the explicitly labeled local-effect sensitivity.

This review establishes auditable handling of the saved observations. It cannot verify provider-side sampling independence, hidden routing, unrecorded failed remote completions, or representativeness of this purposively selected capital set. It does not conclude that the reported Spanish effect is an artifact; the simple sensitivity tested here preserves it.
