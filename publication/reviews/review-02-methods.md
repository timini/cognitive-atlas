# Publication-readiness review 02 — Methods and statistics

**Verdict: major revision before submission. No venue is ready for immediate upload.** The strongest defensible paper is a descriptive, reference-controlled study of three fixed instruction conditions. Its numerical record and geometric checks are transparent, but the regional inferential display is stronger than its diagnosed finite-sample reliability warrants. Human authorship, full AI-preparation disclosure, reuse licensing and a venue-specific package remain unresolved. Several otherwise suitable venues have specific AI-drafting eligibility conflicts.

Reviewed 9 September 2026: manuscript/PDF at `5f9bdaa3641f684708ad914a721eecc25835ab64`, against the current `publication/review-inputs.json` and all 18 journal guides. Only the **100-capital English/Arabic/written-Chinese Gemini 3.5 Flash** collection is assessed. This is an **internal, author-requested AI-assisted readiness review**, not a journal-appointed report or independent human scientific assessment. I did not read the other four publication reviews. No journal submission or editorial contact was made.

I read the manuscript and all 14 criteria for all 18 venues, verified every current review-input hash, and successfully reran `python -m paper.revision100.verify`. I also inspected the generated regional table, validation record and release manifest. This was not a fresh rerun of every expensive randomization or an independent proof of the entire collector. The previously recorded 84 software tests are implementation evidence, not statistical calibration or human review. The public reproduction ZIP is **41,789,224 bytes** and includes code/data; the repository is also public on 9 September 2026, making the frozen paper’s privacy wording stale. The revised PLOS guide’s conflicting initial-submission/LaTeX instructions are incorporated below.

## Prioritized scientific findings

**S1 — Preserve the fixed-condition interpretation (major; all C09, especially J07/J08/J10/J13).** `main.tex:47–51` specifies one alias, one date, one assistant-authored/unvalidated wording per language, English entity names and tightly clustered requests. Arabic/Chinese additionally explain shortest surface distance. The caveats at 98, 209 and 211 are appropriate. Within-pair resampling does not create independent language, translation, date or model replications. Concurrent collection avoids complete separation of dates by condition, but does not remove condition-specific routing, temporal dynamics or phrasing. Claims about language itself would need human-reviewed alternative translations, localized-name factors, randomized/interleaved requests and independently repeated collection blocks. That is future research, not evidence already collected or a universally mandatory formatting prerequisite.

**S2 — State rejection conditionally on exchangeability (major; all C09).** Lines 94–98 correctly specify the strong null: equality of within-pair response distributions under independent requests. Different dispersion alone can reject it; a geometric test statistic does not turn this into a population-median-map null. Preserve that distinction. However, the assertions that tests “reject” or “establish departures” at 159 and 168 should carry the independence/exchangeability qualification already admitted at 51: *under the assumed within-pair exchangeability model, observed statistics exceed the shuffled baseline*. Pooling does not establish exchangeability, and common provider disturbances can couple cells. Observed shifts remain valid descriptive quantities; conditional p-values are not unconditional language effects. Six distance tests and three map tests have separate Holm corrections, not study-wide control. Zero exceedances indicate Monte Carlo resolution, not exact underlying probabilities.

**S3 — Retain local estimates; demote their hypothesis-test display (major; all C09, particularly J13/J14).** Lines 101–105 correctly distinguish single-response error from global pair-median MAE, and 182–197 distinguish an Arabic smaller disadvantage from an absolute benefit. The main table at 189 nevertheless displays decisive-looking p-values from a method whose equal-mean rare-tail diagnostic has only 3.3–7.5% coverage and 100% familywise rejection (263). The variance correction at 259 repairs a second moment, not missing tail support. Empirical resampling is a legitimate diagnostic; a confidence statement about an unknown response law still requires assumptions. I recommend removing the main regional p-value columns, retaining gains/interactions, and presenting empirical-resampling sensitivity in a clearly labeled supplement. At minimum, put the numerical failure beside the main table. Do not claim equivalence or evidence that local benefits are absent: say *no observed gain for these operational groups*. Beijing/Singapore are two cases, and the Arab States set is a regional proxy; neither is a universal language-affinity classifier.

**S4 — Keep geometry descriptive and in-sample (moderate; all C09, especially J01/J04/J05/J09/J10).** WGS84 inverse geodesics (44), fixed-radius arc fitting (77–81), global orthogonal spherical alignment (83), full cosine-spectrum/rank/domain diagnostics (85), reference-floor reporting without scalar subtraction (137), multiple starts (145), and distinct non-metric stress (71–75, 278) are strengths. They establish neither a global optimum nor unique latent geometry, unqueried-city prediction or intrinsic dimensionality. The manuscript correctly says so, including the Earth scree baseline (153). Stronger predictive claims would require held-out relationships or separately collected behavioral tasks. Coastline interpolation is not measured coastline knowledge, topology preservation or demonstrated perceptual utility (87). A user study or new embedding algorithm is not a universal condition for publishing this bounded result.

**S5 — Keep denominators and QC explicit (moderate; all C08/C09).** Lines 54–58 reconcile 148,500 completed slots, 148,504 attempts and 148,491 valid values; 4,948 complete pairs enter distance tests versus 4,950 in descriptions/map tests. The abstract’s “148,500 distance judgments” would be more exact as “completed responses,” or by stating accepted values once. The whole-response ASCII parser is candidly disclosed as unconstrained output, not falsely described as provider-schema generation. Preserve malformed/over-range records rather than repair or hide them. Sensitivities at 200 and 267–274 support the observed ordering and small map-shift changes, not unseen tails or all inferential claims. Ties and ten responses per cell cannot establish normality, modality or a general distinction between guessing and knowledge (125); the paper appropriately avoids those stronger assertions.

## Shared submission blockers and evidence key

**Humans and AI (C10/C11).** The author line is blank (21), and 220 says identities are unassigned. Actual humans must establish authorship/contributions, verify science/citations and complete affiliations, funding, conflicts and applicable ethics information. No account handle supplies those facts. Mentions of measured Gemini, assistant translations and ten AI reviews do not disclose the full assistant writing/coding/analysis history. T&F-affiliated J01/J04/J05/J16 and Royal Society J15 have specific restrictions; J12 discourages extensive use, J10 has policy/FAQ tension, and J18 needs current-policy clarification. Disclosure is necessary, but not proof of eligibility. Honest editorial inquiry is a recommended next action, not an inquiry made here or a promise that rewriting cures the history.

