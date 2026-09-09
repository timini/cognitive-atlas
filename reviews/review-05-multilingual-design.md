# Review 5: Multilingual design and local-language interpretation

**Recommendation:** Revise the framing and add targeted descriptive checks before treating the multilingual results as a research conclusion about languages. The saved results support differences among these particular prompt conditions. They do not isolate an effect of language independent of wording, spelling, or geographic composition. The manuscript already acknowledges many of these limitations unusually explicitly; the recommendations below concern making those qualifications operative in the results and abstract.

**Scope and limits:** I inspected `paper/main.tex`, all five frozen prompts in `paper/results/exact-language-prompts.json`, `atlas/languages.py`, `paper/scripts/local_language.py`, the frozen local-analysis source files and hashes, dataset selection code, and the language-affinity references. I independently recomputed the local point estimates and several descriptive subgroup quantities from the saved observations. I did not rerun the bootstrap or global permutation tests, make model calls, or perform native-speaker validation. My translation assessment is a textual/semantic review by an AI reviewer, not evidence of independent human linguistic validation. This review concerns the historical 50-capital formatted-number protocol, not subsequent structured-output or 100-capital conditions.

## Findings

### 1. High importance for interpretation: language and explanatory wording are not separately identified

**Evidence:** `atlas/languages.py:6–10`; frozen exact prompts at `paper/results/exact-language-prompts.json:2–6`; manuscript `paper/main.tex:47`, `:186`, and `:204`.

English requests a “straight-line great-circle distance”; French combines “à vol d’oiseau” with a great circle. Spanish and Chinese explicitly define the target as the shortest distance along Earth's surface. Arabic likewise explicitly requests the shortest surface distance along a great circle. All target a defensible surface-distance concept, but the information supplied to the model is not identical: explanatory disambiguation is part of three conditions. This matters especially because straight-line wording can otherwise evoke a chord rather than an arc. The manuscript correctly admits the confound, but its compact conclusion that instruction languages change the matrix can still be read as an isolated language effect.

**Concrete change:** In the abstract and conclusion use “the five translated prompt conditions” and describe the result as prompt-condition sensitivity. Expand the Methods example to include Arabic, and add a compact prompt-equivalence table recording target geometry, surface-distance explanation, output restriction, and entity-name policy. A confirmatory experiment should cross language with independently reviewed equivalent phrasings; a post hoc rewrite cannot repair the existing intervention and must not replace the historical prompts.

**Severity:** Major limitation for a language-specific or causal claim; not a demonstrated failure of the numerical analysis. The existing exploratory qualification makes the narrower result defensible.

### 2. Medium: English entity names and Chinese variety need more precise labeling

**Evidence:** `atlas/languages.py:2`, `:10–13`; `paper/main.tex:47–49`, `:104`, `:186`, `:194`.

The Chinese prompt is written in simplified Chinese characters. A written API prompt does not test spoken Mandarin, and the language label alone does not document script/register. Across all non-English conditions the place names remain canonical English, so the input is deliberately mixed-language. This is a useful controlled design, but it excludes the potentially important effect of recognizable local spellings and should be visible wherever a reader sees a short “Arabic” or “Mandarin” label.

**Concrete change:** Define `zh` once as “written Chinese, simplified characters (Mandarin-oriented standard wording)” or a comparably precise convention, while preserving exact bytes. Add “instruction language; English place names” to language-result captions. Keep localized-name replication separate and factorial, as already proposed at `paper/main.tex:194`.

**Severity:** Reporting precision and construct validity; no claim here that the Chinese text is mistranslated.

### 3. Medium: geographic composition is a quantitatively large alternative explanation for the local interaction

**Evidence:** Local group definitions at `paper/main.tex:98–107`; interaction at `:109–115`; acknowledged confounding at `:188`; implementation at `paper/scripts/local_language.py:18–23`, `:83–87`; purposive sample at `scripts/expand_capitals.py:9–16`, `:51–52`.

Independent recomputation from the frozen 1,223 complete pairs gives a median ground-truth distance of **10,879.5 km** for Spanish-associated pairs versus **6,920.3 km** for other pairs. Arabic-associated pairs have median distance **5,329.2 km**, versus **8,224.6 km** elsewhere. The interaction compares groups with substantially different distance distributions. Its subtraction removes an overall average difference; it does not standardize for distance. The observed Spanish gain could therefore coexist with a distance-dependent prompt effect rather than a language-affinity effect. This is not evidence that the gain disappears after adjustment; no such analysis was performed in this review.

**Concrete change:** Add a descriptive balance table for distance and region, then report a clearly exploratory distance-stratified or distance-standardized sensitivity analysis. Retain the current unadjusted estimand as the original analysis, document any new specification, and avoid causal interpretation if the effect persists. In the abstract call it a gain “on the prespecified operational subset of this benchmark,” not improved local geographic knowledge.

**Severity:** Material limitation of interpreting the interaction as localization. Already mentioned in the limitations, but the measured imbalance warrants a result-level check rather than only a generic caveat.

