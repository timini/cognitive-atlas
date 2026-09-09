# Response to the five publication-readiness reviews

This revision addresses GitHub issues [11](https://github.com/timini/cognitive-atlas/issues/11), [12](https://github.com/timini/cognitive-atlas/issues/12), [13](https://github.com/timini/cognitive-atlas/issues/13), [14](https://github.com/timini/cognitive-atlas/issues/14) and [15](https://github.com/timini/cognitive-atlas/issues/15). The assessed manuscript was `5f9bdaa3641f684708ad914a721eecc25835ab64`; the reports remain immutable assessments of that version. The revised article uses the same 100-capital observations. No new model calls were made.

The [criterion disposition file](publication-dispositions.json) explicitly accounts for all 1,260 original cells. Its statuses describe actions taken or remaining, not new reviewer scores or acceptance predictions. The selected preparation target is Transactions in GIS. One manuscript cannot simultaneously satisfy 18 incompatible templates and article scopes.

## Scientific and editorial changes

| ID | Review concern | Response and evidence | Remaining limit |
|---|---|---|---|
| R01 | Incremental contribution and geographic fit (reviews 01–05; C01/C02) | Introduction distinguishes prior distance/MDS work from repeated global spherical evaluation. A new antecedent table includes Bhandari, Karimi/Janowicz, Decoupes (2025) and MultiGlobeQA (2026 preprint). | This is an empirical extension; no new embedding algorithm, broad language benchmark, policy evaluation or neural mechanism is claimed. |
| R02 | High correlation and triangle violations alone are weak evidence (01 finding 2; 02 S4; 03 P1/P2) | New `revision100/error_control.py` generates 999 explicit methodological controls per condition, preserving every pair's absolute median error and therefore MAE/RMSE/absolute relative errors. Main methods/results and a table report the result. | Signs are independent except where the QC domain forces one; this control is descriptive and post hoc. It preserves neither signed bias nor error dependence and establishes no cognitive cause. |
| R03 | Conditional exchangeability versus language effects (02 S1/S2; all C09) | Result statements now explicitly condition shuffled comparisons on assumed independence/exchangeability. The six distance and three map test families remain separate. | Temporal dependence is unverified; one wording/alias/date per condition cannot identify a general language effect or unequal population median maps. |
| R04 | Fragile regional inference (all five reviews) | Removed regional p-value columns and the interval figure from the main presentation. Main conclusions use gains and sensitivities. The methods state the 3.3–7.5% coverage and 100% familywise-rejection failure; full bootstrap derivation, probabilities and the warning-labeled interval figure remain in the appendix. | The audit does not justify nominal coverage or show that the actual response law has rare tails. No equivalence or absence-of-benefit claim is made. |
| R05 | Regional groups, confounding and estimands (02 S1/S3; 03 P3/P4) | Retained named groups, endpoint counts, individual-response versus pair-median error definitions, distance balancing, omissions, and the distinction between interaction and absolute gain. | Beijing/Singapore are two cases; Arab States membership is a regional proxy, not a common cultural-affinity scale. |
| R06 | Geometry, projection, optimization and predictive scope (02 S4; 03 P2; 04 finding 7) | Retained the WGS84 spherical reference, full-spectrum checks, multistart diagnostics, in-sample neighborhood results, and explicit illustrative status of coastline warping. | No global optimum, intrinsic dimension, topology preservation, navigation skill or held-out predictive accuracy is claimed. |
| R07 | Counts, parsing, exclusions and variation (02 S5; 04 finding 6) | Abstract now says completed responses. Methods retain 148,500 slots, 148,504 attempts, 148,491 valid values and 4,948 complete pairs; unconstrained numeric collection is not relabeled as output-schema generation. | Ten answers cannot establish normality or recover unseen modes; historical execution gaps remain disclosed. |
| R08 | Abstract density and revision-process writing (01 finding 5; 05 findings 3/4) | New descriptive title and 129-word abstract. Added six keywords and a short running title. Removed dated revision subtitle and prose such as “this revision independently checks.” Shortened release-history narration while retaining scientific provenance limits. | Final title-page identities and declarations still require actual author information. |
| R09 | Main figures, supplements and file limits (all C03–C07) | 12-point double-spaced source; eight main displays. Moved dispersion, full pairwise tests and bootstrap interval visualization to referenced appendices. Four supplement ZIPs each remain under 20 MB; extracting all parts reproduces the full package. | Other journals' mandatory classes, Word conversion, PLOS figure formats and anonymous packages are deferred unless that venue is chosen. |
| R10 | Public access, citations, permanence and licensing (all C08) | Corrected stale private-repository wording. Added a formal citation to a fixed data snapshot. Full and split reproduction packages include code, observations, controls and hashes. | Permanent DOI and code/data reuse licenses need an actual archive deposit and rights-holder decisions; public access is not a substitute. |
| R11 | Human authorship and substantive AI assistance (all C10/C11) | Added an explicit Methods/provenance account of Codex assistance in drafting, coding, analysis, translation, figures and reviews. Distinguishes measured Gemini from preparation tools and automated checks from human validation. | Actual authors, affiliations, correspondence, ORCID, contributions, funding, conflicts and human checks are not supplied. No declarations have been fabricated. |
| R12 | Venue eligibility, anonymity, fees and approvals (all C11–C14) | Prepared a TGIS-specific package and scientific cover-letter draft with public-posting disclosure. Historical AI-preparation and public-identity policy holds remain documented for other venues. | No editor contacted, permission inferred, fee agreed, exclusivity attested or journal submission made. Disclosure does not establish eligibility at every venue. |

## What the new control changes

| Instructions | Observed violated triples | Control mean | Central 95% control range |
|---|---:|---:|---:|
| English | 10.69% | 11.52% | 11.15–11.92% |
| Arabic | 13.30% | 12.30% | 11.91–12.71% |
| Chinese | 10.74% | 11.85% | 11.46–12.23% |

Every control retains the observed absolute error of every pair. Only 3, 2 and 2 pairs, respectively, force a sign because of the reporting domain. The original rate of around 10% violations is therefore less surprising than it appears without an error-matched comparator. English and Chinese are more consistent than the average control by this statistic; Arabic is less consistent. Those are conditional descriptive observations, not validated language effects or a diagnosis of a neural representation. Control ranges are not sampling confidence intervals.

## Review-by-review accounting

- **01 Editorial:** its five numbered priorities map to R11/R12, R01–R04, R03/R05, R09/R10, and R08/R09/R12.
- **02 Methods:** S1→R03/R05; S2→R03; S3→R04/R05; S4→R02/R06; S5→R07. Shared package/declaration requests map to R08–R12.
- **03 Contribution:** P1→R01/R02; P2→R06; P3→R03; P4→R04/R05; P5→R11/R12; P6→R09/R10 and explicit scope limits.
- **04 Reproducibility:** findings 1–7 map to R11, R10, R10/R12, R12, R09, R07 and R03–R06.
- **05 Style/policy:** findings 1–7 map to R11, R12, R08, R08, R04, R06/R09 and R10.

## Outstanding decisions and stronger-study requests

The manuscript has been substantively revised; it is not yet a fully authorized journal submission. Actual author information was requested during this revision. The [submission declaration record](submission/transactions-in-gis/author-declarations.json) uses null for facts not supplied. Null does not mean no funding, no conflicts or no authors. Rights approval, permanent archiving, human scientific review and selected-venue portal/policy checks remain open.

Replicated, independently reviewed wordings; randomized collection blocks; additional model snapshots; localized-name factors; and held-out behavioral tasks would support stronger claims. They have not been conducted. The present paper addresses those requests by limiting its claims and specifying the needed replication design, not by claiming a rewrite supplies new evidence.

## Honest publication assessment

The study is interesting as a carefully bounded empirical case study. The strongest contribution is the connection between repeated explicit distance estimates, geographic error and global consistency, with controls that prevent overinterpretation. The transparent failure diagnosis and complete observations are useful research evidence.

The novelty is moderate. Prompted geographic reconstruction predates this project, and recent work already studies geographic distortion and broad multilingual geospatial tasks. The new error-sign control improves scientific interpretation while making the headline “inconsistent geography” less dramatic. One model alias, one time period and one unvalidated wording per condition limit a general contribution about LLMs or language.

I would consider a specialist or soundness-focused journal submission after the remaining author/rights/archive work and independent scientific reading. I would not currently pitch it as a major discovery about hidden cognitive maps or expect it to meet a demanding general-AI venue's novelty threshold. A preregistered replication across independently reviewed prompts and collection blocks would strengthen the evidence more than simply adding further capitals to this same design. This is an editorial judgment, not an acceptance forecast.