**Access, permanence and rights (C08/C13).** Lines 214–218 and the public bundle establish meaningful data/code access. Hashes are neither DOI archives nor reuse grants. No verified project-wide reuse license was found in the inspected release. J09 lacks its mandatory checklist; J16/J18 require a DOI/software archive; J17 requires a recognized repository or supplements. Other guides encourage durable deposits. Humans must approve a license after checking source/provider rights. Historical source-capture gaps at 218 cannot be erased by a new lock.

**Packaging (C03–C07/C12/C14).** The abstract has 194 whitespace-delimited words; the title has 12 words/98 characters after removing the TeX line break. Recount in the actual portal after editing. Fifteen generic pages are not publisher typeset pages. J02’s 150-word abstract cap is exceeded; J14’s eight-display cap is exceeded by four figures and six main tables. J16/J17 need supplement splitting or external deposits. Mandatory templates need actual reflow; J12 requires Word. Do not call production-only bibliography changes an initial rejection where format-free is verified; PLOS’s conflicting LaTeX-specific instructions need separate resolution. An identifying public preprint may be allowed even when identifying links in an anonymous review copy are forbidden. Single-anonymous routes need named human metadata.

## Full assessment matrices

These cover **18 journals × 14 criteria = 252 unique assessments**. Pass is artifact compliance or editorial fit judgment, not acceptance. Partial names remaining work; Fail marks a demonstrable missing requirement or policy conflict; Unknown preserves unresolved rules/author facts/eligibility. No N/A shortcuts are used. Reasons below are part of the cell evidence. Recommendations in guides are not invented mandatory statistical tests.

C01 scope; C02 contribution/type; C03 limits; C04 structure/front matter; C05 files/template; C06 references; C07 figures/supplements; C08 reproducibility; C09 inference; C10 humans/declarations; C11 AI policy; C12 review/anonymity; C13 costs/rights; C14 submission/history.

| Journal | C01 | C02 | C03 | C04 | C05 | C06 | C07 |
|---|---|---|---|---|---|---|---|
| J01 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J02 | Pass | Partial | Fail | Partial | Partial | Pass | Partial |
| J03 | Partial | Fail | Unknown | Unknown | Unknown | Unknown | Partial |
| J04 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J05 | Pass | Partial | Unknown | Partial | Unknown | Unknown | Partial |
| J06 | Fail | Fail | Partial | Fail | Partial | Fail | Partial |
| J07 | Pass | Partial | Partial | Pass | Fail | Partial | Partial |
| J08 | Pass | Partial | Partial | Partial | Fail | Fail | Partial |
| J09 | Pass | Partial | Unknown | Partial | Fail | Partial | Partial |
| J10 | Pass | Partial | Partial | Partial | Fail | Partial | Partial |
| J11 | Pass | Partial | Partial | Partial | Partial | Unknown | Partial |
| J12 | Fail | Fail | Pass | Fail | Fail | Fail | Partial |
| J13 | Pass | Partial | Partial | Partial | Partial | Partial | Partial |
| J14 | Pass | Partial | Partial | Partial | Pass | Partial | Fail |
| J15 | Pass | Partial | Pass | Partial | Pass | Partial | Partial |
| J16 | Pass | Partial | Pass | Fail | Partial | Fail | Fail |
| J17 | Partial | Fail | Partial | Fail | Partial | Partial | Fail |
| J18 | Partial | Partial | Partial | Partial | Partial | Partial | Partial |

| Journal | C08 | C09 | C10 | C11 | C12 | C13 | C14 |
|---|---|---|---|---|---|---|---|
| J01 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J02 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
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
| J13 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J14 | Partial | Partial | Fail | Fail | Partial | Unknown | Partial |
| J15 | Partial | Partial | Fail | Fail | Fail | Unknown | Partial |
| J16 | Fail | Partial | Fail | Fail | Fail | Unknown | Partial |
| J17 | Fail | Partial | Fail | Fail | Fail | Unknown | Partial |
| J18 | Fail | Partial | Fail | Unknown | Fail | Unknown | Partial |

## Criterion-by-criterion reasons

The linked dated guides supply official rules and sources. Unverified rules remain open rather than receiving guessed defaults.

### J01 — International Journal of Geographical Information Science

[Guide and official sources](../journals/j01-international-journal-of-geographical-information-science.md)

- **J01-C01 — Pass.** Geographic representation and uncertainty are directly addressed (main.tex 29–38, 68–87).
- **J01-C02 — Partial.** The repeated-judgment/spherical-control contribution is plausible but needs a sharper GIScience advance over the explicitly cited reconstruction antecedent; confirm regular-article category.
- **J01-C03 — Unknown.** Current journal word, abstract and page limits were inaccessible; the 15-page generic layout cannot establish compliance.
- **J01-C04 — Partial.** The operational title and Methods/Results/Discussion structure work; add keywords and confirm unknown keyword/heading rules.
- **J01-C05 — Unknown.** Current journal-specific LaTeX and initial format-free eligibility remain unverified; retain editable TeX/PDF rather than assume publisher-wide acceptance.
- **J01-C06 — Unknown.** Exact journal bibliography rule is unknown; the manuscript uses alphabetically ordered numeric plain references (225–226).
- **J01-C07 — Partial.** Four vector plots and reference controls are available, but final-size accessibility and unknown artwork rules need inspection; coastline interpolation is correctly qualified (87, 150).
- **J01-C08 — Partial.** An availability paragraph and public code/data ZIP exist (213–218); persistent archive, formal dataset citation, licenses and anonymous review access remain unfinished.
- **J01-C09 — Partial.** Apply statistical findings S1–S5 below; the WGS84 control is particularly valuable, but conditional tests need conditional presentation and the regional p-values remain fragile.
- **J01-C10 — Fail.** Author field is blank (21), and responsible humans/affiliations/contributions/funding/conflicts are explicitly unresolved (220).
- **J01-C11 — Fail.** The recorded substantive AI drafting conflicts with the verified T&F first-draft restriction; editorial eligibility clarification and complete assistance disclosure are required, not a cosmetic rewrite.
- **J01-C12 — Fail.** Double-anonymous instructions are unmet by the identifying Pages/GitHub URLs (214) and unreviewed metadata; an empty author field does not anonymize the artifact.
- **J01-C13 — Unknown.** Exact APC, license choices, author rights and institutional/funder eligibility remain unknown.
- **J01-C14 — Partial.** Exclusivity and the publisher-hosted online-identity restriction require a candid account of the existing public paper; eligibility cannot be repaired by hiding its history.

### J02 — Transactions in GIS

[Guide and official sources](../journals/j02-transactions-in-gis.md)

