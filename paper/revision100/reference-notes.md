# Verified reference and operational-definition notes for the 100-capital revision

Prepared 9 September 2026. This is a source-verification memo, not a claim that the new analyses were preregistered. Only this file was written. No model calls were made. Source text was checked directly where accessible; access limitations are recorded below.

## 1. Closest prior studies

### Bhandari, Anastasopoulos, and Pfoser (2023)

**Preferred publication metadata:** Prabin Bhandari, Antonios Anastasopoulos, Dieter Pfoser. *Are Large Language Models Geospatially Knowledgeable?* Proceedings of the 31st ACM International Conference on Advances in Geographic Information Systems, SIGSPATIAL ’23, Hamburg, 13–16 November 2023. DOI `10.1145/3589132.3625625`. Four-page proceedings version available in the [NSF public-access repository](https://par.nsf.gov/servlets/purl/10537831). The [ten-page arXiv version](https://arxiv.org/pdf/2310.13002) expands the presentation; cite the version actually used for section references.

**Verified:** proceedings §5 uses 93 contiguous-US cities, LLaMA-13B, prompted numeric pair distances, two-dimensional MDS, least-squares alignment to known cities, and leave-one-city coordinate prediction; it also analyzes nine census divisions. Five-beam decoding is stated on p. 2. Table 2 reports coordinate error 346.65 km for prompted distances and 190.41 km for real-distance MDS on the contiguous set; these are **coordinate errors**, not pairwise distance MAEs. The 3,527-city number belongs to a different coordinate-elicitation task. Fifty samples per prompt belong to the preposition-generation task, not repeated numeric distance estimates.

**Positioning:** geographic distance prompting, reconstruction, alignment, and real-distance controls predate this project. The present advance is repeated numeric sampling, a global spherical fit, and explicitly conditional multilingual comparisons. Do not claim priority for MDS or compare incompatible error estimands.

### Karimi and Janowicz (2024)

Mina Karimi and Krzysztof Janowicz. *Exploring challenges of Large Language Models in estimating the distance.* Abstracts of the International Cartographic Association **7**, article 68, 2024. DOI `10.5194/ica-abs-7-68-2024`. [Publisher page](https://ica-abs.copernicus.org/articles/7/68/2024/index.html); [two-page abstract](https://ica-abs.copernicus.org/articles/7/68/2024/ica-abs-7-68-2024.pdf).

Table 1 labels its reference column “Google Map Routing (km).” It includes English and Persian answers for Tehran–Isfahan and Kashmar–Kesheh. This supports attribution of earlier multilingual distance examples, not a replicated global great-circle benchmark. Their causal explanations about training exposure are not evidence available for this project's model. Keep the conference-abstract designation; do not imply directly comparable numerical accuracy or establish a general language effect from those examples.

### CogEval (2023)

The [NeurIPS publisher record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/dc9d5dcf3e86b83e137bad367227c8ca-Abstract-Conference.html) confirms *Evaluating Cognitive Maps and Planning in Large Language Models with CogEval*, **Advances in Neural Information Processing Systems 36**, main conference, 2023; DOI `10.52202/075280-3056`.

Publisher BibTeX additionally verifies pages **69736–69751**, publisher **Curran Associates, Inc.**, and volume **36**. Its displayed author order is Ida Momennejad; Hosein Hasanbeig; Felipe Vieira Frujeri; Hiteshi Sharma; Nebojsa Jojic; Hamid Palangi; Robert Ness; Jonathan Larson. Author ordering differs from the original arXiv listing and PDF title page: use the publisher's BibTeX for the published entry, rather than combining metadata from versions. [Publisher BibTeX endpoint](https://proceedings.neurips.cc/paper_files/paper/22301-/bibtex).

The study evaluates eight LLMs using systematic cognitive-map and planning tasks derived from human experiments. Its relevant distinction is **using relational structure for planning**, whereas this project fits geometry to geographic judgments. Reconstructing a low-stress geometry does not show that a model uses that geometry to plan or navigate. Do not cite CogEval as evidence that prompted geography is unstructured.

## 2. Bootstrap references and exact variance calculation

A defensible reference for the basic interval is A. C. Davison and D. V. Hinkley (1997), *Bootstrap Methods and their Application*, Cambridge University Press, DOI `10.1017/CBO9780511802843`. The [publisher frontmatter](https://www.cambridge.org/core/books/abs/bootstrap-methods-and-their-application/frontmatter/C358552520C4D386D9B6164916FD52E6) verifies author names, publication year, and the confidence-interval chapter. I did not obtain the full chapter, so do not invent an exact page/equation citation from this memo.

The [official SciPy bootstrap documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html) identifies the basic method as reverse percentile and distinguishes it from percentile and BCa intervals. The formula is independently shown in [Ryan Tibshirani's author-hosted bootstrap notes, §2.1](https://stat.cmu.edu/~ryantibs/advmethods/notes/bootstrap.pdf): if bootstrap statistic quantiles are q, the basic interval is `[2 theta_hat - q(.975), 2 theta_hat - q(.025)]`. The notes were visible through indexed PDF text; direct web opening was restricted. This formula is also derived immediately by approximating the distribution of `theta_hat - theta` with that of `theta_star - theta_hat`.

**The project's sqrt(10/9) multiplier should be justified by derivation, not portrayed as a universally prescribed bootstrap correction.** For n observed single-response errors `y_r`, write

```
s² = sum_r (y_r - y_bar)² / (n - 1).
```

One empirical-bootstrap draw has conditional variance `(n - 1)s²/n`. The mean of n independent empirical draws therefore has variance `(n - 1)s²/n²`, versus the usual variance estimate `s²/n` for the sample mean. Multiplying centered bootstrap mean deviations by `sqrt(n/(n - 1))` matches those two variances. For a linear contrast `theta_hat = sum_c a_c y_bar_c` of independently sampled cells with the **same n=10**, the shared factor similarly gives conditional variance `sum_c a_c² s_c²/n`. This covers home-group mean gains and home-minus-other interactions, provided their coefficients are defined once and cells are resampled independently.

For corrected deviations `delta_b = sqrt(10/9) * (theta_star_b - theta_hat)`, use the inverted interval `[theta_hat - quantile(delta,.975), theta_hat - quantile(delta,.025)]`. The variance calculation is exact conditional on the observed cells and independent resampling. Coverage is still approximate: matching a second moment does not validate tails, rare modes, independence, or nominal type-I error. It is not a studentized bootstrap, BCa interval, city-level bootstrap, or guarantee of 95% coverage. If cell sample sizes differ, a single multiplier is no longer justified; use complete n=10 cells or account for each cell separately. Report that analytic-SE agreement is an implementation check, not inferential calibration.

A centered-bootstrap p-value from absolute deviations is an approximate repeated-call test, not an exact randomization test. Do not use it to establish a causal language effect or uncertainty across new cities, translations, models, or collection dates. If retained, document the Monte Carlo plus-one rule, tails, family of tested contrasts, correction factor, and complete-case selection explicitly.

## 3. Proposed fixed local association sets for the 100-capital exploratory analysis

### Scope and naming

Use **two explicitly operational groups**, not a universal classifier of a city's language. They need not encode the same social construct, so compare each translated condition with English within its own group; do not rank Arabic-versus-Chinese cultural advantage from these heterogeneous groups. These are exploratory post-collection definitions. If historical outcomes were inspected before choosing them, say so. Recording them before running the new local calculation does not make them preregistered.

The prompt condition `zh` is written standard Chinese in simplified characters, conventionally labeled Mandarin in the interface; this experiment contains no speech. Arabic instructions are written standard Arabic; country membership does not measure use of that written variety.

### Arabic: fixed Arab States regional proxy

Prefer an explicit **frozen 22-country list** from a dated UN publication to an undocumented claim that every included city is predominantly Arabic-speaking. Source: G. Iattoni, E. Vermeersch, C. P. Baldé, I. C. Nnorom, R. Kuehr (2021), *Regional E-waste Monitor for the Arab States 2021*, UNU/UNITAR and ITU, Bonn, ISBN `978-92-61-35311-7`, [official ITU PDF](https://www.itu.int/dms_pub/itu-d/opb/hdb/D-HDB-E%20WASTE-2021-ARB-PDF-E.pdf), printed p. 22, section C. The full PDF was read in memory after the web tool's size limit prevented opening it. Its prose lists the 22 members used for the report's scope. This is primary institutional evidence for that regional definition, not a linguistic survey. Do not reuse the nearby unsupported generalizations about universal religious/language prevalence; do not copy the map's erroneous repeated `MAR` abbreviation for Mauritania.

The [UNCTAD League of Arab States grouping](https://investmentpolicy.unctad.org/international-investment-agreements/groupings/39/league-of-arab-states) is a current corroborating institutional listing, but full-page retrieval returned 403 and only its indexed metadata was available. It should not be the sole verification basis. The [UN group explainer](https://www.un.org/en/node/44631) confirms a 22-member regional organization but is not a full name list.

Frozen two-letter IDs from the dated ITU list:

```
AE BH DJ DZ EG IQ JO KM KW LB LY MA MR OM PS QA SA SD SO SY TN YE
```

Intersect with the exact 100-capital dataset:

```
AE BH DJ DZ EG IQ JO KW LB MA MR OM QA SA TN
```

This gives **15 capitals**, listed below. Absent from the sampled dataset: `KM LY PS SD SO SY YE`. Their absence is dataset coverage, not a decision about whether they belong to the regional source list. Full-matrix associated-pair count before exclusions is `4950 - choose(85,2) = 1380`; recompute after complete-case filtering.

| ID | Canonical capital | Country |
|---|---|---|
| AE | Abu Dhabi | United Arab Emirates |
| BH | Manama | Bahrain |
| DJ | Djibouti | Djibouti |
| DZ | Algiers | Algeria |
| EG | Cairo | Egypt |
| IQ | Baghdad | Iraq |
| JO | Amman | Jordan |
| KW | Kuwait City | Kuwait |
| LB | Beirut | Lebanon |
| MA | Rabat | Morocco |
| MR | Nouakchott | Mauritania |
| OM | Muscat | Oman |
| QA | Doha | Qatar |
| SA | Riyadh | Saudi Arabia |
| TN | Tunis | Tunisia |

Recommended manuscript label: **Arab States group (15 sampled capitals)**. Recommended interpretation: error contrast for pairs with at least one endpoint in this regional proxy. This does not measure native language, dialect, city demographics, model-training exposure, or causes of an advantage.

### Chinese: two named cases, Beijing and Singapore

Use the explicitly named set `CN SG` rather than a purported exhaustive rule classifying every Mandarin-associated place. Justification is institutional standard-language association for China and observed Mandarin home-language use in Singapore. Calling it a **Beijing–Singapore case group** is the most transparent label.

China: the [State Council's account of the revised standard-language law](https://english.www.gov.cn/news/202512/27/content_WS694f530ac6d00ca5f9a084bb.html), 27 December 2025, identifies Putonghua/Mandarin and standardized Chinese characters, and reports the revision effective 1 January 2026. This supplies current institutional context, not a measure of Beijing residents' usage or a legal analysis. The older 2000 law text should not be cited as though its version is the current law.

Singapore: use the [Singapore Department of Statistics Census 2020 dataset, table CT/17446](https://data.gov.sg/datasets/d_cc287e319cfc285408e26321e0c9cace/view). It explicitly separates Mandarin from other Chinese dialect categories. It records 1,075,172 residents with Mandarin as their most frequently spoken home language, out of a displayed total 3,596,284, and also documents English–Mandarin bilingual home use. These are **2020** census figures with stated household/speaking exclusions; they demonstrate substantial Mandarin use, not a Mandarin majority or an exclusive language identity. Avoid treating the portal's later ingestion/update date as the census year.

The [Singapore constitution Article 153A search result](https://sso.agc.gov.sg/Act/CONS1963?Phrase=Official+and+National+language&ProvIds=pr153A-&ViewType=Within&WiAl=1) currently indexes Mandarin explicitly among four official languages, but direct retrieval returned 403. The census source above is fully accessible and sufficient for this memo's limited association rationale; no inference from generic “Chinese official language” to universal Mandarin speech is needed.

| ID | Canonical capital | Country |
|---|---|---|
| CN | Beijing | China |
| SG | Singapore | Singapore |

Before exclusions this yields `4950 - choose(98,2) = 197` associated pairs. Report the two cities separately and leave-one-city sensitivities: a pooled result over two cases is particularly fragile. Malaysia's exclusion means only that it was not selected for this narrow named-case group; it is not a claim that Mandarin is absent there. Do not say this list captures all culturally or linguistically associated places.

### Dataset binding and provenance

The IDs and names above were programmatically intersected with `data/capitals-100-v3.csv` (100 records), SHA-256:

```
eae1289f55099654ffeb238660444595f752209d9d73fe6bbc5dad620d59f5d7
```

Record in the analysis manifest: source URLs and source years; retrieval date; full source regional list; included dataset IDs; excluded source IDs; the explicit Chinese two-case selection; dataset SHA; exploratory status; exact pair-membership rule (`a in group or b in group`); and complete-case exclusions. These choices define interpretable descriptive contrasts without implying that membership causes model performance.

## 4. Limits relevant to final writing

- Primary materials support the narrow facts above. This was not an exhaustive literature review or independent native-speaker validation.
- No new statistical outcomes were inspected or computed for this memo, beyond deterministic set intersections and pair counts.
- Institutional language context and regional membership do not establish a coherent “home language” construct shared by every city.
- Review source access failures are recorded rather than silently replaced with uncited assertions.
- Bibliography updates and the actual group manifest remain the lead author's responsibility; this memo modifies neither.
