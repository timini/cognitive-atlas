# Academic review 09: novelty, related work, and theoretical framing

Reviewed on 9 September 2026 by independent review agent `review_09_novelty`. This review concerns the historical 50-capital manuscript, not the later 100-capital extension. No other review reports were read before forming these findings. No manuscript, analysis, or data files were changed.

Snapshot: `paper/main.tex` SHA-256 `5f48fffc573f56005f8074bdb7e73514e3fc1671575de2be6b379b3622eb7fa4`; `paper/references.bib` SHA-256 `23794082e3e32a3f7b289a02156335ca61274588dbaba90c41a0027c620aabc2`.

## Overall assessment

The defensible contribution is a repeated-sampling geographic benchmark with matched multilingual conditions and separate measures of accuracy and consistency. The manuscript appropriately avoids claiming that prompted MDS is new or that observable answers reveal hidden neural representations. However, its contribution is presented mainly as an inventory of software capabilities. The closest prior experiment deserves a precise comparison, and the results should more clearly explain what repeated sampling and geometric diagnostics establish beyond familiar evidence that language models know many geographic facts.

Recommendation: revise the scientific positioning before submission. These findings do not establish fabricated results or invalidate the recorded measurements.

## Findings, ranked by importance

### 1. Moderate — Explain the experimental advance over the closest prior study, rather than listing implementation features

**Location:** `paper/main.tex:26`, `paper/main.tex:32`; `paper/references.bib:5`.

The introduction's acknowledgement of earlier prompted MDS is correct, but too compressed to make the incremental contribution assessable. Bhandari et al., §6, explicitly obtained numerical city-pair distances, used two-dimensional MDS and alignment, and compared with true-distance, random, and co-occurrence controls. Their experiment used 93 contiguous-US cities and beam-search decoding. It is therefore a close antecedent to the core reconstruction, rather than merely general geospatial background. [Primary paper, §6](https://arxiv.org/pdf/2310.13002).

The current abstract leads with a “file-based experimental pipeline,” and the introduction lists auditable implementation, multilingual protocols, and spherical reconstruction without saying which additional scientific questions these changes resolve.

**Suggested fix:** add a concise comparison distinguishing the prior regional reconstruction from the present global sphere, deterministic decoding from repeated stochastic responses, and geographic accuracy from conditional language contrasts. State the principal contribution as estimation and comparison of elicited distance distributions on a fixed benchmark. Describe storage and job management only in reproducibility materials. Avoid claiming any individual technique as a methodological first without a broader literature assessment.

### 2. Moderate — Bring the accuracy–consistency distinction into the reported scientific contribution

**Location:** `paper/main.tex:30`, `paper/main.tex:36`, `paper/main.tex:132`–`153`, `paper/generated/language-table.tex:1`–`5`, `paper/main.tex:204`.

The opening promises to distinguish knowing pairwise facts from describing a coherent geometry. Yet the narrative results largely emphasize high correlations, similar-looking maps, and language tests. The generated language table already contains an instructive contrast: Spearman correlations around 0.998 coexist with triangle-violation rates of roughly 9.6–12.2%. The current discussion does not unpack this distinction. Readers can finish the paper knowing that languages differ without understanding what reconstruction and consistency diagnostics contributed.

**Suggested fix:** add a short results paragraph explaining that high rank accuracy does not imply exact metric consistency, using the reported table values. Report violation magnitudes or point to their existing exports before interpreting how serious the violations are: counts alone treat tiny rounding violations and large incompatibilities alike. Distinguish the empirical distance matrix from its best-fitting spherical approximation. This would supply a research rationale for the geometry pipeline without adding a claim about internal maps.

### 3. Moderate — Keep the headline language claim tied to the observed prompt conditions

**Location:** `paper/main.tex:153`, `paper/main.tex:186`, `paper/main.tex:204`.