- **J02-C01 — Pass.** Spatial analysis, uncertainty and visualization match the actual study rather than merely its website (34, 68–87).
- **J02-C02 — Partial.** Original research is suitable; explain how repeated responses plus spherical reference controls add knowledge beyond established MDS.
- **J02-C03 — Fail.** The 194-word abstract (26) exceeds the verified 150-word maximum; overall main-text limit remains unverified.
- **J02-C04 — Partial.** Add 5–6 keywords and a running title under 40 characters; 12-point/double-spaced presentation is preferred, distinct from free-format eligibility.
- **J02-C05 — Partial.** Free-format LaTeX submission is allowed and source exists; resolve the guide’s contradictory initial PDF-only versus source-upload wording in the live portal.
- **J02-C06 — Pass.** The current plain bibliography is consistent, satisfying the verified initial consistency rule; retain its evidence when applying any later production style.
- **J02-C07 — Partial.** Embedded numbered figures/tables and captions exist; separate figures, tables and supporting files are revision-stage work, not an initial format-free rejection.
- **J02-C08 — Partial.** Public observations/code and availability text exist; add durable data archiving and a formal shared-data citation as expected by the journal.
- **J02-C09 — Partial.** Methods are evaluable and denominators clear; S1–S5 identify remaining inference concerns under Wiley soundness expectations.
- **J02-C10 — Fail.** True author details, funding/conflicts and submitting-author ORCID are absent; no identities or declarations can be inferred from an account handle.
- **J02-C11 — Fail.** The paragraph on ten AI reviews (220) does not disclose substantive writing, code and analysis assistance; Wiley also requires human verification and suitable tool/content terms.
- **J02-C12 — Fail.** Single-anonymous review requires genuine author metadata, currently blank; there is no reason to impose double-anonymous removal here.
- **J02-C13 — Unknown.** Standard copyright and optional OA routes exist, but exact APC, agreement coverage and the authors’ rights/funder decision are unknown.
- **J02-C14 — Partial.** Prepare the Wiley Authors/Research Exchange package, disclose the public preprint/bundle, confirm journal treatment of prior posting and obtain actual exclusive-submission approval.

### J03 — Computers, Environment and Urban Systems

[Guide and official sources](../journals/j03-computers-environment-and-urban-systems.md)

- **J03-C01 — Partial.** AI/geocomputation overlap is real, but a capital-distance benchmark has no evaluated urban or environmental systems question.
- **J03-C02 — Fail.** The present empirical study lacks an evidenced urban/environmental application contribution; article taxonomy also needs live-guide confirmation.
- **J03-C03 — Unknown.** The official guide was blocked; no abstract, word or page ceiling is established.
- **J03-C04 — Unknown.** General research sections are readable, but keyword, highlights and graphical-abstract obligations are unverified.
- **J03-C05 — Unknown.** Current LaTeX class and initial-file rules were inaccessible; generic Elsevier rules cannot certify this journal’s package.
- **J03-C06 — Unknown.** Exact bibliography and initial-format flexibility are unverified; the existing consistent plain style is not proof of compliance.
- **J03-C07 — Partial.** Capital/reference plots and qualified interpolation are useful; journal-specific dimensions, resolution and supplementary-file ceilings remain unknown.
- **J03-C08 — Partial.** The public ZIP and availability section establish access, but the journal data tier, permanent deposit, formal citations and reuse terms remain unresolved.
- **J03-C09 — Partial.** S1–S5 apply; no routing, navigation or decision-impact validation is claimed or demonstrated, and an applied reinterpretation would require new evidence.
- **J03-C10 — Fail.** Elsevier requires accountable human authors and truthful declarations; the manuscript expressly leaves identity unresolved (21, 220).
- **J03-C11 — Fail.** Full manuscript-assistance disclosure before references and research/code assistance in Methods are missing; measured Gemini responses do not disclose assistant preparation.
- **J03-C12 — Unknown.** The current journal-specific review anonymity model was not verified; prepare separable identity metadata only after confirming the portal.
- **J03-C13 — Unknown.** Subscription/OA support is known, but exact charges, licenses and author eligibility remain unverified.
- **J03-C14 — Partial.** Elsevier permits preprints generally; disclose the current PDF, verify journal-specific files, exclusivity and author approval rather than assume portal completion.

### J04 — Cartography and Geographic Information Science

[Guide and official sources](../journals/j04-cartography-and-geographic-information-science.md)

- **J04-C01 — Pass.** The measured geometry versus displayed map distinction directly fits cartographic and GIScience audiences (83–87, 150).
- **J04-C02 — Partial.** Original research is plausible; strengthen the contribution as an evaluation of geographic reconstruction, without claiming unmeasured user comprehension.
- **J04-C03 — Unknown.** Current article/abstract limits were not retrieved; generic 15-page pagination is not a compliance assessment.
- **J04-C04 — Partial.** The title and operational interpretation are suitable; keywords, abstract shape and exact headings need confirmation.
- **J04-C05 — Unknown.** Journal LaTeX/template and format-free eligibility remain unknown, despite existing working TeX/PDF.
- **J04-C06 — Unknown.** Exact house reference style remains unverified; preserve the original method and geographic-source citations when converting.
- **J04-C07 — Partial.** Interactive displays and free color are supported, but rights and accessibility checks remain; use the unwarped reference and capital plots, not coastline appearance as measured evidence.
- **J04-C08 — Partial.** Public raw data/code are accessible; current sharing tier, persistent archive, licenses and anonymous deposit route remain unresolved.
- **J04-C09 — Partial.** S1–S5 apply; the paper appropriately admits mesh folds/topology changes and does not establish perceptual utility (87).
- **J04-C10 — Fail.** Human authors, contributions and declarations remain absent (21, 220), with geographic-source reuse responsibility still requiring human confirmation.
- **J04-C11 — Fail.** T&F’s first-draft restriction conflicts with substantial assistant drafting; eligibility and detailed tool/version disclosure must be resolved honestly.
- **J04-C12 — Fail.** Double-anonymous review is not satisfied by identifying URLs in 214 and unvetted artifact metadata.
- **J04-C13 — Unknown.** Hybrid/Open Select is verified, but current APC and author rights/funding choices are unknown; free color does not mean free OA.
- **J04-C14 — Partial.** ScholarOne is the stated route; precise preprint/package exceptions and author approvals remain unresolved and existing public dissemination must be declared.

### J05 — Spatial Cognition & Computation

[Guide and official sources](../journals/j05-spatial-cognition-and-computation.md)