### 4. Medium: “local” overwhelmingly means a global pair with one associated endpoint

**Evidence:** `paper/main.tex:98`, `:163–165`; `paper/scripts/local_language.py:84` uses `any(axis=1)`.

Independent counts show that only **15 of 278** Spanish-associated pairs have both endpoints in the six-country group; **263** have exactly one. The corresponding both/one endpoint counts are French **6/184**, Arabic **6/184**, and Chinese **1/96**. Thus the analysis primarily measures global distance judgments involving an associated capital, rather than distances within a language-associated region. The formal definition is correct, but “local-language advantage” is liable to suggest a stronger geographic localization than the estimator provides.

**Concrete change:** Prefer “associated-endpoint advantage” or spell out “pairs involving at least one associated capital” in the abstract/results. Add the both/one endpoint counts. As a descriptive sensitivity, the Spanish gains are **20.21 km** for both-associated pairs and **17.20 km** for exactly-one-associated pairs, compared with the pooled **17.36 km**. These are small, unequal subsets, not independent confirmatory tests.

**Severity:** Interpretation and presentation; the implementation agrees with the stated formal definition.

### 5. Medium: the affinity classification needs a reproducible evidence table and alternate-definition sensitivity

**Evidence:** `paper/main.tex:101–107`; `paper/scripts/local_language.py:18–23`, `:81`; references `paper/references.bib:39–49`.

The operational rule mixes official/co-official national status with majority Spanish use. It is explicit and not inherently invalid, but it applies different kinds of association across languages. Ottawa and Singapore also belong to English-speaking institutional contexts, while French excludes Algeria and Morocco under the legal-status rule. These choices make “local versus English” heterogeneous across groups. The conclusion should remain about the listed endpoints, not a homogeneous class of native-language capitals.

I checked the cited [Instituto Cervantes report](https://cvc.cervantes.es/Lengua/anuario/anuario_24/moreno-alvarez/p02.htm), which explicitly distinguishes legal status from prevalent use and multilingual competence. That source supports the need for the distinction; it does not independently validate every group's membership or the timestamp of the claimed pre-analysis choice. The cited Singapore statute could not be retrieved by the web tool (HTTP 403), so I do not claim fresh legal verification of Article 153A. The saved analysis states that groups were fixed before local inspection; that chronology is a provenance assertion, not something established by the numerical outputs alone.

**Concrete change:** Add one source/date/rationale row per included country and relevant excluded case. Keep the original grouping frozen; add an explicitly exploratory alternate grouping only if it answers a specified robustness question. Document the dated artifact establishing when the operational rule was fixed, or soften the chronology to what the records can substantiate.

**Severity:** Reproducibility and external-validity concern; no specific membership error established.

### 6. Low: make the limits of the Chinese subgroup visible alongside its estimate

**Evidence:** `paper/main.tex:104`, `:165`, `:183`, `:233`; saved omission results in `paper/results/local-language-audit.json`.

The Chinese-associated group has only Beijing and Singapore. The overall **−10.54 km** gain becomes **+4.43 km** when Beijing is removed, and **−25.76 km** when Singapore is removed. This heterogeneity is already correctly reported later in the manuscript, but a reader of the principal local-results table sees a single significant associated-pair deterioration without the instability immediately beside it.

**Concrete change:** Put “2 capitals; opposite city-level directions” in the relevant table note or nearby sentence, and do not summarize this as poorer Chinese knowledge of Chinese-speaking geography. The manuscript's statement that no general local-language rule is established is appropriate and should remain.

**Severity:** Presentation; existing qualification substantially addresses the problem.

## Verification record

- The frozen five prompts exactly equal the historical `PROMPTS` dictionary in `atlas/languages.py` at review time.
- Every frozen local-analysis `result.json` source matched its recorded SHA-256 before recomputation.
- Recomputed associated-pair gains match the saved results: French **−5.00084 km**, Spanish **+17.35825 km**, Arabic **−22.69618 km**, Chinese **−10.53628 km**.
- Recomputed Spanish other-pair gain **−7.16436 km** implies the reported interaction **+24.52261 km**. The reported 7.0% improvement is consistent with the stated English single-response error baseline.
- Pair masks and exclusions agree with the implementation and give the manuscript's French/Spanish/Arabic/Chinese counts **190/278/190/97**.
- I verified point estimates, masks, prompts, and source integrity. I did **not** independently validate the reported permutation/bootstrapped p-values in this scoped review.

## Strengths to retain

The new English baseline correctly shares the numeric-format protocol with the translated conditions. Exact Unicode prompts are preserved. The paper explicitly states that only instructions were translated, that translations lack independent native-speaker validation, and that local analysis was exploratory. It distinguishes mean single-response error from median-matrix error, rejects causal cultural explanations, describes complete-case exclusions, and reports capital omission sensitivity. These safeguards support a publishable narrow claim about this fixed collection of prompt conditions, provided they remain prominent rather than being lost in broad “language-specific cognitive map” language.
