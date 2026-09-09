# Academic review 06: references and claim–source fidelity

Reviewer scope: independent source audit, 9 September 2026. Reviewed the historical 50-capital paper, not the subsequent 100-capital extension. Source commit: `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`. `paper/main.tex` SHA-256: `5f48fffc573f56005f8074bdb7e73514e3fc1671575de2be6b379b3622eb7fa4`; `paper/references.bib`: `23794082e3e32a3f7b289a02156335ca61274588dbaba90c41a0027c620aabc2`.

**Assessment: the central related-work attributions are sound. No fabricated reference or major misattribution was found. Two moderate documentation gaps should be resolved before submission, followed by three minor citation improvements.** This is a review of evidential attribution, not certification of the numerical analysis.

## Findings, ranked by severity

### 1. Moderate: the bespoke bootstrap needs a derivation and methodological references

**Location:** `paper/main.tex:117`; `paper/scripts/local_language.py:44` and `:96`.

The paragraph introduces basic intervals, centered bootstrap tail probabilities, a `sqrt(10/9)` correction, and the nonregularity of medians with ties without citing any bootstrap source. None of the fourteen references addresses bootstrap inference. A reader cannot determine which parts are standard and which are this study's modifications. This matters because the Spanish-associated claim in the abstract depends on this procedure.

The variance multiplier has an elementary justification for the sample mean: conditional empirical-bootstrap variance is `(n−1)s²/n²`, while the unbiased estimated sampling variance is `s²/n`. Multiplying deviations by `sqrt(n/(n−1))` matches those variances. **That calculation alone does not prove nominal coverage or calibrated tail probabilities.** The paper should distinguish that limited derivation from inferential validation, especially with only ten observations in each stratum.