- **J05-C01 — Pass.** Spatial cognition and crosslinguistic spatial expression closely match the operational question (29–38).
- **J05-C02 — Partial.** An empirical paper is plausible; make the behavioral inference contribution explicit and avoid treating a fitted sphere as a stored neural representation.
- **J05-C03 — Unknown.** Current word/page/abstract limits remain inaccessible and therefore unknown.
- **J05-C04 — Partial.** Operational cognitive-map language is careful; add keywords and preserve exploratory status, with exact journal count/structure still unknown.
- **J05-C05 — Unknown.** Current journal LaTeX acceptance/template is unverified; general T&F files do not establish compliance.
- **J05-C06 — Unknown.** Exact citation style is unknown; existing antecedents are relevant but the theoretical spatial-knowledge discussion could be more discriminating.
- **J05-C07 — Partial.** Reference controls and residual plots exist; artwork specifications and final accessible encodings remain unchecked.
- **J05-C08 — Partial.** Public raw outputs, prompts and executable analysis exist; sharing tier, persistent identifier, licenses and review-access route remain unresolved.
- **J05-C09 — Partial.** S1–S5 apply, particularly wording confounding and absence of behavioral transfer or human-comparison evidence; these limit interpretation rather than invalidate descriptive geometry.
- **J05-C10 — Fail.** No accountable human author/declaration record exists; model queries alone are not evidence that human-participant ethics approval is applicable.
- **J05-C11 — Fail.** T&F drafting restriction creates an eligibility hold; disclosure of the true extensive preparation history is necessary but not established as sufficient.
- **J05-C12 — Unknown.** Anonymous referees are stated, but author-anonymity mode was not verified; do not infer double-anonymous rules.
- **J05-C13 — Unknown.** Open Select exists; current APC, licenses, incidental fees and author coverage remain unknown.
- **J05-C14 — Partial.** ScholarOne submission is known, but package/preprint exceptions and human final approval still need confirmation; disclose the public PDF.

### J06 — Applied Spatial Analysis and Policy

[Guide and official sources](../journals/j06-applied-spatial-analysis-and-policy.md)

- **J06-C01 — Fail.** The present study does not evaluate a policy decision or applied geographic outcome, the defining audience requirement.
- **J06-C02 — Fail.** Research-paper type exists, but the required applied contribution cannot be supplied by a speculative policy paragraph.
- **J06-C03 — Partial.** 194-word abstract satisfies 150–250; the normal 8,000-word limit needs an explicit count using a confirmed inclusion convention.
- **J06-C04 — Fail.** Four to six mandatory keywords are absent; current numbered headings are shallow enough but front matter needs adaptation.
- **J06-C05 — Partial.** Editable TeX exists and is permitted for mathematical work; supply complete editable sources at every submission and consider the recommended Springer template.
- **J06-C06 — Fail.** Current numeric citations conflict with author–year/alphabetic references; regenerate DOI-linked bibliography in the required style.
- **J06-C07 — Partial.** Figures/tables are numbered and captioned; prepare cited, captioned supplementary objects and verify artwork at final size.
- **J06-C08 — Partial.** Availability prose and public ZIP exist; formal statement placement, durable deposit and anonymous reviewer access require completion.
- **J06-C09 — Partial.** S1–S5 apply; no causal or policy-benefit claim is supportable without a measured decision outcome.
- **J06-C10 — Fail.** Portal author contributions, competing interests and genuine human/funding/ethics declarations are absent.
- **J06-C11 — Fail.** Substantive LLM drafting/code/translation use is not disclosed in Methods; the narrow copyediting exemption does not cover this history.
- **J06-C12 — Fail.** Double-anonymous review requires removing identifying materials; use current portal identity fields instead of blindly following older title-page language.
- **J06-C13 — Unknown.** Subscription has no APC; optional OA quote is £2,290/$3,190/€2,590 plus applicable tax, but author route/coverage and license choice remain unknown.
- **J06-C14 — Partial.** Exclusive submission and coauthor approval are required; disclose existing online dissemination and complete the live transition-era portal checklist.

### J07 — Transactions of the Association for Computational Linguistics

[Guide and official sources](../journals/J07-tacl.md)

- **J07-C01 — Pass.** The three written instruction conditions and elicited model behavior are relevant to NLP evaluation (46–51).
- **J07-C02 — Partial.** Original empirical evaluation is plausible; technical significance beyond earlier distance/MDS work needs sharpening without inventing an algorithmic advance.
- **J07-C03 — Partial.** Reflow before testing the ten-main-page limit and separate five replication/three complementary appendix allowances; the current generic 15 pages prove neither pass nor failure.
- **J07-C04 — Pass.** Title, operational definition and research sections are adequate; 5–10 editorial-comment keywords are optional, not a missing mandatory manuscript element.
- **J07-C05 — Fail.** The generic article class is not the mandatory TACL template; rebuild and inspect fonts/metadata, retaining publication LaTeX source.
- **J07-C06 — Partial.** Use the supplied ACL bibliography style while preserving primary antecedents and the behavioral/activation distinction.
- **J07-C07 — Partial.** Appendices follow references and are referenced, but must be anonymized and are not reviewed; key rare-tail diagnostics cannot rely only on the appendix. Resolve conflicting external-link guidance.
- **J07-C08 — Partial.** Promised artifacts already exist publicly; prepare permitted anonymous reviewer access, a persistent citation and reusable licenses without identifying URLs.
- **J07-C09 — Partial.** S1–S5 apply; one unvalidated wording per written language is not multilingual mechanism identification and clustered requests do not prove independence.
- **J07-C10 — Fail.** Complete actual human coauthor profiles and private declarations; identity and scientific responsibility are expressly unassigned.
- **J07-C11 — Fail.** ACL content-assistance acknowledgments are absent; disclose actual drafting, coding, analysis, translations and these preparatory reviews under human responsibility.
- **J07-C12 — Fail.** Anonymous submission is currently defeated by account-associated URLs (214); removal of the prior anonymity period does not allow identifying links in the review PDF.
- **J07-C13 — Unknown.** No submission/publication charge and immediate OA are verified; actual publication agreement, artifact rights and human consent remain unresolved.
- **J07-C14 — Partial.** Check exclusive archival review, actual submission history, applicable nine-month ACL-family and twelve-month TACL rejection exclusions, and portal metadata before upload.

### J08 — Computational Linguistics

[Guide and official sources](../journals/J08-computational-linguistics.md)

