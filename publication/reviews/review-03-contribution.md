# Publication-readiness review 03 — Contribution, geographic interpretation and audience

**Date:** 9 September 2026. **Manuscript:** `5f9bdaa3641f684708ad914a721eecc25835ab64`, the 100-capital English/Arabic/written-Chinese Gemini 3.5 Flash study. Author-side AI assessment of all 18 journals and 14 criteria; not journal-appointed or human peer review. I checked the manuscript, guides and 24 input hashes without reading other reports or changing the paper. PLOS’s conflicting upload instructions remain unresolved. No journal was contacted.

**Recommendation:** prepare a venue-specific revision. Transactions in GIS is the strongest geographic-audience fit; PLOS ONE is a soundness-oriented alternative; TMLR is the strongest AI-audience candidate conditional on policy clarification. No current package is ready for submission: actual human ownership, full assistance disclosure, declarations and venue-specific files remain unfinished.

## Priority findings

1. **P1 — Clarify the incremental contribution.** `paper/main.tex:32–38`, `:129–155`, `:202–205`; J01/J02/J05/J07/J09/J10/J11/J18-C02. The result joins repeated responses, metric inconsistency, global spherical reconstruction and an Earth control. Earlier numerical city-distance/MDS work is correctly cited; this is not a new embedding algorithm. Add a compact antecedent comparison across entity domain, decoding, reference distance, geometry, repeated-output retention and inferential target. Dataset size, storage format and website deployment are not sufficient novelty.
2. **P1 — Lead with effect sizes and the behavioral interpretation.** `paper/main.tex:36`, `:78–91`, `:139–178`, `:203–205`; J01/J04/J05/J07/J09/J10/J11/J14-C09. Spearman above .998 can coexist with 10.7–13.3% violated triples. The 150–158-km displacement versus a 9.5-km reference control is descriptive; the control is not a scalar bias correction. The 79–88-km between-condition shifts explain subtle world-scale differences. Fitted points obey geometry by construction, coastlines were never elicited, and neither the sphere nor stress curve proves an internal manifold, semantic dimensionality or navigation skill.
3. **P1 — Retain the instruction-condition boundary.** `paper/main.tex:47–53`, `:94–107`, `:168`, `:205–211`; J05/J07/J08/J10/J12/J13/J14/J17-C09. English entity names, unvalidated wording differences and one alias/date prevent a language-community inference. Strong common-distribution rejection can arise from dispersion changes without a population-median-map difference. Existing prose is appropriately careful. A stronger future study would randomize time blocks, independently reviewed phrasings and localized entity names as separate factors; those are new measurements, not a rewrite of current evidence.
4. **P1 — De-emphasize regional p-values.** `paper/main.tex:109–117`, `:181–200`, `:258–265`; J02/J05/J07/J08/J10/J13/J14/J15/J16/J17-C09. Arabic’s +13.1-km interaction is a smaller disadvantage, while absolute associated gain is −8.9 km; Chinese’s two-case gain is −10.7 km. These groups are not comparable cultural-affinity scales. Severe rare-tail bootstrap failure prevents interpreting ten-response intervals as reliable unseen-tail coverage. Lead with estimates, composition and sensitivities; consider moving exploratory probability columns to a supplement while retaining the failure diagnostic in reviewed main text. This is editorial/statistical advice, not a mandated journal test choice.
5. **P1 — Resolve actual authorship and AI-preparation eligibility.** `paper/main.tex:21`, `:50`, `:220`; all C10/C11. Human authors are unassigned; translation and AI-review statements omit substantive coding, analysis and drafting assistance. Responsible people must verify claims/citations and provide true identities, contributions, funding, interests and ethics applicability. T&F-linked first-draft restrictions affect J01/J04/J05/J16; J15 restricts AI scientific interpretation; J12 discourages extensive use; J10 has a policy tension; J18 has unresolved current AI-data wording. Disclosure alone does not establish eligibility, and rewriting cannot be claimed to erase provenance. Obtain candid editorial clarification where needed.
6. **P2 — Complete the archive and choose the actual audience.** `paper/main.tex:213–220`; all C08, particularly J09/J15/J16/J17/J18. The ZIP and now-public GitHub supply code/data; the paper’s privacy statement is stale (live check, 9 September 2026). DOI, reuse rights and required checklists are separate gaps. The 41.8-MB archive exceeds PeerJ/EPJ single-file limits. J03/J06/J12/J17-C01/C02 also require applied/social evidence absent here: capital errors do not demonstrate planning utility, policy impact or cultural mechanisms. Do not invent such findings to improve fit.

## Evidence key and status interpretation

- **E01 — Format and counted front matter:** `paper/main.tex:1–27`: generic 10-point A4 article, blank author, title 12 whitespace-counted words/98 characters after replacing the TeX line break, abstract 194 whitespace-counted words/1,434 characters; 15-page PDF, 1,108,680 bytes. These transparent counts are not a substitute for a venue’s count convention or template pagination.
- **E02 — Contribution and framing:** `paper/main.tex:30–40`: nearest geographic reconstruction precedents, repeated global benchmark, behavioral operational definition, exploratory scope.
- **E03 — Elicitation and estimands:** `paper/main.tex:42–76`, `:94–117`: purposive sample, WGS84 reference, one alias/date, English names, unvalidated translated instructions, clustered dispatch, strict whole-response parser, exclusions, median/global versus single-response/regional estimands, strong null and multiplicity.
- **E04 — Geometric evidence:** `paper/main.tex:78–92`, `:129–155`, `:168–178`: reconstruction/alignment, reference-sphere control, stress distinctions, convergence sensitivity, in-sample neighborhoods and illustrative deformation.
- **E05 — Interpretation and statistical limitations:** `paper/main.tex:181–211`, `:258–283`: post hoc group construction, negative absolute gains, distance balancing, exclusion sensitivity, severe rare-tail bootstrap failure, limited inference to unseen conditions.
- **E06 — Access and reuse:** `paper/main.tex:213–220`; `public/paper/reproduction.zip` is 41,789,224 bytes; public download and GitHub both supply data/code. Current manuscript states no archival DOI; root has no LICENSE file. Hash locks provide computational provenance but cannot retroactively establish historical dirty-source or provider state. No unobserved funding/license facts are presumed.
- **E07 — Figures/references/source:** `paper/main.tex:123–198`, `:225–293`; four vector figure sources; numeric `plain` bibliography sorted alphabetically, 18 cited references; multiple main/appendix tables including a two-page capital table. Separate sources exist; journal-production/accessibility certification has not been performed in this review.
- **E08 — Authorship/disclosure/package:** `paper/main.tex:21`, `:50`, `:220`; no genuine named-author title page, contribution/funding/conflict statements or full substantive assistance declaration. Submission forms, personal histories, rights choices and financial eligibility cannot be inferred.
- **E09 — Policy:** the corresponding frozen journal guide’s C10–C14 and its linked official publisher sources, especially `publication/research/geospatial-sources.md`. These distinguish studying generated responses from using assistants to prepare research/text. AI-review labeling does not exempt substantive preparation from disclosure.