**Requested revision:** cite an authoritative bootstrap treatment, include the mean-variance derivation in the supplement, and identify the centered, variance-adjusted procedure as the implemented approximation. Add an appropriate source or narrowly qualified explanation for the tied-median concern. Do not imply that adding a general bootstrap citation proves validity of this particular adjustment. A foundational source is [Efron, *Bootstrap Methods: Another Look at the Jackknife*](https://doi.org/10.1214/aos/1176344552); a detailed treatment is [Efron, *The Jackknife, the Bootstrap and Other Resampling Plans*](https://epubs.siam.org/doi/book/10.1137/1.9781611970319).

### 2. Moderate: the language-affinity classification lacks a complete source trail

**Location:** `paper/main.tex:98–107`; `paper/references.bib:39–49`; `paper/scripts/local_language.py:18–23`.

The paper gives explicit country groups, which is good, but attaches three broad references to a rule combining legal status and majority usage. The saved local-analysis `sources` field identifies model-result files, not the external evidence for group membership. There is no country-by-country mapping from classification to article, table, date, or legal provision. In particular, the bibliography supplies no targeted Arabic-status or mainland-China language-status source. This is a reproducibility gap in the definition of a central explanatory variable, not evidence that the listed memberships are false.

The [Cervantes report](https://cvc.cervantes.es/Lengua/anuario/anuario_24/moreno-alvarez/p02.htm) directly supports distinguishing actual use from formal status and explicitly discusses Argentina in this context. [Singapore's Article 153A](https://sso.agc.gov.sg/Act/CONS1963?ProvIds=pr153A-&WiAl=1) directly names Mandarin as an official language. The OIF source is relevant, but a whole-report citation leaves readers to locate the relevant classifications themselves.

**Requested revision:** add a small provenance table with ISO code, assigned language, rule used, exact source locator, reference date, and any exclusion rationale. Cite national legal sources where legal status is the rule, and demographic tables where majority use is the rule. Preserve the original frozen classification as a historical analysis choice; do not silently update memberships after seeing results. Specify how mainland China's standard spoken/written language category is being mapped to the experimental label “Mandarin.”

### 3. Minor: clarify the evidential scale of the closest multilingual distance predecessor

**Location:** `paper/main.tex:32`; `paper/references.bib:13–16`.

The sentence about Karimi and Janowicz is accurate: their [two-page conference abstract](https://ica-abs.copernicus.org/articles/7/68/2024/ica-abs-7-68-2024.pdf) includes English/Persian distance examples. However, the main text does not tell readers that this is an illustrative conference abstract. Its table uses Google Maps routing distances as the comparison, which differs from this manuscript's explicitly geodesic benchmark. The bibliography already correctly labels it a conference abstract.

**Requested revision:** add a short qualification in the related-work sentence: an illustrative conference abstract reporting language-dependent distance estimates against routing examples. This makes the scientific relationship more precise and avoids suggesting a prior matched, repeated great-circle experiment. Do not repeat the predecessor's causal speculation about training-data coverage as established evidence.

### 4. Minor: cite the statistical principle directly, and keep software documentation versioned

**Location:** `paper/main.tex:93`; `paper/references.bib:36–38`.

The SciPy documentation does support the `(b+1)/(B+1)` convention and the strong same-distribution null; the citation is not wrong. But it is a mutable software manual rather than the primary methodological reference. The inspected page now identifies itself as SciPy 1.18.0. The manuscript's custom stratified implementation should not be mistaken for a direct call to the documented function, whose default two-sided convention is also different from using an absolute-valued statistic with an upper-tail count.

**Requested revision:** retain the explicit algorithm already given in the paper, add the primary randomized-permutation reference identified by the [SciPy manual](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.permutation_test.html)—Phipson and Smyth (2010), *Permutation P-values Should Never Be Zero*—and pin any software-documentation URL to the version actually consulted. No numerical error is alleged here; the manuscript already states its absolute-statistic convention.

### 5. Minor: improve dataset citation identity and bibliographic precision

**Location:** `paper/references.bib:30–35` and `:47–49`; `paper/main.tex:40`.

“Populated Places and Terms of Use” combines two resources but links only to the populated-places page. The year 2026 is an access year, not an identified dataset release. The repository records source hashes in `data/capitals-50-v2.sources.json`, so stronger provenance exists but is not surfaced by the citation. The rendered bibliography also lowercases “Article 153A” to “article 153a” under the plain bibliography style.

**Requested revision:** identify the exact Natural Earth layer/release if recoverable, link its dataset URL and the separate [terms of use](https://www.naturalearthdata.com/about/terms-of-use/), and distinguish retrieval date from publication date. Preserve the coordinate-source hashes. Protect proper nouns and legal identifiers with BibTeX braces. These are citation-quality improvements; the public-domain statement itself is supported.

## Reference-by-reference verification

| Citation | Source check and result |
|---|---|
| Louwerse & Zwaan (2009) | [Publisher abstract](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1551-6709.2008.01003.x) confirms distributional text statistics, geographic MDS, authors, year, volume and pages. The manuscript's modest summary is supported. |
| Bhandari et al. (2023) | [Author preprint](https://arxiv.org/abs/2310.13002) explicitly describes prompting and MDS to recover city locations. Title, authors and identifier match. |
| Gurnee & Tegmark (2024) | [ICLR proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0a6059857ae5c82ea9726ee9282a7145-Abstract-Conference.html) confirms venue/year and activation-based representations. The manuscript correctly distinguishes this from API behavior. |
| Karimi & Janowicz (2024) | [Publisher record](https://ica-abs.copernicus.org/articles/7/68/2024/) and full abstract confirm metadata and English/Persian examples. See finding 3. |
| Karney (2013) | [Publisher record](https://link.springer.com/article/10.1007/s00190-012-0578-z) supports ellipsoidal inverse geodesics; issue year 2013 is correct despite online publication in 2012. |
| Kruskal (1964) | [Publisher record](https://link.springer.com/article/10.1007/BF02289565) confirms nonmetric goodness-of-fit formulation and metadata. |
| Schönemann (1966) | [Publisher record](https://link.springer.com/article/10.1007/BF02289451) confirms orthogonal Procrustes attribution and metadata. |
| Holm (1979) | Stable JSTOR identifier and bibliographic entry are consistent; the full primary article was not accessible through this review's browser. I did not independently re-prove familywise-error control. |
| Natural Earth | Official layer and terms pages support the dataset attribution and public-domain status. Exact release identity could be improved. |
| scikit-learn | [Version 1.7 SMACOF documentation](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.smacof.html) supports metric/nonmetric SMACOF and monotonic-regression distinctions. This verifies method attribution, not the saved run's implementation. |
| SciPy | Documentation supports the randomized plus-one convention and exchangeability framing. See finding 4. |
| Cervantes | Official report confirms authors, 2024 date, and the distinction between legal status and language use. |
| OIF | Official report exists and relevant institutional material distinguishes official status from actual French use. The entire report was not retrievable for a page-by-page classification audit. |
| Singapore constitution | Official provision directly supports Mandarin's co-official status; the legal locator is correct. |

## Strengths and limits of this review

The manuscript explicitly disclaims priority for prompted geographic MDS, separates behavior from hidden representations, identifies the brief cartographic source as an abstract in its bibliography, and uses primary sources for the main methodological foundations. These reduce the risk of citation inflation.

All fourteen entries were inspected. External checks used publisher, author-preprint, institutional, legal, or official documentation sources. Some DOI redirects and full texts were inaccessible; accessibility failures are not treated as evidence of false claims. This was not an exhaustive search for all prior literature, a legal opinion, a native-speaker validation, a numerical reproduction, or an audit of the later 100-capital maps. No paper text, references, code, or measurements were changed.