- **J08-C01 — Pass.** Language-model elicitation is an appropriate CL topic if presented as model evaluation rather than human language processing.
- **J08-C02 — Partial.** A Short Paper is a reasonable route for the bounded result; a stronger linguistic lesson is needed before claiming a broad theory.
- **J08-C03 — Partial.** Current 15 generic pages do not establish fit to the typical 20 initial/25 final Short Paper pages; reflow in CL class. No independent abstract ceiling verified.
- **J08-C04 — Partial.** English and abstract are present; separate title/author/abstract metadata and 5–10 editorial keywords remain to be supplied.
- **J08-C05 — Fail.** LaTeX exists but the mandatory current clv2025 class has not been used; rebuild PDF and ensure exact multilingual prompts remain accessible.
- **J08-C06 — Fail.** Use required CL citation/reference files rather than the current plain bibliography.
- **J08-C07 — Partial.** Editable plots and self-contained figure captions exist; supplement-size limits remain unverified and must be checked before uploading the ZIP.
- **J08-C08 — Partial.** Promised data/code are publicly downloadable in the ZIP and now-public repo; persistent citation and actual output/code reuse terms remain unresolved.
- **J08-C09 — Partial.** S1–S5 apply; do not retrofit native-speaker approval or temporal replication into this dataset, and retain the failed diagnostic visibly.
- **J08-C10 — Fail.** Mandatory full names, affiliations and emails are missing; funding/contributions/conflicts need actual human completion.
- **J08-C11 — Fail.** ACL requires disclosure of generated content assistance in acknowledgments; current translation/review mentions are incomplete for assistant-written research and prose.
- **J08-C12 — Fail.** Single-blind submission requires author names/affiliations on page one; the blank author field is noncompliant.
- **J08-C13 — Unknown.** Immediate OA is known and the checklist requests ability to assign copyright to ACL; current exact fee/license agreement and authors’ ability to agree remain unknown.
- **J08-C14 — Partial.** Complete original-submission declarations, true prior/conference publication history, exclusivity and unrestricted-review assurances; a public preprint is not a journal publication.

### J09 — Journal of Artificial Intelligence Research

[Guide and official sources](../journals/J09-jair.md)

- **J09-C01 — Pass.** Accuracy versus global consistency is relevant to AI evaluation and knowledge representation.
- **J09-C02 — Partial.** A full Article fits the analyses, but general AI significance beyond a single-model application of established methods is not yet compelling enough.
- **J09-C03 — Unknown.** Concision is advised; a strict article/abstract maximum was not verified, so neither unlimited length nor compliance is established.
- **J09-C04 — Partial.** A structured abstract is encouraged, not compulsory; current sections are readable but final heading/Figure/Table capitalization and section introductions need style adaptation.
- **J09-C05 — Fail.** JAIR-formatted PDF is required initially; current generic article is noncompliant. Retain source archive/PDF for final preparation.
- **J09-C06 — Partial.** Regenerate in JAIR style; published antecedents already appear, with final preference for published versions over technical reports.
- **J09-C07 — Partial.** Test plots in monochrome; online appendices are outside review, so decisive diagnostics belong in PDF. Final online code needs the journal release form.
- **J09-C08 — Fail.** The mandatory reproducibility checklist is absent from the submission PDF, a verified desk-rejection trigger, despite substantial public reproduction materials.
- **J09-C09 — Partial.** S1–S5 apply; the reference control and full-spectrum diagnostics support technical care but cannot establish stationary independent provider draws.
- **J09-C10 — Fail.** Genuine human authors and core scientific contribution are unassigned; actual funding/conflicts and accountability remain incomplete.
- **J09-C11 — Fail.** Human-sourced core contributions and responsibility are required; no full assistance statement documents the substantial automated preparation.
- **J09-C12 — Partial.** Reviewer confidentiality is known and a named submission is recommended; prepare genuine author fields, with explicit double-anonymous status unverified.
- **J09-C13 — Unknown.** No author fees and final CC BY footer/agreement are known; actual rights and human approval to license all components remain unverified.
- **J09-C14 — Partial.** Answer the three mandatory editorial questions about importance, nearest JAIR work and prior publication; verify exclusivity/history and final-preparation timing if accepted.

### J10 — Transactions on Machine Learning Research

[Guide and official sources](../journals/J10-tmlr.md)

- **J10-C01 — Pass.** Analysis and visualization of learned-system behavior fit the stated scope.
- **J10-C02 — Partial.** An empirical article can meet the evidence-and-interest standard after claims are narrowed; an attractive atlas alone is not the finding.
- **J10-C03 — Partial.** Variable length is allowed but excess can delay review; recount after template conversion and confirm any abstract rule instead of assuming unlimited submission.
- **J10-C04 — Partial.** Literal title and main-text strong null are appropriate; template front matter is not prepared and no separate keyword rule was verified.
- **J10-C05 — Fail.** The mandatory unmodified TMLR LaTeX template has not been used; generic article PDF risks desk rejection.
- **J10-C06 — Partial.** Use template bibliography configuration and retain direct comparison to earlier numerical-distance embeddings; no reference-count ceiling was verified.
- **J10-C07 — Partial.** The 41.8-MB ZIP is below the 100-MB supplement cap but is not anonymous; supplements are discretionary, so move the rare-tail failure magnitude into main reviewed evidence.
- **J10-C08 — Partial.** Raw observations, locks, code and verification command exist; build/test an anonymous bundle and distinguish recomputation from new provider calls.
- **J10-C09 — Partial.** S1–S5 apply; reduce claim strength rather than manufacture new experiments, and do not treat shared-city pairs as independent country samples.
- **J10-C10 — Fail.** Active profiles, fixed human author list, funding/conflicts and applicable ethics information are missing; no broader-impact or ethics attestations can be invented.
- **J10-C11 — Fail.** First-page AI disclosure footnote is absent and the FAQ/editorial-policy tension over human-sourced ideas/results requires clarification given extensive assistant assistance.
- **J10-C12 — Fail.** Double-blind OpenReview submission is defeated by identifying URLs and bundle metadata; permitted public preprints must not be linked from the anonymous version.
- **J10-C13 — Unknown.** No author fees and CC BY 4.0 from submission are verified, but rights and deliberate author agreement to durable public submission remain unknown.
- **J10-C14 — Partial.** Check actual author quotas/profiles and exclusivity; no overlap with archival reviewed work, including expanded conference papers, while preprints are permitted. No author-approved portal package exists.

### J11 — Artificial Intelligence (AIJ, Elsevier)

[Guide and official sources](../journals/J11-artificial-intelligence.md)