**Pass** means the inspected artifact meets the verified applicable requirement, or is a positive fit judgment for C01. **Partial** names a real adaptation or unresolved subsidiary item. **Fail** names a known unmet requirement/policy conflict; it does not predict editorial rejection. **Unknown** preserves missing policy or author facts. **N/A** would require a genuinely inapplicable criterion; none of the 14 broad criteria is wholly inapplicable here. A category can be Fail because disclosure is demonstrably absent while editorial eligibility under another subsidiary policy remains Unknown. Initial format-free acceptance is kept separate from later production style.

## Complete 18 × 14 coverage

The matrices contain all 252 unique assessments. Tables below explain every non-pass; the JSON sidecar also preserves evidence for every Pass. Scope passes use E02–E04; format/count passes use E01/E06/E07 and the cited guide. Scores are not totaled or converted into acceptance odds.

| Journal | C01 | C02 | C03 | C04 | C05 | C06 | C07 |
|---|---|---|---|---|---|---|---|
| J01 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J02 | Pass | Partial | Fail | Fail | Partial | Pass | Partial |
| J03 | Partial | Partial | Unknown | Unknown | Unknown | Unknown | Partial |
| J04 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J05 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J06 | Partial | Partial | Partial | Fail | Partial | Fail | Partial |
| J07 | Pass | Partial | Partial | Partial | Fail | Partial | Partial |
| J08 | Pass | Partial | Partial | Fail | Fail | Fail | Partial |
| J09 | Pass | Partial | Unknown | Partial | Fail | Partial | Partial |
| J10 | Pass | Partial | Unknown | Partial | Fail | Partial | Partial |
| J11 | Pass | Partial | Partial | Partial | Partial | Unknown | Partial |
| J12 | Partial | Partial | Partial | Fail | Fail | Fail | Partial |
| J13 | Pass | Partial | Pass | Partial | Partial | Partial | Partial |
| J14 | Pass | Partial | Partial | Partial | Pass | Partial | Fail |
| J15 | Pass | Partial | Pass | Fail | Pass | Partial | Partial |
| J16 | Pass | Partial | Partial | Fail | Partial | Fail | Fail |
| J17 | Partial | Partial | Partial | Fail | Partial | Partial | Fail |
| J18 | Pass | Partial | Partial | Partial | Pass | Partial | Partial |

| Journal | C08 | C09 | C10 | C11 | C12 | C13 | C14 |
|---|---|---|---|---|---|---|---|
| J01 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J02 | Partial | Partial | Fail | Fail | Partial | Unknown | Partial |
| J03 | Partial | Partial | Fail | Fail | Unknown | Unknown | Partial |
| J04 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J05 | Partial | Partial | Fail | Fail | Unknown | Unknown | Partial |
| J06 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J07 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J08 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J09 | Fail | Partial | Fail | Fail | Partial | Unknown | Partial |
| J10 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J11 | Partial | Partial | Fail | Fail | Unknown | Unknown | Partial |
| J12 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J13 | Partial | Partial | Fail | Fail | Partial | Unknown | Partial |
| J14 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J15 | Fail | Partial | Fail | Fail | Partial | Unknown | Partial |
| J16 | Fail | Partial | Fail | Fail | Fail | Unknown | Partial |
| J17 | Fail | Partial | Fail | Fail | Fail | Unknown | Partial |
| J18 | Fail | Partial | Fail | Fail | Partial | Unknown | Partial |

### J01 — International Journal of Geographical Information Science