The sentence that languages change the pattern of mistakes and the conclusion that all instruction languages change the distance matrix are broader than the treatment actually varied. The methods correctly state that only one assistant-authored translation was used per language, while city names remain English. The limitation at line 186 is explicit and valuable, but a conclusion read independently can still sound like an identified effect of language itself.

This is a framing issue even if the conditional randomization calculations are correct. A specific French instruction differs from a specific English instruction in both language and wording; there is no independent replication of those factors.

**Suggested fix:** refer in the results and conclusion to “the five instruction conditions” or “these translated prompts.” Reserve claims about language-general sensitivity for a replicated wording-by-language design. Retain the distinction between distributional exchangeability tests and accuracy contrasts; do not promote a conditional p-value into evidence for different hidden worlds or a stable language-specific map.

### 4. Minor — Clarify the relevance and limits of the English–Persian antecedent

**Location:** `paper/main.tex:32`; `paper/references.bib:13`–`16`.

Karimi and Janowicz do discuss English versus Persian distance answers, so the existing citation supports that attribution. However, their two-page conference abstract's comparison table uses Google Maps routing distances as its reference, and reports illustrative examples. It does not provide the matched global geodesic repeated-sampling design of this manuscript. [Primary conference abstract, Table 1](https://ica-abs.copernicus.org/articles/7/68/2024/ica-abs-7-68-2024.pdf).

**Suggested fix:** explicitly identify this as earlier illustrative multilingual evidence, and identify the current contribution as a systematic great-circle/geodesic benchmark under a common response protocol. Do not describe current numerical accuracy as directly improving on that study, because its target distances differ. The bibliography already correctly labels it a conference abstract; preserve that qualification.

### 5. Minor — Position “cognitive” against behavioral task evaluations, not only activation studies

**Location:** `paper/main.tex:20`, `paper/main.tex:32`–`36`, `paper/main.tex:185`–`194`.

The distinction from Gurnee and Tegmark is accurate: their work analyzes learned representations, while this manuscript observes API outputs. [Primary activation study](https://arxiv.org/abs/2310.02207). The remaining framing would benefit from one behavioral cognitive-map reference. CogEval, for example, evaluates cognitive maps and planning through systematic tasks, controls, and repeated evaluations across LLMs; it concerns planning in relational environments rather than reconstruction of real-world city distances. [Primary CogEval paper](https://arxiv.org/abs/2309.15129).

**Suggested fix:** briefly distinguish reconstruction of a best-fitting geometry from demonstrating that the model uses that geometry in planning, navigation, or inference. No renaming of the project is necessary. A one-sentence operational definition of “Cognitive Atlas” as a behavioral summary would make the title's intended meaning unambiguous. An extensive navigation-literature detour is unnecessary.

## Verified strengths

- The draft explicitly rejects a first-use claim for prompted MDS (`main.tex:32`).
- Its characterization of activation-based evidence is supported by Gurnee and Tegmark, and it explicitly leaves memorization and numerical heuristics unresolved (`main.tex:34`).
- It identifies the Spanish-associated result as exploratory and does not turn the outcome into a general cultural or local-language advantage (`main.tex:165`, `188`, `194`).
- It does not infer extra semantic dimensions merely from Euclidean stress, and it separates interpolated coastlines from directly elicited capital relations (`main.tex:192`).
- The generalizations explicitly stop at the sampled conditions. There is no substantive claim here that results transfer to personality, politics, or other nongeographic concept domains.

## Scope and limits of this review

This was a targeted novelty and construct-framing review, not an exhaustive systematic literature review. Primary sources were checked for the nearest prompted-MDS antecedent, the English–Persian example, activation-based spatial representations, and behavioral cognitive-map evaluation. A literature search cannot establish absence of all competing work. I did not independently recompute numerical results, validate translations as a native speaker, audit all bibliography entries, or assess optimizer correctness. The table observations in finding 2 are descriptive readings of the manuscript's generated table, not newly reproduced measurements. The later 100-capital results and subsequent direct map tests must not be retroactively treated as analyses in this frozen paper.