- **J11-C01 — Pass.** The diagnostic addresses broad AI reasoning/knowledge representation and therefore has topical relevance.
- **J11-C02 — Partial.** A regular article is preferable to forcing a Research Note, but the mature general contribution is weak for this ambitious venue.
- **J11-C03 — Partial.** Editorial advice is 20–30 standard pages without a hard article cap; 4,500 applies to Research Notes, not this proposal. Current publisher abstract limit is unknown.
- **J11-C04 — Partial.** English, abstract and references are present; mandatory keyword/highlight counts remain unknown and should not be invented.
- **J11-C05 — Partial.** Existing A4 single-column PDF is usable, but 10-point text falls below the preferred 11-point guidance; elsarticle is recommended rather than a verified initial mandatory class.
- **J11-C06 — Unknown.** Current publisher reference style is inaccessible; confirm before treating plain or elsarticle defaults as compliant.
- **J11-C07 — Partial.** Existing vector plots are near publication quality, but final-resolution/accessibility checks and unknown artwork/supplement ceilings remain.
- **J11-C08 — Partial.** Availability text and public code/data exist; journal data tier is unknown, while permanent archiving and licenses remain incomplete.
- **J11-C09 — Partial.** S1–S5 apply; complete empirical evidence is present for the descriptive snapshot, not a general model or language mechanism.
- **J11-C10 — Fail.** Elsevier author ethics cannot be satisfied by an empty author line and unassigned human scientific responsibility.
- **J11-C11 — Fail.** June 2026 Elsevier policy needs manuscript assistance before references and research/code assistance in Methods; neither complete declaration is present.
- **J11-C12 — Unknown.** Current journal anonymity model was not directly verified; do not inherit another Elsevier journal’s mode.
- **J11-C13 — Unknown.** Current journal APC, subscription charges and licenses were inaccessible; author funding/rights cannot be inferred.
- **J11-C14 — Partial.** Use Editorial Manager after confirming current files; declare preprint/prior work, obtain author approval and ensure no concurrent journal review. Older editorial pages need live-portal reconciliation.

### J12 — AI & SOCIETY

[Guide and official sources](../journals/J12-ai-and-society.md)

- **J12-C01 — Fail.** The paper measures geographic judgments, not societal experience or cultural harms, so the central societal audience question is unfulfilled.
- **J12-C02 — Fail.** A Research Article needs an evidenced societal argument; a commentary recast or speculative cultural paragraph would not solve the contribution gap.
- **J12-C03 — Pass.** The 194-word abstract is within the ordinary 150–250 range; current manuscript is below the normal 10,000-word research guidance and should not be padded.
- **J12-C04 — Fail.** Mandatory 4–6 keywords are missing; preserve accessible numbered headings with at most three levels while avoiding unsupported social interpretation.
- **J12-C05 — Fail.** Journal-specific Word-only instructions override generic LaTeX mentions; the current TeX/PDF package lacks required editable DOCX.
- **J12-C06 — Fail.** Author–year/alphabetical DOI-linked style conflicts with current numeric plain citations; relevant social references should not be added merely for appearance.
- **J12-C07 — Partial.** Figures/tables are cited and captioned; prepare Online Resource supplement labels and final-size accessible static evidence.
- **J12-C08 — Partial.** Data Availability Statement substance exists via public ZIP; formal heading, persistent archive, licenses and anonymous access remain incomplete.
- **J12-C09 — Partial.** S1–S5 apply; selected city pairs and a regional proxy cannot justify statements about societies or causal linguistic disadvantage.
- **J12-C10 — Fail.** Actual contributions/competing interests belong in the portal but are unassigned; no human research ethics approval should be invented.
- **J12-C11 — Fail.** Journal-specific discouragement of LLM use beyond grammar/translation conflicts with the recorded extensive assistance; eligibility clarification plus Methods disclosure is needed.
- **J12-C12 — Fail.** Double-blind review requires anonymizing manuscript and supplements, including public account links, using current portal identity fields.
- **J12-C13 — Unknown.** Subscription has no APC; optional OA £2,390/$3,390/€2,790 plus tax and CC BY/CC BY-NC-ND are known, but author funding/license choice is unknown.
- **J12-C14 — Partial.** Declare the public academic-site manuscript, confirm eligibility before Word conversion, and obtain exclusive-submission/coauthor approval through actual forms.

### J13 — PLOS ONE

[Guide and official sources](../journals/J13-plos-one.md)

- **J13-C01 — Pass.** Original measured model behavior with objective geographic ground truth is within the broad scientific remit.
- **J13-C02 — Partial.** Research Article is suitable under soundness rather than impact criteria, conditional on resolving the fragile statistical presentation and human accountability.
- **J13-C03 — Partial.** 194-word abstract and 98-character full title meet the 300-word/250-character caps; required separate short title (100 characters maximum) has not been provided. No overall word cap applies.
- **J13-C04 — Partial.** Logical research sections exist; title page, acknowledgments, continuous lines and house double spacing remain adaptations, not format-free initial blockers.
- **J13-C05 — Partial.** General format-free guidance conflicts with the LaTeX-specific template warning and initial PDF-without-figures request. Prepare combined TeX plus separate figures and confirm portal handling; current embedded-figure PDF is not an unconditional pass.
- **J13-C06 — Partial.** Current alphabetical numeric order must become citation-order Vancouver for final style; this is not an initial format-free rejection.
- **J13-C07 — Partial.** The LaTeX route requests separate figures initially; current PDF plots need permitted TIFF/EPS conversion, 300–600 dpi or appropriate vector output, ≤10-MB files and font/accessibility checks. Do not assume all figure preparation is final-stage only.
- **J13-C08 — Partial.** Data/code availability text and public ZIP satisfy substantial access needs; confirm essential custom-code reuse terms and archive persistently with citation.
- **J13-C09 — Partial.** S1–S5 apply to the technical-validity criterion; dropping fragile regional hypothesis-test emphasis would better match the defensible evidence.
- **J13-C10 — Fail.** Actual authors, affiliations, correspondence/ORCID, CRediT and financial/conflict forms are missing; funding must be entered in the required form rather than invented acknowledgments.
- **J13-C11 — Fail.** Methods lack tools, uses, validation and affected-content disclosure for manuscript/code assistance, distinct from the measured Gemini model.
- **J13-C12 — Fail.** Author identities must be supplied; the blank title page is incomplete. Optional journal review-history publication is separate from these internal AI reviews.
- **J13-C13 — Unknown.** Listed regular APC is US$2,477 at submission-date rate with CC BY, but actual assistance/coverage, rights and author payment decision remain unknown.
- **J13-C14 — Partial.** The one-page cover letter and author-approved submission declarations are missing; disclose the permitted preprint and ensure exclusive journal submission.