[Criteria and subsidiary requirements](../journals/j01-international-journal-of-geographical-information-science.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J01-C02 | Partial | The repeated global spherical benchmark is useful, but its incremental contribution over 93-city distance/MDS research needs a sharper comparison; current article taxonomy remains unverified (E02). |
| J01-C03 | Unknown | The official guide could not establish word, abstract or page limits; 194 abstract words and 15 generic-layout pages do not establish journal compliance (E01). |
| J01-C04 | Partial | Readable research sections and operational cognitive framing exist; keywords are absent and journal-specific heading/title requirements remain unverified (E01–E02). |
| J01-C05 | Unknown | Working TeX/PDF exists, but journal-specific LaTeX and format-free acceptance were not verified; do not treat the generic article class as accepted (E01). |
| J01-C06 | Unknown | Primary antecedents are cited, but the required reference style remains inaccessible; current plain numbered/alphabetical output cannot be certified (E02, E07). |
| J01-C07 | Partial | Capital-only measurements and illustrative coastline captions are distinguished; final artwork/accessibility/file rules still need checking and grayscale inspection (E04, E07). |
| J01-C08 | Partial | Data/code statement and public reproduction ZIP exist; persistent archive, reuse permission and anonymous review deposit remain unresolved (E06). |
| J01-C09 | Partial | Reference-sphere and metric diagnostics support GIScience claims; temporal dependence and the strong-null interpretation constrain language inference (E03–E05). |
| J01-C10 | Fail | The paper expressly leaves human authors and affiliations unassigned; contributions, funding, conflicts and applicable ethics statements are missing (E08). |
| J01-C11 | Fail | The recorded substantive assistant drafting conflicts with the verified T&F first-draft restriction; full tool/version/role disclosure is also missing. Editorial eligibility requires a ruling, not cosmetic rewriting (E08–E09). |
| J01-C12 | Fail | Double-anonymous materials are not prepared: account-identifying Pages/GitHub links remain in the paper and archive; a blank author field does not anonymize them (E06). |
| J01-C13 | Unknown | Exact APC/licenses and actual author funding or rights decisions are unresolved; no assumption of free OA is justified (J01 guide C13). |
| J01-C14 | Partial | Exclusive-submission package and author approvals are absent. Public identity exposure creates a separate eligibility hold under the cited journal instructions; disclose it rather than erase history (E06, E08). |

### J02 — Transactions in GIS

[Criteria and subsidiary requirements](../journals/j02-transactions-in-gis.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J02-C02 | Partial | Original research is the appropriate category; foreground the accuracy/coherence distinction and reference control rather than collection scale or implementation (E02, E04). |
| J02-C03 | Fail | The 194-word abstract exceeds the verified 150-word maximum; main-text ceiling remains unknown and needs separate checking (E01). |
| J02-C04 | Fail | The mandatory 5–6 keywords and under-40-character running title are absent; current 10-point single-spaced layout also differs from preferred 12-point double spacing (E01). |
| J02-C05 | Partial | LaTeX and free-format initial submission are permitted; existing PDF/source is usable, but contradictory initial-upload instructions require live-portal resolution (E01). |
| J02-C07 | Partial | Separate vector figures and captions exist; revision-stage separate table/supplement files and final-size accessible encodings still need a submission manifest (E07). |
| J02-C08 | Partial | Underlying observations and scripts are publicly downloadable, but expected archiving and formal dataset citation need a durable release and verified reuse terms (E06). |
| J02-C09 | Partial | Methods define denominators, Monte Carlo families and the failed tail calibration; independent time/phrasing replication is absent, limiting interpretations rather than invalidating the descriptive benchmark (E03–E05). |
| J02-C10 | Fail | Human authors, affiliations, required submitting-author ORCID and authentic contribution/funding/conflict records are absent (E08). |
| J02-C11 | Fail | Wiley substantive-AI disclosure and verification/accountability record are missing; Gemini-as-subject and ten AI reviews do not disclose code/text preparation or applicable tool terms (E08–E09). |
| J02-C12 | Partial | Single-anonymous review does not require removing public project identity, but actual author metadata is missing and no named submission package exists (E08). |
| J02-C13 | Unknown | Standard copyright and optional OA routes exist; current OA quote, institutional coverage and author license choice are not known (J02 guide C13). |
| J02-C14 | Partial | Wiley Authors/Research Exchange forms, exclusive-submission declaration and author approval remain to be prepared; disclose the existing public manuscript and confirm its treatment (E06, E08). |

### J03 — Computers, Environment and Urban Systems

[Criteria and subsidiary requirements](../journals/j03-computers-environment-and-urban-systems.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J03-C01 | Partial | AI/geocomputation overlap exists, but national-capital distances do not evaluate an urban or environmental system (E02, E05). |
| J03-C02 | Partial | An empirical article would need a demonstrated urban/environmental contribution; adding speculative planning implications would not supply one. Portal taxonomy is unresolved (E05). |
| J03-C03 | Unknown | Official abstract, word and page limits were inaccessible; no third-party 250-word assumption should be used (E01; J03 guide C03). |
| J03-C04 | Unknown | Existing English research sections are readable, but mandatory keywords, highlights and graphical-abstract rules are not verified (E01). |
| J03-C05 | Unknown | TeX/PDF/vector source exists; current journal template and initial-upload rules remain inaccessible (E01, E07). |
| J03-C06 | Unknown | The journal bibliography style and initial flexibility are unverified; do not borrow another Elsevier journal style as authority (E07). |
| J03-C07 | Partial | The paper separates geodesics, fitted points and illustrative coastlines, but final artwork dimensions/resolution/supplement limits are unverified (E04, E07). |
| J03-C08 | Partial | The public ZIP and availability section support reuse; this journal data-policy tier, persistent archive and actual reuse license remain unresolved (E06). |
| J03-C09 | Partial | The benchmark is reproducible descriptively, but no decision task or acceptable urban-error threshold is measured; keep routing/planning claims absent (E03–E05). |
| J03-C10 | Fail | Elsevier accountable human authorship and authentic funding/conflict/contribution declarations have not been supplied (E08). |
| J03-C11 | Fail | Required manuscript-preparation and research-assistance disclosures are absent; distinguish assistant coding/analysis/text from observed Gemini output generation (E08–E09). |
| J03-C12 | Unknown | Journal-specific single/double anonymity was not verified; prepare removable title metadata without pretending the review mode is known (J03 guide C12). |
| J03-C13 | Unknown | Subscription with OA support is known, but current APC, license options and author funding/rights decisions are not (J03 guide C13). |
| J03-C14 | Partial | Public preprint history can be disclosed under publisher policy; actual journal package fields, exclusive-submission statement and human approval remain missing (E06, E08). |

### J04 — Cartography and Geographic Information Science

[Criteria and subsidiary requirements](../journals/j04-cartography-and-geographic-information-science.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J04-C02 | Partial | A research article needs a contribution about representation choices; compare display alternatives on the saved coordinates without claiming an unmeasured usability improvement (E02, E04). |
| J04-C03 | Unknown | Current word, page and abstract limits could not be verified; the generic PDF length is not a journal count (E01). |
| J04-C04 | Partial | Operational framing and map caveats are present; keywords and exact abstract/heading conventions remain absent or unverified (E01–E02). |
| J04-C05 | Unknown | Current LaTeX/template and format-free eligibility are journal-specific and unverified; preserve the source until checked (E01). |
| J04-C06 | Unknown | Exact bibliography style is unresolved despite appropriate MDS/geodesic/alignment antecedents in the paper (E02, E07). |
| J04-C07 | Partial | Interactive displays and free color are supported, but rights clearance and accessible final-size legends must be completed; illustrative geometry is already identified (E04, E07). |
| J04-C08 | Partial | Complete raw/analysis access exists through the public ZIP; anonymous permanent deposit and permissions remain unfinished, and the sharing tier is unknown (E06). |
| J04-C09 | Partial | The text correctly admits possible folded triangles and unmeasured coastline shape; add a visual sensitivity comparison if claiming interpretive advantages of this deformation (E04). |
| J04-C10 | Fail | Human author/contribution declarations and geographic-input rights audit are not completed; author information remains expressly unassigned (E08). |
| J04-C11 | Fail | Substantive assistant drafting conflicts with T&F first-draft guidance and lacks the detailed required disclosure. Obtain an honest eligibility determination (E08–E09). |
| J04-C12 | Fail | The account-associated manuscript URLs and reproduction archive have not been anonymized for the verified double-anonymous process (E06). |
| J04-C13 | Unknown | Hybrid/Open Select and free color do not establish an OA price; exact fees/licenses and author funding eligibility remain unresolved (J04 guide C13). |
| J04-C14 | Partial | ScholarOne package and authentic approvals are not prepared; disclose public posting and clarify journal preprint/package rules separately from anonymity (E06, E08). |

### J05 — Spatial Cognition & Computation

[Criteria and subsidiary requirements](../journals/j05-spatial-cognition-and-computation.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J05-C02 | Partial | An empirical study is appropriate, but theoretical value needs a clearer account of which alternatives accuracy, coherence and stability can distinguish—and which remain observationally equivalent (E02, E05). |
| J05-C03 | Unknown | Current numerical article/abstract/page limits are unverified; neither 194 words nor 15 generic pages can be certified against them (E01). |
| J05-C04 | Partial | Readable behavioral definition exists; add keywords and explicit exploratory questions while checking journal heading/keyword requirements (E01–E02). |
| J05-C05 | Unknown | LaTeX acceptance and current template are unresolved; no general publisher template should be assumed acceptable (E01). |
| J05-C06 | Unknown | Exact style is unverified. Prior geographic reconstruction is acknowledged, but stronger cognitive-theory engagement would improve interpretation (E02, E07). |
| J05-C07 | Partial | Residual plots and reference controls are useful; provide an accessible repeated-answer distribution example and check currently unknown artwork/supplement specifications (E04, E07). |
| J05-C08 | Partial | Exact prompts, raw observations and group definitions are publicly available, but persistent anonymous archive, reuse rights and sharing-policy tier remain unresolved (E06). |
| J05-C09 | Partial | The behavioral boundary is careful; one unvalidated wording with English names cannot identify language-specific spatial representation, and no human or navigation comparison was collected (E03–E05). |
| J05-C10 | Fail | Accountable human authorship/contributions and real funding/conflict/ethics-applicability declarations are missing; model queries do not automatically require human-participant approval (E08). |
| J05-C11 | Fail | T&F first-draft restriction conflicts with the recorded preparation; required tool/version/role disclosure is absent. Neither model subject matter nor later human editing establishes eligibility (E08–E09). |
| J05-C12 | Unknown | Anonymous expert referees are verified, but author anonymity is not; confirm author-side review requirements rather than infer double anonymity (J05 guide C12). |
| J05-C13 | Unknown | Open Select is offered, but exact APC/licenses/incidental charges and author funding details are unknown (J05 guide C13). |
| J05-C14 | Partial | ScholarOne route exists; actual package, prior-posting interpretation and exclusive-submission/author approvals need completion (E06, E08). |

### J06 — Applied Spatial Analysis and Policy

[Criteria and subsidiary requirements](../journals/j06-applied-spatial-analysis-and-policy.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J06-C01 | Partial | Quantitative spatial analysis overlaps, but no applied policy question or decision consequence is evaluated (E02, E05). |
| J06-C02 | Partial | A Research Paper needs an empirically supported application; a public atlas and hypothetical policy paragraph do not establish that contribution (E05). |
| J06-C03 | Partial | The 194-word abstract meets 150–250; the normally 8,000-word article rule needs a venue-specific count because its inclusions are unverified (E01). |
| J06-C04 | Fail | Required 4–6 keywords are absent; current sections remain within three numbered levels, so the heading hierarchy itself is acceptable (E01). |
| J06-C05 | Partial | Editable TeX is available and accepted for mathematical work; package all included tables/figures and consider the recommended Springer template before submission (E01, E07). |
| J06-C06 | Fail | Current numeric citations do not meet author–year style; convert to alphabetical author–year references with DOI links (E07). |
| J06-C07 | Partial | Figures/tables are numbered and cited, but captioned supplements and final accessible production files are not organized as a journal package (E07). |
| J06-C08 | Partial | An availability section and public code/data exist; persistent archive, verified reuse permissions and anonymous access still need completion (E06). |
| J06-C09 | Partial | Statistical claims are bounded, but practical/causal policy inference has no supporting evaluation; choose another venue rather than add unsupported implications (E05). |
| J06-C10 | Fail | Required contribution/conflict interface fields and authentic author/funding/ethics declarations are absent (E08). |
| J06-C11 | Fail | Substantive assistant use requires Methods disclosure beyond the narrow copyediting exemption; the existing AI-review paragraph does not provide it (E08–E09). |
| J06-C12 | Fail | Double-anonymous manuscript/supplements still expose project identity in URLs; populate real author details privately using the newer portal fields (E06, E08). |
| J06-C13 | Unknown | Subscription has no APC and listed optional OA routes exist; actual author license/funder choice, coverage and acceptance-date quote remain undecided (J06 guide C13). |
| J06-C14 | Partial | Exclusive submission, coauthor approval and accurate prior-posting disclosures are not prepared; follow current interface over obsolete title-page instructions (E06, E08). |

### J07 — Transactions of the Association for Computational Linguistics

[Criteria and subsidiary requirements](../journals/J07-tacl.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J07-C02 | Partial | A completed empirical evaluation fits, but technical significance needs a precise increment beyond numerical-distance MDS antecedents; no new embedding algorithm is demonstrated (E02). |
| J07-C03 | Partial | Ten main pages plus separate five-page replication and three-page complementary appendices require actual TACL reflow; the current 15-page generic PDF is not directly comparable (E01). |
| J07-C04 | Partial | Literal title and self-contained sections work; keep primary caveats in reviewed main text and prepare portal metadata/optional 5–10 keyword comments (E01, E05). |
| J07-C05 | Fail | The required official TACL format is not used; generic article source must be ported and publication LaTeX sources prepared (E01). |
| J07-C06 | Partial | The supplied ACL bibliography style remains to be applied; closest geographical antecedents are already present and should remain prominent (E02, E07). |
| J07-C07 | Partial | Appendices follow references, but anonymization and the conflicting external-artifact-link guidance are unresolved; non-reviewed appendices must not carry indispensable conclusions (E05–E07). |
| J07-C08 | Partial | Promised code/data already exist publicly; prepare an anonymous allowed-access route and explicit license/archive record rather than point reviewers at identifying URLs (E06). |
| J07-C09 | Partial | The strong-null and wording limitations are well stated; make the NLP claim about three instruction conditions, with no generalized language effect or verified independent sampling (E03–E05). |
| J07-C10 | Fail | Mandatory complete coauthor profiles and genuine human contribution/funding/conflict declarations are absent (E08). |
| J07-C11 | Fail | ACL-required content-generation acknowledgments are missing; writing, code, translation, analysis and author-side AI review roles need truthful disclosure and human accountability (E08–E09). |
| J07-C12 | Fail | The submission and supplementary links are identifying; the removal of a pre-submission anonymity period permits public preprints but not identifying review materials (E06). |
| J07-C13 | Unknown | No submission/publication fees and immediate OA are verified; actual copyright/license agreement and rights authorization still need human confirmation (J07 guide C13). |
| J07-C14 | Partial | No concurrent archival review is permitted; actual author histories must be checked for nine-month ACL-family and twelve-month TACL rejection exclusions, alongside portal approvals (E08). |

### J08 — Computational Linguistics

[Criteria and subsidiary requirements](../journals/J08-computational-linguistics.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J08-C02 | Partial | Short Paper is a sensible focused-results category; strengthen the lesson about rank accuracy versus metric coherence without promoting the study to a comprehensive spatial theory (E02, E04). |
| J08-C03 | Partial | The typical 20-page initial/25-page final Short Paper limits need the CL class; 15 generic pages do not prove compliance and the abstract ceiling is unverified (E01). |
| J08-C04 | Fail | English prose and abstract exist, but required separate title/author/abstract metadata and 5–10 editorial keywords are not prepared (E01, E08). |
| J08-C05 | Fail | Mandatory clv2025.cls is absent; current generic article LaTeX must be ported and rendered, preserving equations and multilingual supplement access (E01). |
| J08-C06 | Fail | Required CL citation/reference files are not used; current plain numeric bibliography requires conversion (E07). |
| J08-C07 | Partial | The static paper is independently readable; editable vector figures exist, but journal-specific supplement ceilings and final accessibility specifications remain unverified (E07). |
| J08-C08 | Partial | ACL-promised artifacts exist in the public ZIP and now-public GitHub; add a persistent citation and explicit artifact reuse permissions (E06). |
| J08-C09 | Partial | The manuscript distinguishes conditional resampling from new-language/date inference; the failed rare-tail diagnostic and fixed unvalidated translations must stay visible (E03–E05). |
| J08-C10 | Fail | Mandatory full human names, affiliations and emails, plus authentic contribution/funding/conflict disclosures, are not supplied (E08). |
| J08-C11 | Fail | ACL-required acknowledgments must describe substantive generated text/code/analysis/translation assistance; the existing review statement is insufficient (E08–E09). |
| J08-C12 | Fail | The single-blind checklist requires author names/affiliations on page one; the blank author field is a known failure, not anonymity compliance (E01, E08). |
| J08-C13 | Unknown | Immediate OA is known, but current exact fees/license and the authors ability to assign copyright to ACL remain unverified (J08 guide C13). |
| J08-C14 | Partial | Originality/concurrent archival-review declarations and any conference-extension history require real author confirmation; no compliant submission package has been prepared (E08). |

### J09 — Journal of Artificial Intelligence Research

[Criteria and subsidiary requirements](../journals/J09-jair.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J09-C02 | Partial | A full Article fits the multiple analyses; significance beyond one model snapshot and established MDS needs clearer evidential comparison to closest work (E02, E05). |
| J09-C03 | Unknown | No strict article/abstract ceiling was verified; concision advice is not evidence of unlimited permitted length (E01; J09 guide C03). |
| J09-C04 | Partial | Readable sections exist; consider encouraged structured abstract and implement final heading/Figure/Table capitalization without treating this advice as an initial rejection rule (E01). |
| J09-C05 | Fail | JAIR-formatted submission PDF is required, while the manuscript uses generic article; final complete source archive is a later obligation (E01). |
| J09-C06 | Partial | Current style needs JAIR configuration at production; published methodological antecedents are present but the precise incremental contrast should be more explicit (E02, E07). |
| J09-C07 | Partial | Grayscale readability needs inspection; keep essential calibration/reference evidence in the review PDF because online appendices are outside review, and complete the final code release form (E05–E07). |
| J09-C08 | Fail | The mandatory appended JAIR reproducibility checklist is absent despite extensive available code/data; its omission is an explicit desk-rejection condition (E06). |
| J09-C09 | Partial | Reproducible diagnostics support the descriptive result; independent time/prompt/model replication is absent and ten responses cannot characterize unobserved tails (E03–E05). |
| J09-C10 | Fail | Human authors and accountable scientific contributions remain unassigned; funding/conflict records and independent human verification are not documented (E08). |
| J09-C11 | Fail | Actual assistance is not fully disclosed and human ownership of the core contribution is not established in the manuscript; AI cannot supply qualifying authorship (E08–E09). |
| J09-C12 | Partial | Named submission metadata is missing; reviewer confidentiality does not itself require double-anonymous preparation, and no such mandate was verified (E08; J09 guide C12). |
| J09-C13 | Unknown | No author fees and final CC BY are verified; actual author acceptance of the publication agreement and rights in code/data remain unconfirmed (J09 guide C13). |
| J09-C14 | Partial | Three mandatory editorial answers—importance, closest JAIR work, prior publication—are not prepared; exclusivity and genuine author approval must be confirmed (E08). |

### J10 — Transactions on Machine Learning Research

[Criteria and subsidiary requirements](../journals/J10-tmlr.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J10-C02 | Partial | The evidence-and-interest standard suits a bounded empirical article; sharpen the reusable finding and keep claims commensurate with one alias and three fixed conditions (E02, E05). |
| J10-C03 | Unknown | Variable length is allowed but no abstract ceiling was verified; the current generic-page count cannot certify all length rules (E01; J10 guide C03). |
| J10-C04 | Partial | Core results and strong null are in main text; adopt the template front matter and check any current keyword fields, whose mandatory count is unknown (E01, E05). |
| J10-C05 | Fail | The mandatory unmodified TMLR LaTeX template is not used; the current generic format is a demonstrable submission-format failure (E01). |
| J10-C06 | Partial | Regenerate citations using the template configuration; retain prior distance-reconstruction work and verify final output rather than claiming current plain style is approved (E02, E07). |
| J10-C07 | Partial | The 41,789,224-byte ZIP is below 100 MB and appendices follow references, but all supplements need anonymization and critical evidence must remain in the paper (E06–E07). |
| J10-C08 | Partial | Public frozen inputs, scripts and local verification support reproducibility; anonymous bundle testing, persistent archive and clear reuse permissions remain unfinished (E06). |
| J10-C09 | Partial | Claims are largely reduced to evidence; avoid treating common-distribution rejection as equal-median rejection or pair cells as independent country observations (E03–E05). |
| J10-C10 | Fail | Fixed-at-submission human author set, active profiles, conflicts, funding and human-subject applicability records are not supplied (E08). |
| J10-C11 | Fail | The FAQ-required first-page AI disclosure footnote is absent. Editorial/FAQ tension about human-sourced ideas/results also requires clarification given extensive assistance (E08–E09). |
| J10-C12 | Fail | Double-blind OpenReview materials still contain identifying URLs/metadata. Public preprints are allowed, but the anonymous submission must not link to them (E06). |
| J10-C13 | Unknown | No fees and CC BY 4.0 from submission are known; human authors have not authorized rights/licensing or durable public-review exposure (J10 guide C13). |
| J10-C14 | Partial | Author quotas/profiles and non-overlap declarations are unchecked; nonarchival posting is allowed, but archival extension restrictions and actual author approval require confirmation (E08). |

### J11 — Artificial Intelligence (AIJ, Elsevier)

[Criteria and subsidiary requirements](../journals/J11-artificial-intelligence.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J11-C02 | Partial | A regular article fits better than compressing multiple analyses into a Research Note; mature novelty needs a general AI lesson beyond standard-tool application (E02, E05). |
| J11-C03 | Partial | The editorial FAQ has no hard regular-article cap; 20–30 pages is advice and the 4,500-word Research Note cap is inapplicable to the proposed route. Current abstract ceiling remains unknown (E01). |
| J11-C04 | Partial | English, abstract and references are present; mandatory publisher keywords/highlights counts could not be verified and submission metadata is missing (E01, E08). |
| J11-C05 | Partial | Single-column A4 complies with preferred shape; current 10-point text falls below preferred 11-point minimum, and elsarticle conversion is recommended rather than proven mandatory (E01). |
| J11-C06 | Unknown | Current publisher citation style was inaccessible; consistent primary references exist but exact production compliance cannot be certified (E02, E07). |
| J11-C07 | Partial | Vector figures/captions are substantial inputs, but final publication quality at journal size and current artwork/supplement ceilings remain to be checked (E07). |
| J11-C08 | Partial | Availability section and public code/data are present; current journal-specific data tier, durable archive and explicit reuse license remain unresolved (E06). |
| J11-C09 | Partial | Reference controls and finite-sample diagnostics strengthen completeness; a stronger general AI claim would need additional independent evidence, not stronger wording (E03–E05). |
| J11-C10 | Fail | Elsevier-required genuine authorship, contributions, funding and conflicts have not been supplied; AI checks do not establish human scientific responsibility (E08). |
| J11-C11 | Fail | Required manuscript AI declaration before references and research/code assistance disclosure in Methods are missing; name actual tools and oversight truthfully (E08–E09). |
| J11-C12 | Unknown | Current journal anonymity model was not directly verified; do not import generic Elsevier double-anonymous instructions (J11 guide C12). |
| J11-C13 | Unknown | Current journal APC, subscription charges and licenses were inaccessible; author funding and rights choices are also unresolved (J11 guide C13). |
| J11-C14 | Partial | Editorial Manager package, exclusive-review declarations and author approval remain unprepared; disclose preprint and any conference history accurately (E06, E08). |

### J12 — AI & SOCIETY

[Criteria and subsidiary requirements](../journals/J12-ai-and-society.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J12-C01 | Partial | The study concerns AI but does not measure societal/cultural effects or language-community experience; a social argument cannot be inferred from pair errors (E03, E05). |
| J12-C02 | Partial | A Research Article requires an evidenced societal argument absent here; merely reducing equations or adding colonial-bias speculation would not meet that threshold (E02, E05). |
| J12-C03 | Partial | The 194-word abstract satisfies the ordinary 150–250 range; the normal 10,000-word scale is not a target to pad toward, and a venue-specific count remains needed (E01). |
| J12-C04 | Fail | The required 4–6 keywords are absent; heading depth already fits three levels, but reader-facing definitions should be strengthened for this audience (E01–E02). |
| J12-C05 | Fail | Journal-specific Word-only submission conflicts with the current TeX/PDF package; editable DOCX conversion and equation/reference QA would be necessary if eligibility is resolved (E01). |
| J12-C06 | Fail | Numeric plain citations fail the required author–year alphabetical style; DOI links and relevant social scholarship must follow any genuinely supported claim (E07). |
| J12-C07 | Partial | Figures/tables are numbered and cited; supplements need Online Resource captions and accessible final artwork, with website content supplementary to the reviewed evidence (E07). |
| J12-C08 | Partial | Data Availability content and public ZIP exist, but permanent anonymous deposit and artifact licensing/attribution remain incomplete (E06). |
| J12-C09 | Partial | Conditional effects and uncertainty are disclosed, but no causal cultural/social interpretation is supported; the regional proxy is not a sampled language community (E03–E05). |
| J12-C10 | Fail | Required human contributions, competing interests and authentic funding/ethics-applicability interface records are missing (E08). |
| J12-C11 | Fail | Substantive Methods disclosure is absent. Extensive drafting/analysis also conflicts with the journal’s strong discouragement beyond grammar/translation; permissibility is unresolved, not a proven blanket ban (E08–E09). |
| J12-C12 | Fail | Double-blind review materials retain identifying public links; separate real portal identities from anonymous manuscript/supplements (E06, E08). |
| J12-C13 | Unknown | Subscription without APC and optional OA quotes/licenses are known; author coverage, acceptance-date price and license choice require confirmation (J12 guide C13). |
| J12-C14 | Partial | Exclusive-submission and public-prepublication disclosures plus author-approved Word/files package are missing; clarify AI eligibility before conversion (E06, E08). |

### J13 — PLOS ONE

[Criteria and subsidiary requirements](../journals/J13-plos-one.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J13-C02 | Partial | Research Article is appropriate under technical-soundness review; the bounded descriptive finding is sufficient to argue relevance without alleging a new general AI theory (E02, E05). |
| J13-C04 | Partial | Research sections exist; title page, double spacing, continuous line numbers and acknowledgments need house-style adaptation. Initial format flexibility is ambiguous for LaTeX; verify stage-specific handling (E01, E08). |
| J13-C05 | Partial | Official format-free advice conflicts with the LaTeX template warning and no-embedded-figures request. Current PDF embeds figures; prepare a flattened TeX source/separate artwork and confirm portal handling (E01, E07). |
| J13-C06 | Partial | Current numbered bibliography is alphabetical, so final Vancouver first-citation order requires conversion; this is a final-style task, not a format-free initial blocker (E07). |
| J13-C07 | Partial | Four vector PDF plots need TIFF/EPS conversion, 300–600-dpi or appropriate vector/font checks and ≤10-MB files. The LaTeX route requests separate figures initially; resolve the format-free tension (E07). |
| J13-C08 | Partial | Public ZIP supplies underlying responses and essential custom code, satisfying access in substance; verify license/availability wording and preferably archive with a persistent identifier (E06). |
| J13-C09 | Partial | Technical transparency is strong, but local bootstrap significance remains fragile despite candid calibration disclosure; emphasize estimates and keep the conditional tail limitation next to inference (E03–E05). |
| J13-C10 | Fail | Required human authors/correspondence/ORCID and CRediT are absent; funding and competing interests must be completed truthfully in designated forms (E08). |
| J13-C11 | Fail | Methods does not disclose all preparation tools, actual uses, validation and affected content; the human ownership/accountability record is unassigned (E08–E09). |
| J13-C12 | Partial | Author identities and review-history preference must be supplied; account URLs are not a double-anonymity failure here, and internal AI reports must stay distinct from journal review (E06, E08). |
| J13-C13 | Unknown | The listed US$2,477 and CC BY route are known; actual funding assistance, author rights and acceptance of charges remain undetermined (J13 guide C13). |
| J13-C14 | Partial | Required one-page cover letter, author approvals, prior-posting disclosures and exclusive-submission statement are not prepared; the existing preprint itself is allowed (E06, E08). |

### J14 — Scientific Reports

[Criteria and subsidiary requirements](../journals/J14-scientific-reports.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J14-C02 | Partial | Article is the appropriate category; preserve the fixed-conditions result and do not retrospectively call this exploratory collection a Registered Report (E02, E05). |
| J14-C03 | Partial | Title is 12 words and abstract 194, meeting 20/200; recommended 11 typeset pages and 4,500 main-text words require a supplement split and the specified exclusion-based count (E01). |
| J14-C04 | Partial | Unstructured abstract and coherent main sections already fit; add appropriate keyword/front-matter fields while treating suggested body order as advice (E01, E08). |
| J14-C06 | Partial | Eighteen cited entries are below the recommended 60, but current plain alphabetical numbering needs Nature reference-order/style conversion (E07). |
| J14-C07 | Fail | The current review PDF includes more than eight display items and a two-page capital table; move appendices to a separate supplement and select at most eight main figures/tables (E07). |
| J14-C08 | Partial | An availability section and public code/data bundle exist; formal deposition/supplement route, code-policy compliance and reuse permissions require completion (E06). |
| J14-C09 | Partial | The descriptive benchmark is supported; clustered calls and one wording/date do not provide independent condition replication, and regional uncertainty is explicitly fragile (E03–E05). |
| J14-C10 | Fail | Required human authors, correspondence, contributions, explicit conflicts, funding and applicable ethics declarations are absent (E08). |
| J14-C11 | Fail | Required Methods disclosure omits assistant drafting/coding/analysis; detailed current AI-policy exceptions were not accessible and must be checked rather than assumed (E08–E09). |
| J14-C12 | Fail | Required identified-author title page is missing; detailed review options remain unverified, so do not assume anonymous preparation resolves this (E01, E08). |
| J14-C13 | Unknown | Fully OA and a portfolio starting-price indication are known; exact journal invoice currency/tax/license/coverage and author funding remain unresolved (J14 guide C13). |
| J14-C14 | Partial | Cover letter, correspondence, reviewer suggestions/exclusions, prior-editor discussions and author/exclusivity approvals are not prepared; disclose the public release (E06, E08). |

### J15 — Royal Society Open Science

[Criteria and subsidiary requirements](../journals/J15-royal-society-open-science.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J15-C02 | Partial | Research Article under soundness-based review fits; emphasize a bounded finding and informative null local advantage without presenting exploratory inference as confirmatory (E05). |
| J15-C04 | Fail | Required full title page and 3–10 keywords are absent; standardize British English and retain consistent kilometre/SI notation during adaptation (E01, E08). |
| J15-C06 | Partial | Final Vancouver first-citation numbering differs from the current alphabetical plain style; data/code identifiers need formal citations at production (E07). |
| J15-C07 | Partial | The 41.8-MB bundle is below the 350-MB individual cap; later source figures/tables and CC BY-compatible supplementary rights still need a formal package (E06–E07). |
| J15-C08 | Fail | Public access exists, but no qualifying CC0 or CC BY license for underlying data/code/materials is documented; required openness is more than a downloadable ZIP (E06). |
| J15-C09 | Partial | Reference-controlled, reproducible descriptions are suitable; conditional tests cannot support independently replicated language effects and local tail uncertainty must remain explicit (E03–E05). |
| J15-C10 | Fail | Required submitting-author ORCID and human author/contribution/funding/conflict declarations are missing (E08). |
| J15-C11 | Fail | Actual assistant drafting/analysis exceeds the verified writing-support boundary and lacks affected-elements disclosure; obtain an editorial eligibility ruling without mislabeling assistance as readability editing (E08–E09). |
| J15-C12 | Partial | Single-anonymous review needs author identities and an informed decision about mandatory publication of journal review history; these author-side AI reports are not that history (E08). |
| J15-C13 | Unknown | Listed APC and CC BY are known; author coverage/VAT/funding/rights remain undetermined and the separate 2026 S2O change does not waive RSOS charges (J15 guide C13). |
| J15-C14 | Partial | Preprints are permitted, but author-approved submission declarations and exclusivity are unprepared; resolve AI policy before investing in final publication files (E06, E08). |

### J16 — PeerJ Computer Science

[Criteria and subsidiary requirements](../journals/J16-peerj-computer-science.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J16-C02 | Partial | Research Article fits if the benchmark’s original insight and rigorous methods are foregrounded; document substantive human scientific ownership (E02, E08). |
| J16-C03 | Partial | Abstract is 194 words/1,434 characters and title 98 characters, within 500/3,000/250 caps; an overall research-word ceiling remains unverified (E01). |
| J16-C04 | Fail | Author cover page and line numbers are absent; A4/10-point layout differs from US Letter, 2.5-cm margins and 12-point Times instructions (E01, E08). |
| J16-C05 | Partial | LaTeX PDF plus complete sources are supported; adapt to the official template and package every dependency rather than assuming the generic article layout is finished (E01, E06). |
| J16-C06 | Fail | Required author–year citations and author/year/title reference ordering differ from current numeric plain output (E07). |
| J16-C07 | Fail | The single 41,789,224-byte ZIP exceeds the 30-MB individual supplementary cap, although below the 50-MB total; split or use a suitable archive and prepare separate figures/tables (E06–E07). |
| J16-C08 | Fail | Code/data are accessible, but the required DOI software-archive route is missing for social-platform-hosted software; confirm any applicable direct-supplement alternative and license the release (E06). |
| J16-C09 | Partial | Invalid observations and diagnostics are preserved; emphasize descriptive estimands because conditional bootstrap probabilities do not guarantee robust population inference (E03–E05). |
| J16-C10 | Fail | Qualifying human authors/coauthor confirmations and actual affiliations/funding/conflicts/ethics declarations are missing (E08). |
| J16-C11 | Fail | Required tool/version/how/why disclosure is absent; linked T&F first-draft restrictions create a substantive eligibility hold, not an automatic exception for a computational study (E08–E09). |
| J16-C12 | Fail | The required identified-author cover page is missing; optional review-history publication/reviewer signing need real author decisions, not claims about these AI reports (E08). |
| J16-C13 | Unknown | CC BY is specified but current CS APC/membership fees were unreadable; actual funding and rights decisions remain unresolved (J16 guide C13). |
| J16-C14 | Partial | No routine cover letter is needed, but actual author submission, coauthor confirmation, prior-posting disclosure and exclusivity remain to be completed (E06, E08). |

### J17 — EPJ Data Science

[Criteria and subsidiary requirements](../journals/J17-epj-data-science.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J17-C01 | Partial | Generative models trained on human traces are in scope, but the current paper does not establish an insight into human/social systems (E02, E05). |
| J17-C02 | Partial | Regular Article would need substantive new social/system insight; standard-method description alone does not establish the scope threshold, and cultural mechanisms must not be invented (E02, E05). |
| J17-C03 | Partial | The 194-word abstract meets 150–250; no regular-article main-text ceiling was verified, so complete compliance cannot be certified (E01). |
| J17-C04 | Fail | Required title/correspondence, 3–10 keywords, abbreviation list and Declarations headings are absent from the current package (E01, E08). |
| J17-C05 | Partial | LaTeX/editable sources are accepted; double spacing and line numbers need adaptation, with a recommended Springer template rather than an invented mandatory class (E01). |
| J17-C06 | Partial | Current bibliography has relevant primary sources; formal URL/data citations and exact journal/template style remain to be checked (E02, E07). |
| J17-C07 | Fail | The current 41.8-MB ZIP exceeds 20 MB per supplement; split and cite supplements individually. Vector plots must also be checked against 10-MB/300-word-legend caps (E06–E07). |
| J17-C08 | Fail | The package lacks the required recognized-repository/supplement deposit, archive identifier and explicit software license; personal-site-only availability does not meet this criterion (E06). |
| J17-C09 | Partial | Transparent geographic statistics are useful, but they do not identify social mechanisms; robust local inference is further constrained by post hoc grouping and tail failure (E03–E05). |
| J17-C10 | Fail | Required human correspondence and availability/conflict/funding/contribution/acknowledgment Declarations are not completed (E08). |
| J17-C11 | Fail | Substantive AI preparation is not documented in Methods; current Gemini protocol and AI-review statement omit actual assistant text/code/analysis roles (E08–E09). |
| J17-C12 | Fail | Single-anonymous review requires visible author identity; the current unassigned author field and missing correspondence fail that submission requirement (E08). |
| J17-C13 | Unknown | Listed APC/currency/license options exist; current acceptance-date rate, taxes, waivers, funder compatibility and author agreement remain unconfirmed (J17 guide C13). |
| J17-C14 | Partial | Author submission and a cover letter covering fit/policy/conflicts/approvals/exclusivity are not prepared; disclose public posting without overstating social implications (E06, E08). |

### J18 — Data Science Journal

[Criteria and subsidiary requirements](../journals/J18-data-science-journal.md).

| Criterion | Status | Reason and evidence |
|---|---|---|
| J18-C02 | Partial | Research Paper is plausible; explain a transferable measurement/provenance lesson rather than presenting CSV storage, software stack or scale as novelty (E02, E06). |
| J18-C03 | Partial | The 194-word abstract meets 250; the 8,000-word ceiling includes references and needs a reproducible journal-specific full count rather than generic PDF pagination (E01). |
| J18-C04 | Partial | Logical research sections exist; full human-author title page is absent, optional keywords can be added, and final house style remains to be applied within initial flexibility (E01, E08). |
| J18-C06 | Partial | Current numeric style requires final Harvard author–year conversion with alphabetic order/DOIs; initial flexibility should not be mistaken for an immediate format rejection (E07). |
| J18-C07 | Partial | Separate vector inputs exist; prepare compliant 20-MB-or-smaller figures and use 300+ dpi or accepted vector EPS to satisfy the conflicting minimum-resolution wording (E07). |
| J18-C08 | Fail | Required dataset/source-code DOI is absent, despite public access to all observations and code; archive and authorize an explicit reuse license (E06). |
| J18-C09 | Partial | The benchmark documents exclusions and reproducibility well; transferable data-validity claims must distinguish observed complete records from provider replication and reliable population inference (E03–E06). |
| J18-C10 | Fail | Required human authors/contributions, competing-interest statement and authentic applicable funding/ethics information are absent (E08). |
| J18-C11 | Fail | A complete preparation-assistance disclosure is absent. Current policy endpoint is unavailable and broad AI-data wording needs clarification for measured model responses; do not call genuine observations fabricated (E08–E09). |
| J18-C12 | Partial | Single-blind review requires genuine author metadata; the journal prohibition on AI-generated official reviews does not turn this clearly labeled author-side preparation report into journal peer review (E08). |
| J18-C13 | Unknown | The official page conflicts between £790 and £770; obtain the current quote plus tax/coverage and confirm author CC BY rights rather than select a price (J18 guide C13). |
| J18-C14 | Partial | Cover letter must disclose allowed public preprint links; exclusive submission and real author/rights-holder approvals remain unprepared (E06, E08). |

## Venue adaptation decision

For **Transactions in GIS**, foreground accuracy versus coherence and repeated-response variation, shorten the abstract to 150 words, add keywords/running title, complete human/AI declarations and archive/cite the release. For **PLOS ONE**, foreground technical soundness and estimates; complete CRediT/forms and resolve the conflicting LaTeX/format-free instructions before packaging figures. For **TMLR**, lead with the general evaluation lesson, use its mandatory template and anonymous archive, resolve the detailed AI policy, and obtain real author approval for CC BY/OpenReview submission.

**Scientific Reports** is a reasonable broad-science alternative after a main/supplement split; **Computational Linguistics Short Paper** is a conditional specialist route. **IJGIS/CaGIS/Spatial Cognition & Computation/RSOS/PeerJ** have useful scope but substantive policy holds. **JAIR/AIJ/TACL** need a sharper specialist significance case. **Data Science Journal** needs a research-data contribution, DOI and current policy clarification. **CEUS/Applied Spatial Analysis and Policy/AI & SOCIETY/EPJ Data Science** remain lower priorities because the present evidence does not supply their defining applied/social contribution.

Choose one venue and prepare a truthful package. This review neither submits the work nor authorizes fees, invented authorship, concealed preparation history or concurrent journal consideration.