### J14 — Scientific Reports

[Guide and official sources](../journals/J14-scientific-reports.md)

- **J14-C01 — Pass.** The bounded empirical geographic/AI result fits broad original science; confirm computer-science/geoscience handling category.
- **J14-C02 — Partial.** Article is the defensible type; the existing exploratory collection cannot retrospectively become a Registered Report.
- **J14-C03 — Partial.** 12-word title and 194-word abstract meet 20-word/200-word limits. Check recommended 4,500-word count with specified exclusions and publisher typeset-page convention; generic 15 pages are not decisive.
- **J14-C04 — Partial.** Unstructured abstract is present; optional/up-to-six keywords and author metadata need preparation. Suggested Results/Discussion/Methods order is not mandatory.
- **J14-C05 — Pass.** The approximately 1.1-MB combined LaTeX PDF is below the 3-MB first-submission cap; editable sources exist and recommended template conversion may follow.
- **J14-C06 — Partial.** Convert plain alphabetical reference order to Nature numbered style; 18 rendered references are below the recommended 60, which is not a hard ceiling.
- **J14-C07 — Fail.** Four main figures plus six main tables exceed eight main display items; explicitly select/move tables and separate appendix supplements. Check one-page tables and legends under 350 words.
- **J14-C08 — Partial.** Public raw data/code and availability section exist; formal statement/deposit route, persistent archiving and portfolio code/rights requirements need completion.
- **J14-C09 — Partial.** S1–S5 apply; unverified request independence is not independent replication of three language conditions.
- **J14-C10 — Fail.** Human authors/correspondence, contributions, explicit competing interests, funding and applicable ethics details are missing.
- **J14-C11 — Fail.** Methods do not document full substantive LLM assistance; dedicated current AI-policy details remain partially inaccessible and require confirmation.
- **J14-C12 — Partial.** Identified title page is absent; detailed current review-option settings remain unknown, so do not assume double-anonymous preparation.
- **J14-C13 — Unknown.** Fully OA is known; €2,490 is only the portfolio starting figure, not a confirmed journal invoice. Currency/tax/coverage and author agreement remain unknown.
- **J14-C14 — Partial.** Prepare cover letter, correspondence, fit, reviewer suggestions/exclusions and previous editorial-discussion record; check exclusivity and disclose current public posting.

### J15 — Royal Society Open Science

[Guide and official sources](../journals/J15-royal-society-open-science.md)

- **J15-C01 — Pass.** The quantitative empirical study fits science/engineering/mathematics scope.
- **J15-C02 — Partial.** Research Article and soundness-based assessment suit the bounded benchmark, but policy and inference issues prevent present readiness.
- **J15-C03 — Pass.** 194-word abstract meets the 200-word ceiling; the 2026 catalogue states no overall paper-length cap.
- **J15-C04 — Partial.** Add 3–10 keywords and genuine title-page metadata; convert residual American spellings such as kilometer to British English, maintaining SI units.
- **J15-C05 — Pass.** Format-free initial LaTeX PDF is allowed; later flatten main-text inclusions and supply all editable compilation files.
- **J15-C06 — Partial.** Final Vancouver citation-order references and formal data/code identifiers require adaptation, not an initial format-free rejection.
- **J15-C07 — Partial.** The 41.8-MB ZIP is under the 350-MB per-supplement limit; later source figures/tables and CC BY support-material permissions need completion.
- **J15-C08 — Partial.** Underlying data/code are public but no verified CC0/CC BY reuse grant is supplied; required openness includes licensing, not just downloads.
- **J15-C09 — Partial.** S1–S5 apply under soundness criteria; retain the zero-exceedance Monte Carlo resolution and rare-tail failure without overstating confirmatory inference.
- **J15-C10 — Fail.** Submitting-author ORCID, qualifying humans, contributions, funding and competing interests are absent.
- **J15-C11 — Fail.** Restricted readability/language assistance and no AI substitution for scientific interpretation conflict with extensive preparation; editorial clarification and full affected-elements disclosure are essential.
- **J15-C12 — Fail.** Single-anonymous review requires identified authors; eventual mandatory journal review-history publication is not satisfied by these author-commissioned reports.
- **J15-C13 — Unknown.** APC £1,400/US$1,960/€1,680 plus VAT and CC BY are known; author funding/waiver/rights decisions remain unknown, and RSOS does not gain the 2026 S2O fee exemption.
- **J15-C14 — Partial.** Preprints are allowed but must be accurately reported; the author-approved declarations and exclusive submission through the actual journal system are not prepared.

### J16 — PeerJ Computer Science

[Guide and official sources](../journals/J16-peerj-computer-science.md)

- **J16-C01 — Pass.** Empirical model evaluation and reusable computation fit a CS readership when the website is not claimed as the scientific result.
- **J16-C02 — Partial.** A Research Article is appropriate but correctness and original insight need the bounded scientific framing and human ownership discussed below.
- **J16-C03 — Pass.** 194-word abstract is below 500 words and 3,000 characters; 98-character title is below 250. No verified overall research-word cap is asserted.
- **J16-C04 — Fail.** Current A4/24-mm/10-point layout lacks required author cover page, US Letter/2.5-cm/12-point Times presentation and line numbering.
- **J16-C05 — Partial.** LaTeX is supported and source/PDF exist; package the complete source using official template and verify final layout rather than treating current class as ready.
- **J16-C06 — Fail.** Author–year references sorted by author/year/title conflict with the current numbered plain citations.
- **J16-C07 — Fail.** 41,789,224-byte ZIP exceeds the 30-MB individual supplement cap although below 50-MB total; split intelligently or archive externally and separate figures/tables.
- **J16-C08 — Fail.** Data/code access exists but the software archive DOI requirement is not met; confirm any applicable machine-readable supplementary-code route and license the actual release.
- **J16-C09 — Partial.** S1–S5 apply; raw exclusions are preserved, but bootstrap significance must not be represented as robust population inference.
- **J16-C10 — Fail.** Qualifying human authors, confirmed coauthorship, affiliations and actual funding/conflict/ethics declarations are missing.
- **J16-C11 — Fail.** PeerJ requires tool/version/how/why disclosure and points to T&F drafting restrictions; extensive assistance requires eligibility clarification, not a proofreading label.
- **J16-C12 — Fail.** An identified author cover page is required and absent; optional signed reports or published journal history are separate choices from these AI assessments.
- **J16-C13 — Unknown.** CC BY is verified, but current pricing could not be read and APC/membership/coverage decisions remain unknown rather than zero.
- **J16-C14 — Partial.** No routine cover letter/inquiry is required; actual author submission and coauthor confirmation are still missing, with preprints disclosed and duplicate/concurrent publication avoided.

### J17 — EPJ Data Science

[Guide and official sources](../journals/J17-epj-data-science.md)

- **J17-C01 — Partial.** Generative models are explicitly in scope, but the current paper does not explain human/social systems beyond a descriptive behavior snapshot.
- **J17-C02 — Fail.** The required substantive human/social-system insight is not established by standard methods on one model’s distances; do not fabricate cultural conclusions.
- **J17-C03 — Partial.** 194-word abstract meets 150–250; no numerical main-text ceiling was verified, so final length judgment remains open.
- **J17-C04 — Fail.** Mandatory human title page, 3–10 keywords, abbreviation list and required Declarations headings are absent.
- **J17-C05 — Partial.** Editable LaTeX is accepted and exists; add double spacing and line/page numbers and consider the recommended template.
- **J17-C06 — Partial.** Data identifiers/URLs need formal citations; confirm the exact bibliography style against the article template rather than assume current plain output.
- **J17-C07 — Fail.** 41.8-MB ZIP exceeds 20-MB per-supplement ceiling; split or use a recognized archive. Figures must be at most 10 MB and legends at most 300 words.
- **J17-C08 — Fail.** Recognized repository or supplements are required rather than personal-site-only hosting; current Pages lacks archive identifier and explicit software license despite real public access.
- **J17-C09 — Partial.** S1–S5 apply; robust descriptive checks do not provide the additional societal insight demanded by scope.
- **J17-C10 — Fail.** Required availability/conflict/funding/contribution/acknowledgment declarations and responsible human author/correspondence fields are missing.
- **J17-C11 — Fail.** Full substantive LLM use is not documented in Methods; human responsibility and exclusion of AI authors must be reflected accurately.
- **J17-C12 — Fail.** Single-anonymous review keeps author identities visible, but the manuscript leaves them unassigned.
- **J17-C13 — Unknown.** APC £1,340/US$1,990/€1,690 at acceptance-date rate plus taxes and listed license choices are known; funder compatibility and actual author choice remain unknown.
- **J17-C14 — Partial.** Human author submission and cover letter covering fit, issues, conflicts, all-author approval/exclusivity and public preprint history are not ready.

### J18 — Data Science Journal

[Guide and official sources](../journals/J18-data-science-journal.md)

- **J18-C01 — Partial.** Research-data creation, access and reuse are relevant, but the current article foregrounds geographic findings rather than a general data-methodology contribution.
- **J18-C02 — Partial.** Research Paper is plausible after an evidenced benchmark/provenance framing, without describing storage choice or website deployment as novelty.
- **J18-C03 — Partial.** 194-word abstract is below 250; formally count the 8,000-word total including references before certifying research-article length.
- **J18-C04 — Partial.** Logical sections and optional-keyword flexibility help, but a genuine full author title page and eventual house style remain incomplete.
- **J18-C05 — Partial.** Initial PDF is accepted and TeX can accompany it; confirm the final editable-format route before declaring the full package compliant.
- **J18-C06 — Partial.** Harvard author–year/alphabetical DOI-linked style requires conversion from current numeric citations, at the journal’s permitted style stage.
- **J18-C07 — Partial.** Separate figures must be at most 20 MB; use vector EPS or at least 300 dpi to satisfy the stricter of conflicting resolution guidance, retaining informative captions.
- **J18-C08 — Fail.** Explicit dataset/source-code DOI requirement is unmet: public Pages and hashes provide access/version checking but no permanent repository identifier.
- **J18-C09 — Partial.** S1–S5 apply; provenance gaps are openly disclosed and should become methodological lessons rather than erased historical uncertainty.
- **J18-C10 — Fail.** Real human authors/contributions, competing interests and applicable ethics/funding statements are missing.
- **J18-C11 — Unknown.** Current Ubiquity policy endpoint was inaccessible and indexed wording needs clarification for observed LLM outputs; preparation disclosure is incomplete, but data-policy eligibility cannot be decided from ambiguous wording.
- **J18-C12 — Fail.** Single-blind review needs actual named humans; the journal’s ban on AI-generated commissioned reviews does not turn these author-side reports into journal reviews.
- **J18-C13 — Unknown.** CC BY is known but official prices conflict (£790 table versus £770 prose); obtain a written quote and confirm human rights/funding instead of choosing a number.
- **J18-C14 — Partial.** Disclose allowed web/preprint versions with a cover-letter link, obtain rights-holder/all-author approval and exclusive-submission confirmation; these facts cannot be fabricated.

## Relative venue choices and action order

My first preparation choices are **Transactions in GIS (J02)** for geographic uncertainty, **PLOS ONE (J13)** for bounded soundness-led evidence, and **TMLR (J10)** for learned-system behavior if its human-contribution/policy questions are resolved. **Scientific Reports (J14)** is a broad alternative after reducing displays; **Computational Linguistics (J08)** is a plausible focused Short Paper if the linguistic evaluation contribution is sharpened without inflating claims.

**Spatial Cognition & Computation (J05)** and **CaGIS (J04)** are strong topical matches on policy hold. **IJGIS (J01)** adds public-identity eligibility and a demanding contribution threshold. **TACL (J07), JAIR (J09), AIJ (J11)** need a clearer general lesson than record volume. **RSOS (J15)** and **PeerJ CS (J16)** are relevant but have material preparation-policy holds. **Data Science Journal (J18)** is conditional on data-methodology framing, DOI and policy clarification. **CEUS (J03), Applied Spatial Analysis and Policy (J06), AI & SOCIETY (J12), EPJ Data Science (J17)** are weak immediate targets without real urban/policy/social-system evidence. Do not manufacture that evidence in prose. These are relative judgments, not acceptance probabilities.

First establish accountable humans and assistance history; then revise S2/S3 around the descriptive claim; complete a licensed persistent release and citations; clarify unresolved eligibility for the selected venue; prepare one journal’s actual files, abstract, figures, review identity treatment, cover letter/forms and author approvals. Have a human statistical reader and qualified Arabic/Chinese readers assess the claim and prompt record before submission. Later language review cannot retroactively change collected wording. Preserve the frozen paper and identify the eventual submission version separately.

No manuscript, guide, observation or scientific measurement was changed. The [machine-readable 252-cell assessment](review-02-methods.json) records the same dispositions for coverage verification.
