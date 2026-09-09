# Publication review 1 — scientific and editorial readiness

**Final assessment: major revision and author/policy clearance before any submission.**

Independent AI-assisted publication-review simulation, prepared on 9 September 2026. This is not a journal decision or human peer review. The manuscript reviewed is `paper/main.tex` and its 15-page PDF at source commit `5f9bdaa3641f684708ad914a721eecc25835ab64`. Only the 100-capital English, Arabic, and written-Chinese study is considered. I did not read the other four new publication reviews.

The strongest publishable result is the coexistence of accurate global distance ordering and imperfect metric consistency, supported by spherical reconstruction and an ellipsoidal-distance reference control. The paper has credible descriptive content and unusually transparent implementation evidence. It is not yet a submission-ready package. Its multilingual findings are fixed-prompt observations; a large request count does not replace independent language/wording/date replication.

## Evidence ledger

References below are to the frozen `paper/main.tex` unless otherwise stated.

- **E1 — title and metadata:** lines 20–27; author field empty, no affiliations or corresponding author, unstructured abstract with 194 whitespace-delimited tokens. The line count is a reproducible source count, not a journal-certified word count.
- **E2 — contribution and scope:** lines 29–38; prior prompted-distance MDS work is acknowledged, cognitive-map terminology operationalized, and exploratory status stated.
- **E3 — design:** lines 40–58; 100 purposively selected capitals, WGS84 geodesics, one model alias, three translations, ten temporally clustered calls per pair, unvalidated translations with English entity names, explicit parsing and QC flow.
- **E4 — geometric methods:** lines 60–87; median matrices, all triangle tests, metric/non-metric reconstruction, sphere and Procrustes methods, reference controls, coastline artifacts separated from measurements.
- **E5 — inferential target:** lines 89–105; strong response-distribution exchangeability null, separate multiplicity families, post hoc unequal operational groups, conditional bootstrap and its limits.
- **E6 — results and communication:** lines 107–203; effect sizes precede significance, distinct estimands identified, metric and geometric evidence quantified. Four figures, ten floating tables and one long capital table appear across manuscript and appendices.
- **E7 — interpretation:** lines 203–224; limitations and future replication design explicit; main conclusion stays at observed behavior and distributional departures.
- **E8 — public evidence and provenance:** lines 213–220; public source/data reproduction package, stale private-repository wording, no archival DOI, historical provenance gaps disclosed, ten AI reviews disclosed. `paper/VALIDATION.md` records local test and numerical checks. No root `LICENSE` file is present.
- **E9 — statistical failure diagnosis:** appendix lines 261–267; empirical bootstrap's rare-tail stress scenario has 3.3–7.5% associated-gain coverage and 100% familywise rejection. Disclosure is strong; the resulting local intervals still require editorial restraint.
- **E10 — presentation and declarations:** generic 10-point A4 article class and `plain` bibliography; no journal template, keywords, cover letter, competing-interest statement, funding statement, named contributor statement or detailed AI-writing/code-assistance declaration in the manuscript. Their absence is observable; the underlying funding/conflicts/authorship facts are unknown and must be supplied by the authors.

## Assessment convention and scope

I read all 18 frozen journal guides and the shared assessment protocol; policy sources and access limitations are linked in each guide. I separately rechecked the [T&F drafting restriction](https://authorservices.taylorandfrancis.com/editorial-policies/using-ai-in-your-research-and-manuscript-preparations/), [PLOS publication criteria](https://journals.plos.org/plosone/s/criteria-for-publication), and [TMLR acceptance criteria](https://jmlr.org/tmlr/acceptance-criteria.html) on 9 September 2026. No journal was contacted, and I did not certify inaccessible rules.

Verified manuscript SHA-256: `7fc248a6d19bb09ae2070e734295bb8ded6a8854ed79694122649e47f75cdd26`; PDF SHA-256: `70032fc564431a245928d4f54bc464593164c639ad6e62a6699440f3cf825ceb`. Local file sizes checked: PDF 1,108,680 bytes; reproduction ZIP 41,789,224 bytes. The frozen guide hashes are in `publication/review-inputs.json`.

**Pass** means the applicable inspected criterion is satisfied; scope and contribution passes are my editorial judgments. **Partial** names an incomplete adaptation or scientific concern. **Fail** marks an observed unmet rule, an explicit preparation-policy conflict, or a labeled editorial fit failure. **Unknown** means policy or author facts cannot be established. A category may contain a known passing subrule and an unresolved subrule; the aggregate remains Unknown. The detailed ledger below explains this rather than silently treating unknown policies as permission. No entire category is N/A; human-participant approval itself appears inapplicable to API queries, but human authors must determine and declare the actual ethics context.

Initial submission is distinguished from final production style; conflicting format-free and LaTeX-specific guidance remains unresolved. The ZIP and now-public repository provide code and observations; the frozen paper’s private-repository wording is stale (live GitHub check, 9 September 2026). An archive identifier, reuse permission and author agreement remain separate questions. Missing declarations do not prove misconduct or undisclosed conflicts; the underlying facts are unknown. Policy holds below are not permission to erase preparation history.

## Prioritized editorial findings

### 1. Establish a real submission author and a truthful preparation record — submission blocker

The author line is empty and the manuscript explicitly says author identities remain unassigned (E1/E8). Named human responsibility, contributions and approval cannot be replaced by tests or AI reviews. Before any venue-specific submission, the actual contributors must determine qualifying authorship, verify the scientific argument, supply affiliations/correspondence/ORCIDs where required, and make truthful funding/conflict/ethics statements. Do not infer absence of funding or conflicts from missing prose. Ordinary editing can supply headings, but only humans can attest to the underlying facts. This affects C10 and C14 across all 18 venues, and named-review C12 requirements.

The present disclosure names AI reviews and assistant-authored translations; it does not explain substantial assistance with drafting, coding, statistical interpretation and figure generation. Disclose those roles, tools/versions where recoverable, and actual human checks. Studying Gemini does not disclose use of an assistant to prepare the paper. For J01/J04/J05/J16, the verified T&F first-draft restriction creates a substantive policy conflict; J15 has a restrictive writing/interpretation policy. J12 and J10 need clarification of discouragement or policy tension. J18 needs clarification of the current rule for collecting model outputs as the research object. I recommend an honest eligibility inquiry if pursuing these held venues; I do not claim a later rewrite cures historical incompatibility.

### 2. Publish the descriptive accuracy–consistency result; reduce the local significance narrative — scientific/editorial major revision

The strongest result is not simply that distances correlate with Earth. It is the joint pattern: high ranks, nonzero triangle violations of meaningful magnitude, coherent spherical approximations, and a small reference-control residual (E4/E6). The abstract should lead with that result and one interpretable effect-size comparison. Closest prior work is acknowledged, but the contribution paragraph should state exactly which new scientific distinction is resolved by repeated global measurement and which is not. This is especially important for J01/J07/J08/J09/J11.

The manuscript now handles the strong randomization null accurately. I would retain effect sizes and the conditional test description, while making no population-median-map or causal language claim. The regional bootstrap is a different concern: a failure demonstration yielding 3.3–7.5% coverage in an allowed stress scenario is not repaired by calling the resulting intervals exploratory. It does not prove the actual intervals wrong, but it makes those p-values poor headline evidence. Move the local significance columns and derivation to a clearly labeled sensitivity supplement; retain observed group gains, distance balance, omission results and their limitations in the main text. For a narrow descriptive paper, new model calls are not intrinsically required. Stronger language-generalization claims would require a new replicated design, not more permutations of the same data.

### 3. Treat fixed prompts and fixed capitals as the population actually observed — scientific limitation

One alias, one period, one assistant-authored wording per language, English place names, and tightly clustered calls do not provide independent replication of a language treatment (E3). The paper discloses this well. Preserve those limits during journal tailoring rather than using social or cognitive rhetoric to manufacture fit. The two Chinese cases and Arab States regional grouping are unequal constructs; a positive interaction is not an absolute local advantage (E5/E7). J03/J06/J12/J17 would require genuinely relevant additional evidence for their applied/social emphasis. A new conclusion paragraph cannot create it.

A useful further diagnostic from the existing data, if the authors want it, is a simple geographic-null or calibration baseline evaluated with the same accuracy/consistency summaries. That would sharpen what the benchmark explains beyond a high whole-world correlation. It is my recommendation, not a listed journal requirement, and any such diagnostic must be labeled newly computed without adding fabricated model observations.

### 4. Archive and license the working evidence without confusing access with permission — submission blocker at specific venues

The public ZIP is a substantial strength: observations, exact prompts, code, environment and checks are available (E8). Live checks confirm the main repository is also public. However, absent archival identifiers and reuse terms are concrete gaps. J16/J18 explicitly require software/data DOI routes; J17 requires an appropriate repository or supplement route; J15 requires specified open licences. For all venues, an actual rights holder should approve article, code and data licences separately. Public downloading does not grant reuse rights.

The 41.8-MB bundle fits TMLR's 100-MB and RSOS's 350-MB file caps, but not PeerJ's 30-MB or EPJ's 20-MB per-file caps. Split material or provide an accepted archival route. Do not remove raw observations merely to make a supplement smaller. Anonymous-review copies must remove identifying URLs, embedded metadata and account handles without altering observed data or erasing the public project's history.

### 5. Make one venue-specific package after selecting a target — editorial production work

There is no reason to force 18 templates into the frozen research release. A chosen submission branch should retain the locked measurements and modify only the article package. The actual 194-token abstract fails Transactions in GIS's 150-word cap; it is close to Scientific Reports/RSOS's 200-word caps. Scientific Reports currently has ten main display items, above its eight-item limit. TACL, CL, JAIR and TMLR require their own initial formats; AI & SOCIETY explicitly requires Word. RSOS offers initial format flexibility. PLOS has conflicting generic format-free and LaTeX-specific instructions, so its embedded-figure PDF route needs clarification; prepare separate TIFF/EPS figures at 300–600 dpi, at most 10 MB each. Do not convert later reference styling into an invented initial rejection rule.

Several style rules could not be retrieved. Unknown is a real unresolved checklist item, not an allegation that the current manuscript fails an invented limit. The author should obtain those instructions before claiming compliance. Recheck all numerical counts and source citations after final conversion; do not use generic A4 page count as the journal's typeset count.

## Recommended submission order and venue-specific decisions

This is a practical editorial ranking, not an impact-factor ranking or acceptance probability. Every target still needs real authors and disclosures. **Prepare first:** J02 Transactions in GIS; **broad-science alternatives:** J13 PLOS ONE, then J14 Scientific Reports. J10 TMLR is a strong intellectual alternative after its assistance-policy tension is resolved. Do not submit simultaneously.

| Order | Journal | Recommendation for this manuscript |
|---|---|---|
| 1 | J02 Transactions in GIS | Best immediate audience match. Shorten abstract to 150 words, archive data, complete authors/disclosure and resolve upload instructions. |
| 2 | J13 PLOS ONE | Strong bounded empirical Research Article route; demote fragile local significance and finish human accountability/code-rights package. |
| 3 | J14 Scientific Reports | Good broad Article candidate; trim to eight main display items, retain concise abstract and complete declarations. |
| 4 | J10 TMLR | Good ML evaluation fit; seek clarification of extensive assistance, then mandatory anonymous template and author/quota checks. |
| 5 | J08 Computational Linguistics | Focused Short Paper could work if linguistic contribution is sharpened and translations remain explicitly observational. |
| 6 | J07 TACL | Specialist stretch; protect core evidence within ten-page limit, clarify artifact-link policy and strengthen relevance. |
| 7 | J09 JAIR | General AI stretch; stronger transferable lesson plus mandatory reproducibility checklist and human contribution audit. |
| 8 | J11 Artificial Intelligence | Lower-priority general AI article; significant contribution and inaccessible policy details need resolution. |
| 9 | J18 Data Science Journal | Conditional research-data framing; archive DOI and AI-observation policy clarification needed before preparation. |
| 10 | J16 PeerJ Computer Science | Computing fit, but hold on adopted drafting policy; DOI and supplement split also required. |
| 11 | J05 Spatial Cognition & Computation | Excellent conceptual audience, held by drafting policy; stronger behavioral-theory discussion if eligible. |
| 12 | J04 Cartography and Geographic Information Science | Good measured-map contribution, held by drafting policy; explain visualization choices without claiming usability evidence. |
| 13 | J01 International Journal of Geographical Information Science | Ambitious topical fit; both drafting and already-public identity rules need editorial clearance. |
| 14 | J15 Royal Society Open Science | Soundness fit but restrictive AI-preparation policy, licensing and human interpretation record create a hold. |
| 15 | J17 EPJ Data Science | Present contribution does not establish the required social-system insight; substantial new evidence or argument needed. |
| 16 | J03 Computers, Environment and Urban Systems | Reserve research direction; current capital judgments do not establish an urban/environmental application. |
| 17 | J06 Applied Spatial Analysis and Policy | Do not target current version: no evaluated policy or decision consequence. |
| 18 | J12 AI & SOCIETY | Do not target current version: social contribution gap plus AI-use discouragement and Word-only conversion cost. |

## Complete criterion-by-criterion review

Coverage: **252 unique assessments** (18 journals × 14 criteria): Fail 74, Partial 68, Pass 26, Unknown 84. These are completeness counts, not acceptance scores.

Each row is a specific assessment, not an additional journal policy. The corresponding frozen guide supplies official sources and distinguishes verified requirements from recommendations. Evidence references resolve to the ledger above. Known financial amounts are not accepted costs: the person supplying author/funder/rights information must make those choices. C14 Unknown also records missing package work where stated; it does not assert that the authors have made an undisclosed competing submission.

### [J01 — International Journal of Geographical Information Science](../journals/j01-international-journal-of-geographical-information-science.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J01-C01 | Pass | Geographic representation and metric uncertainty directly fit GIScience (E2–E4); fit is editorial judgment. |
| J01-C02 | Partial | Repeated global sampling and spherical controls are useful, but the general methodological advance beyond prior MDS needs sharper articulation; portal article category unresolved (E2). |
| J01-C03 | Unknown | Current word/page/abstract caps were not verified; the 194-token abstract and 15 generic pages do not establish compliance (E1). |
| J01-C04 | Unknown | Readable research structure exists, but keyword count and mandatory heading rules remain unverified; no keywords supplied (E10). |
| J01-C05 | Unknown | Journal-specific LaTeX and format-free eligibility remain unresolved despite working TeX/PDF sources (E10). |
| J01-C06 | Unknown | Exact reference style unverified; consistent plain bibliography and original methods references exist (E2/E10). |
| J01-C07 | Unknown | Measured versus interpolated geometry is clearly captioned, but journal artwork/file requirements and final-size accessibility have not been verified (E4/E6). |
| J01-C08 | Partial | Data/code statement and public ZIP exist; durable licensed deposit and anonymous reviewer route still need preparation (E8). |
| J01-C09 | Partial | Descriptive geometry is supported; local inference remains conditional on unverified independence and finite empirical tails (E3/E5/E9). |
| J01-C10 | Fail | No accountable author list or actual contributions/declarations supplied; funding, conflicts and rights facts remain unknown (E1/E10). |
| J01-C11 | Fail | Recorded assistant drafting conflicts with the verified T&F first-draft restriction; eligibility requires an honest editorial ruling, not a rewritten disclosure (E8/E10). |
| J01-C12 | Fail | Double-anonymous review is incompatible with the current identifying project URLs and non-anonymous bundle (E8). |
| J01-C13 | Unknown | Exact charges, publication-license options, author rights and funding coverage remain unresolved (E8/E10). |
| J01-C14 | Unknown | Existing public account-linked manuscript triggers the cited online-identity concern; exclusivity/history/author approvals and editorial eligibility are unestablished (E8). |

### [J02 — Transactions in GIS](../journals/j02-transactions-in-gis.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J02-C01 | Pass | Spatial representation, uncertainty and geographic computation closely match the measured contribution (E2–E4). |
| J02-C02 | Pass | Original research is appropriate for a bounded repeated-judgment benchmark; spherical reference control supplies substantive analysis beyond the website (E2/E4). |
| J02-C03 | Fail | The 194-token abstract exceeds the verified 150-word maximum; main-text cap remains unresolved (E1). |
| J02-C04 | Fail | Five to six keywords and a running title under 40 characters are absent; preferred spacing/font can be adapted without altering evidence (E10). |
| J02-C05 | Unknown | Free-format LaTeX is supported and sources exist, but conflicting instructions leave initial source-upload timing unresolved (E10). |
| J02-C06 | Pass | Consistent plain bibliography satisfies initial free-format references; production styling remains later work (E2/E10). |
| J02-C07 | Partial | Legends/vector plots exist; prepare separately designated figure/table and supporting files for revision and test accessible encodings (E6). |
| J02-C08 | Partial | Public observations/code and availability statement exist, but expected public archiving and a formal shared-data citation need a durable release (E8). |
| J02-C09 | Partial | Methods are evaluable and nulls explicit; reported local p-values need demotion or stronger justification given calibration failure (E5/E9). |
| J02-C10 | Fail | Actual author details, disclosures and submitting-author ORCID are absent; underlying funding/conflict information is unknown (E1/E10). |
| J02-C11 | Fail | Wiley substantive-assistance disclosure and human verification record are missing; AI reviews/translation notes do not cover drafting, code and analysis (E8/E10). |
| J02-C12 | Fail | Single-anonymous review requires genuine author information, which the empty title-page field does not provide (E1). |
| J02-C13 | Unknown | Optional OA route exists, but exact APC, author rights/funder requirements and institutional coverage are unresolved (E10). |
| J02-C14 | Unknown | No author-approved exclusive submission or verified prior-posting eligibility record exists; use the current Wiley portal after resolving these facts (E8/E10). |

### [J03 — Computers, Environment and Urban Systems](../journals/j03-computers-environment-and-urban-systems.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J03-C01 | Partial | AI/geocomputation fits, but no urban or environmental system is evaluated merely because capitals are cities (E2/E3). |
| J03-C02 | Partial | Original research could fit only after a substantive application argument; article taxonomy and applied evidence remain unresolved (E2/E7). |
| J03-C03 | Unknown | Blocked guide leaves length and abstract limits unverified; do not import another Elsevier journal's limits (E1). |
| J03-C04 | Unknown | Keyword, highlights and graphical-abstract requirements unverified; current research sections are readable (E10). |
| J03-C05 | Unknown | Current class and upload rules unverified; editable TeX/PDF alone does not establish journal compliance (E10). |
| J03-C06 | Unknown | Journal reference style and initial flexibility unresolved, although citations are internally consistent (E10). |
| J03-C07 | Unknown | Current figures distinguish fitted points and interpolation, but production dimensions and supplement-size rules were inaccessible (E4/E6). |
| J03-C08 | Unknown | Journal data-policy tier unresolved; public ZIP and availability statement are real, while archive DOI and licence are missing (E8). |
| J03-C09 | Partial | Current estimates support spatial judgment analysis, not practical routing or urban decision reliability; inference limitations remain (E5/E7). |
| J03-C10 | Fail | Required responsible human authorship and declarations have not been supplied; financial/rights facts remain unknown (E1/E10). |
| J03-C11 | Fail | Elsevier requires substantive preparation/research assistance disclosure; the manuscript documents measured Gemini, translation and reviews but not its full preparation history (E8/E10). |
| J03-C12 | Unknown | CEUS author-anonymity model was not verified; current identifying URLs cannot be judged compliant without that rule (E8). |
| J03-C13 | Unknown | Subscription/OA options exist, but current APC, licences and author funding route are unverified (E10). |
| J03-C14 | Unknown | Publisher preprint exception is relevant, but live package fields, exclusivity and all-author approval remain unverified (E8/E10). |

### [J04 — Cartography and Geographic Information Science](../journals/j04-cartography-and-geographic-information-science.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J04-C01 | Pass | Mathematical cartography and measured-versus-displayed geography fit the audience (E2/E4). |
| J04-C02 | Partial | Original research is plausible, but contribution should explain consequences of reconstruction/deformation choices; no usability evaluation exists (E4/E7). |
| J04-C03 | Unknown | Current article and abstract caps were not retrievable; generic pagination is not evidence of compliance (E1). |
| J04-C04 | Unknown | Title is appropriately behavioral; exact keywords, abstract and heading requirements remain unresolved (E1/E10). |
| J04-C05 | Unknown | LaTeX/template and format-free eligibility are journal-specific and unverified (E10). |
| J04-C06 | Unknown | Exact bibliography style is unresolved; original geodesic, alignment and elicitation references are present (E2/E4). |
| J04-C07 | Partial | Static/reference figures and interactive atlas fit supported displays; rights clearance and accessible final-size encodings still need author review (E6/E8). |
| J04-C08 | Unknown | Journal data-sharing tier remains unverified; public ZIP is accessible but needs durable/licensed and anonymous review arrangements (E8). |
| J04-C09 | Partial | Coastlines are correctly illustrative and no topology-preservation claim is made; local uncertainty and visualization-choice sensitivity remain limitations (E4/E9). |
| J04-C10 | Fail | Genuine authors and contribution/declaration records absent; source-figure rights and financial facts need author confirmation (E1/E10). |
| J04-C11 | Fail | Assistant manuscript drafting conflicts with T&F first-draft policy; seek editorial eligibility clarification before formatting (E8/E10). |
| J04-C12 | Fail | Double-anonymous manuscript and supplements are not prepared: identifying project URLs remain (E8). |
| J04-C13 | Unknown | Open Select exists but exact APC, funder licence compatibility and author rights are unconfirmed (E10). |
| J04-C14 | Unknown | ScholarOne route is known, but preprint exceptions, full package fields, exclusivity and approvals remain unestablished (E8/E10). |

### [J05 — Spatial Cognition & Computation](../journals/j05-spatial-cognition-and-computation.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J05-C01 | Pass | Behavioral spatial geometry and crosslinguistic elicitation are excellent conceptual fits (E2/E3). |
| J05-C02 | Partial | Empirical research type fits, but theoretical relevance beyond descriptive reconstruction needs development without asserting internal maps (E2/E7). |
| J05-C03 | Unknown | Word, page and abstract ceilings unverified; current counts cannot certify compliance (E1). |
| J05-C04 | Unknown | Operational cognitive-map definition and exploratory status are clear; journal structure and keyword count remain unverified (E2/E10). |
| J05-C05 | Unknown | Current LaTeX acceptance/template unresolved; existing editable sources are only preparation assets (E10). |
| J05-C06 | Unknown | Exact citation style unverified; conceptual precedents are present but behavioral-spatial discussion could be stronger (E2/E10). |
| J05-C07 | Unknown | Geometric controls and residuals exist, but artwork requirements and supplement limits remain unverified (E6). |
| J05-C08 | Unknown | Data-policy tier unverified; public raw outputs/prompts/code exist without archival identifier or established reuse licence (E8). |
| J05-C09 | Partial | Strong-null and wording caveats are appropriate; no human comparison, navigation transfer or independent language replication supports stronger cognitive claims (E3/E5/E7). |
| J05-C10 | Fail | No responsible human authors or declarations supplied; human-participant ethics applicability must be determined rather than invented (E1/E10). |
| J05-C11 | Fail | T&F first-draft restriction conflicts with assistant drafting history; disclosure alone is not established as a cure (E8/E10). |
| J05-C12 | Unknown | Anonymous referees do not establish whether author identities must be hidden; exact review model is unresolved (E1/E8). |
| J05-C13 | Unknown | Open Select option known, but APC, licence/incidental charges and author funding details unverified (E10). |
| J05-C14 | Unknown | ScholarOne route known; prior-posting exceptions, package metadata, exclusivity and author consent not established (E8/E10). |

### [J06 — Applied Spatial Analysis and Policy](../journals/j06-applied-spatial-analysis-and-policy.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J06-C01 | Fail | No tested policy or applied decision question supports this journal's defining focus; this is editorial scope judgment (E2/E7). |
| J06-C02 | Partial | Research-paper type exists, but current benchmark does not establish an applied contribution; prose alone cannot supply one (E7). |
| J06-C03 | Unknown | Abstract falls within 150–250 words, but the 8,000-word count convention is unresolved, preventing whole-criterion certification (E1). |
| J06-C04 | Fail | Required four to six keywords absent; current heading depth is within three levels (E10). |
| J06-C05 | Pass | Mathematical LaTeX accepted and complete editable sources exist; recommended Springer conversion is not an initial mandatory template rule (E10). |
| J06-C06 | Fail | Required author–year citations are not the current numeric plain style; alphabetization alone does not satisfy citation format (E10). |
| J06-C07 | Partial | Figures/tables are numbered, cited and captioned; separate captioned supplement package and accessibility review remain (E6). |
| J06-C08 | Partial | Availability statement and public package satisfy core access evidence; durable anonymous review deposit and licensing need work (E8). |
| J06-C09 | Partial | Conditional inferences are carefully bounded; no measured decision consequence supports a policy conclusion (E5/E7). |
| J06-C10 | Fail | Portal contributions, competing interests and responsible human author facts have not been supplied (E1/E10). |
| J06-C11 | Fail | Substantive AI writing/code/analysis assistance is not documented in Methods as required; copyediting exemption is inapplicable (E8/E10). |
| J06-C12 | Fail | Current identifying URLs and supplements conflict with double-anonymous preparation (E8). |
| J06-C13 | Unknown | Subscription no-APC route and quoted optional OA costs are known; actual author licence/funding choice and rights are unconfirmed (E10). |
| J06-C14 | Unknown | Exclusive submission, author approvals and manuscript-specific dissemination eligibility are unestablished (E8/E10). |

### [J07 — Transactions of the Association for Computational Linguistics](../journals/J07-tacl.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J07-C01 | Pass | Reproducible multilingual model evaluation fits NLP, conditional on emphasizing linguistic elicitation rather than website engineering (E2/E3). |
| J07-C02 | Partial | Completed empirical article is appropriate, but significance beyond prior city-MDS and the single-wording design needs a sharper case (E2/E3). |
| J07-C03 | Unknown | Ten-page main-content and appendix allowances require actual TACL reflow; abstract ceiling unverified (E1/E10). |
| J07-C04 | Partial | Literal title and main-text inferential caveats are present; front matter and optional five-to-ten editorial keywords need submission preparation (E1/E5). |
| J07-C05 | Fail | Mandatory TACL format is not the generic article class; source must be rebuilt in current official files (E10). |
| J07-C06 | Partial | References are accurate and consistent but need supplied ACL style; primary novelty comparison should remain explicit (E2/E10). |
| J07-C07 | Unknown | Appendix rules are known, but older external-link prohibition conflicts with newer replication-URL allowance; reviewer-access route needs clarification (E8). |
| J07-C08 | Partial | Promised artifacts already exist publicly; prepare permitted anonymous access and durable licensed citation (E8). |
| J07-C09 | Partial | Nulls and failed calibration are explicit; the linguistic inference remains wording-confounded and temporally unreplicated (E3/E5/E9). |
| J07-C10 | Fail | Required coauthor profiles and human responsibility record absent; private author/conflict fields must be completed truthfully (E1/E10). |
| J07-C11 | Fail | ACL acknowledgement disclosure of generative content assistance missing; current review disclosure does not identify writing/code/analysis roles (E8/E10). |
| J07-C12 | Fail | Mandatory anonymity fails because project URLs and bundle metadata identify the public release; absence of author text is insufficient (E8). |
| J07-C13 | Unknown | No publication charges verified, but current agreement, artifact rights and actual author consent to terms remain unresolved (E10). |
| J07-C14 | Unknown | No evidence establishes eligibility against ACL-family nine-month/TACL twelve-month exclusions, prior history or exclusive author approval (E10). |

### [J08 — Computational Linguistics](../journals/J08-computational-linguistics.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J08-C01 | Pass | Contemporary model evaluation and interdisciplinary language questions fit the stated audience (E2/E3). |
| J08-C02 | Partial | Short Paper is defensible, but independent language/date replication and a sharper linguistic insight would strengthen the editorial case (E2/E7). |
| J08-C03 | Unknown | Typical Short Paper limits require reflow in CL class; exact abstract ceiling was not verified (E1/E10). |
| J08-C04 | Fail | Separate required author/title/abstract metadata and five-to-ten editorial keywords are absent; English prose itself is suitable (E1/E10). |
| J08-C05 | Fail | Mandatory clv2025 class/LaTeX submission format not used; working generic source must be converted (E10). |
| J08-C06 | Fail | Supplied CL citation files are required and current plain style does not use them (E10). |
| J08-C07 | Unknown | Figures are readable with units/captions, but supplement-size ceilings and the specific package route remain unverified (E6). |
| J08-C08 | Partial | Promised observations/code already publicly available; persistent citation and reuse rights remain incomplete (E8). |
| J08-C09 | Partial | Conditional nulls are explicit; one translation/date and failed rare-tail bootstrap constrain linguistic interpretation (E3/E5/E9). |
| J08-C10 | Fail | Mandatory names, affiliations and emails absent; contribution/funding/conflict facts remain unknown (E1/E10). |
| J08-C11 | Fail | ACL acknowledgement disclosure of substantive generative assistance missing; human scientific responsibility not documented (E8/E10). |
| J08-C12 | Fail | Single-blind review requires author names/affiliations on page one, which are absent (E1). |
| J08-C13 | Unknown | Open access/copyright assignment request known; exact current fee/license statement and authors' ability to grant rights unverified (E10). |
| J08-C14 | Unknown | Originality/concurrent archival review/history and author approval cannot be certified from the manuscript; portal record needed (E8/E10). |

### [J09 — Journal of Artificial Intelligence Research](../journals/J09-jair.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J09-C01 | Pass | Accuracy versus structural consistency is relevant to AI evaluation and representation (E2/E4). |
| J09-C02 | Partial | Full Article suits the analyses, but general AI significance beyond one alias and established reconstruction tools needs strengthening (E2/E7). |
| J09-C03 | Unknown | No strict article or abstract ceiling verified; concision advice is not proof that any length is acceptable (E1). |
| J09-C04 | Partial | Unstructured abstract is permissible; structured alternative and final heading/section introductions would improve JAIR fit (E1/E10). |
| J09-C05 | Fail | JAIR-formatted PDF required at submission; generic article class is not compliant (E10). |
| J09-C06 | Partial | Initial bibliography is coherent; final JAIR styling and preference for published antecedents require production review (E2/E10). |
| J09-C07 | Partial | Figures include geometric controls; monochrome readability and critical-diagnostic placement need checking, and later code appendix release form is absent (E6/E9). |
| J09-C08 | Fail | Mandatory reproducibility checklist is not appended to review PDF, despite substantial public artifact evidence (E8). |
| J09-C09 | Partial | Evidence supports bounded description; general claims still limited by dependence, one alias and empirical-tail uncertainty (E3/E5/E9). |
| J09-C10 | Fail | No human author/contributor record supplied; exact journal declaration template is unverified and actual conflicts/funding unknown (E1/E10). |
| J09-C11 | Unknown | Core-contribution human ownership cannot be established from this preparation history; detailed assistance/accountability statement needed before eligibility judgment (E8/E10). |
| J09-C12 | Unknown | Reviewer confidentiality is verified but explicit author-anonymity rule is not; current blank author field is not a completed named submission (E1). |
| J09-C13 | Unknown | No fees and final CC BY verified; human agreement and underlying artifact rights remain unconfirmed (E10). |
| J09-C14 | Unknown | Three mandatory editorial answers and final author-approved exclusivity/history record absent; the underlying history must be supplied (E10). |

### [J10 — Transactions on Machine Learning Research](../journals/J10-tmlr.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J10-C01 | Pass | Analysis and visualization of learned-system behavior directly fit TMLR scope (E2/E4). |
| J10-C02 | Pass | The accurate-rank/inconsistent-metric result is intelligible and of potential ML interest; acceptance remains an editor's judgment (E2/E6). |
| J10-C03 | Unknown | Variable length permitted, but abstract ceiling unverified and current pages must be reflowed in mandatory template (E1/E10). |
| J10-C04 | Unknown | Main argument/caveats are clear; separate mandatory keyword rule unverified and template front matter not prepared (E5/E10). |
| J10-C05 | Fail | Mandatory unaltered TMLR template not used; generic formatting is an initial-submission problem (E10). |
| J10-C06 | Partial | References are substantively relevant but template bibliography conversion remains; no separate reference-count ceiling verified (E2/E10). |
| J10-C07 | Partial | 41.8-MB public ZIP fits 100-MB cap, but must be anonymized; appendix follows references and key evidence should remain reviewed (E6/E8). |
| J10-C08 | Partial | Public code/raw observations and verification commands exist; independently test an anonymized version and resolve reuse licence (E8). |
| J10-C09 | Partial | Claims mostly match evidence; empirical bootstrap and unverified independence still require demoting regional inferential emphasis (E5/E9). |
| J10-C10 | Fail | Active author profiles, fixed real author set, funding/conflicts and applicable ethics fields are absent (E1/E10). |
| J10-C11 | Unknown | Missing first-page AI disclosure is clear; tension between assistive-use permission and human-sourced ideas/results language requires clarification of actual extensive assistance (E8/E10). |
| J10-C12 | Fail | Double-blind package not prepared; public preprint permission does not allow identifying links in anonymous submission (E8). |
| J10-C13 | Unknown | No fee is verified, but irrevocable CC BY from submission and rights/public-review consequences require actual author agreement (E10). |
| J10-C14 | Unknown | All-author remaining quota, profiles, archival overlap and exclusive submission facts unestablished; public preprint alone is not disqualifying (E8/E10). |

### [J11 — Artificial Intelligence (AIJ, Elsevier)](../journals/J11-artificial-intelligence.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J11-C01 | Pass | Reasoning/representation and language-model evaluation fit broad AI scope (E2/E4). |
| J11-C02 | Partial | Regular Article type fits, but mature general AI insight beyond descriptive established-method application remains limited (E2/E7). |
| J11-C03 | Unknown | Advisory 20–30 pages is not a minimum; current publisher abstract limit remains unverified (E1). |
| J11-C04 | Unknown | English abstract/references exist, but current keywords/highlights requirements unavailable (E1/E10). |
| J11-C05 | Partial | Single-column A4 PDF is suitable in principle; 10-point is below preferred at-least-11-point guidance, and elsarticle is recommended (E10). |
| J11-C06 | Unknown | Current publisher bibliography requirement unavailable; do not import another Elsevier journal's rule (E10). |
| J11-C07 | Unknown | Vector plots are promising, but current artwork/supplement ceilings and final production compliance unverified (E6). |
| J11-C08 | Unknown | Current data-policy tier inaccessible; public code/data statement exists, while archiving/licensing remain incomplete (E8). |
| J11-C09 | Partial | Spherical controls and precise nulls strengthen completeness; conditional/local inference and generality remain limited (E3/E5/E9). |
| J11-C10 | Fail | Elsevier human authorship and authentic contribution/funding/conflict declarations have not been supplied (E1/E10). |
| J11-C11 | Fail | Preparation declaration before references and research/code assistance in Methods are missing despite documented substantive assistance (E8/E10). |
| J11-C12 | Unknown | Current AIJ author-anonymity model not directly verified; prepare separable identity fields but do not assume double anonymity (E8/E10). |
| J11-C13 | Unknown | Current charges, publishing options and licences were not verified; author funding/rights also unknown (E10). |
| J11-C14 | Unknown | Editorial Manager route known, but mandatory live files and all-author originality/exclusivity declarations not established (E10). |

### [J12 — AI & SOCIETY](../journals/J12-ai-and-society.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J12-C01 | Fail | No measured societal/cultural/philosophical argument supports this journal's defining focus; this is editorial scope judgment (E2/E7). |
| J12-C02 | Partial | Research Article exists, but a substantive social argument needs evidence, not speculative reframing of regional estimates (E7). |
| J12-C03 | Pass | 194-token abstract satisfies ordinary 150–250 range; current manuscript need not expand toward normal 10,000-word length (E1). |
| J12-C04 | Fail | Four to six keywords absent; current readable numbered heading depth is within three levels (E10). |
| J12-C05 | Fail | Explicit Word-only rule is unmet by the current LaTeX/PDF package (E10). |
| J12-C06 | Fail | Required author–year references differ from current numeric plain citations (E10). |
| J12-C07 | Partial | Numbered static figures/tables exist; Online Resources captions and editable Word-compatible artwork package remain (E6). |
| J12-C08 | Partial | Data Availability content and public ZIP exist, but durable anonymous/licensed deposit needs preparation (E8). |
| J12-C09 | Partial | Descriptive findings are bounded; no valid inference to social groups follows from operational city pairs, and bootstrap weakness remains (E5/E7/E9). |
| J12-C10 | Fail | Actual author/contribution/competing-interest portal records missing; ethics/funding applicability facts need human confirmation (E1/E10). |
| J12-C11 | Unknown | Strong discouragement of LLM use beyond grammar/translation creates an eligibility concern; substantive Methods disclosure is also missing (E8/E10). |
| J12-C12 | Fail | Double-blind materials are not anonymized and identifying project links remain (E8). |
| J12-C13 | Unknown | Subscription no-APC route and optional prices known; author licence/funder choice, rights and acceptance-date charge unknown (E10). |
| J12-C14 | Unknown | Public posting must be acknowledged, but eligibility, Word package and all-author exclusive approval are incomplete (E8/E10). |

### [J13 — PLOS ONE](../journals/J13-plos-one.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J13-C01 | Pass | Bounded empirical science with objective geographic reference fits broad scope (E2–E4). |
| J13-C02 | Pass | Research Article is appropriate; technical validity rather than speculative high impact suits the core descriptive result (E2/E6). |
| J13-C03 | Partial | 194-token abstract and full title fit stated caps; required short-title metadata has not been supplied (E1/E10). |
| J13-C04 | Partial | Scientific structure is readable; title page, continuous line numbering and house spacing need later/portal adaptation without treating format-free style as initial rejection (E1/E10). |
| J13-C05 | Unknown | Generic format-free guidance conflicts with LaTeX-specific template/figure instructions; current embedded-figure PDF needs portal clarification and a combined TeX source (E10). |
| J13-C06 | Partial | Current references are consistent initially; final Vancouver order must replace alphabetic plain numbering (E10). |
| J13-C07 | Partial | Vector source plots exist, but separate TIFF/EPS figures at 300–600 dpi and at most 10 MB need conversion/font checks; LaTeX guidance requests separate figures initially (E6). |
| J13-C08 | Partial | Data availability and essential code are publicly downloadable; reuse rights/licence and durable citation remain unresolved (E8). |
| J13-C09 | Partial | Main descriptive claims are supported, but main-text regional p-values are too prominent given severe diagnosed calibration failure and unverified independence (E5/E9). |
| J13-C10 | Fail | Actual authors/affiliations/correspondence/ORCID/CRediT and financial/conflict form records missing (E1/E10). |
| J13-C11 | Fail | Methods lacks complete tools/purposes/validation/affected-content disclosure for AI-assisted manuscript and analysis preparation (E8/E10). |
| J13-C12 | Fail | Required author identities absent; choice about publishing actual journal review history has not been made (E1/E10). |
| J13-C13 | Unknown | Listed APC and CC BY are verified, but rights, funding assistance/coverage and actual author agreement are unknown (E10). |
| J13-C14 | Unknown | One-page cover letter, author-approved exclusivity and prior-PDF disclosure package absent; no adverse submission history can be inferred (E8/E10). |

### [J14 — Scientific Reports](../journals/J14-scientific-reports.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J14-C01 | Pass | Known-reference empirical analysis fits broad science; computing/geoscience handling category needs author selection (E2/E4). |
| J14-C02 | Pass | Article is suitable for already-collected exploratory results; no retrospective Registered Report claim is made (E2/E3). |
| J14-C03 | Partial | 194-token abstract and literal title satisfy observed hard limits; 11-typeset-page/4,500-main-word guidance requires venue-specific count excluding stated sections (E1). |
| J14-C04 | Partial | Unstructured abstract and logical headings fit; title-page details and any chosen keywords require completion (E1/E10). |
| J14-C05 | Pass | 1,108,680-byte PDF fits combined first-submission 3-MB cap; TeX sources exist for revision (E10). |
| J14-C06 | Partial | References need Nature numbering in citation order; 18 cited items are below advisory 60 (E10). |
| J14-C07 | Fail | Current main text has four figures plus six tables, exceeding eight display items; move/recombine at least two and split long appendix material (E6). |
| J14-C08 | Partial | Public evaluation data/code and availability statement exist; persistent/licensed deposit and portfolio code-access checks remain (E8). |
| J14-C09 | Partial | Transparent methods and modest conclusions are strengths, but small-cell bootstrap and nonreplicated conditions limit inferential certainty (E3/E5/E9). |
| J14-C10 | Fail | Required human author, contribution, explicit competing-interest, funding and applicable ethics statements absent (E1/E10). |
| J14-C11 | Fail | Required substantive LLM-use Methods disclosure incomplete; detailed policy exceptions are unresolved and cannot waive the observed omission (E8/E10). |
| J14-C12 | Fail | Required identified-author title page absent; detailed review-option settings remain unverified (E1). |
| J14-C13 | Unknown | Fully OA route known, but exact journal/currency/tax quote, licence terms, coverage and author agreement unconfirmed (E10). |
| J14-C14 | Unknown | Cover letter, reviewer suggestions/exclusions, related-editor disclosure and exclusive all-author approval unprepared (E10). |

### [J15 — Royal Society Open Science](../journals/J15-royal-society-open-science.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J15-C01 | Pass | Science/mathematics scope includes geographic measurement and model evaluation (E2/E4). |
| J15-C02 | Pass | Research Article and soundness/null-result orientation fit the bounded descriptive findings (E2/E6). |
| J15-C03 | Pass | No overall length cap verified in catalogue; 194-token abstract is below 200 words, subject to final recount (E1). |
| J15-C04 | Fail | Full title page and three-to-ten keywords absent; British-English consistency also needs copyediting (E1/E10). |
| J15-C05 | Pass | Format-free initial LaTeX PDF supported; flatten file inclusions and supply source at the later production stage (E10). |
| J15-C06 | Partial | Consistent references usable initially; final Vancouver citation order and formal data/code citations need conversion (E10). |
| J15-C07 | Partial | 41.8-MB ZIP below 350-MB file cap; separate source files and CC BY rights for supporting material still require confirmation (E6/E8). |
| J15-C08 | Fail | Open code/data exist, but required CC0/CC BY reuse licensing has not been supplied; availability is not permission (E8). |
| J15-C09 | Partial | Objective accuracy/consistency results are supported; conditional inferential assumptions and failed tail calibration constrain claims (E5/E9). |
| J15-C10 | Fail | Submitting-author ORCID and genuine author/contribution/funding/conflict declarations absent (E1/E10). |
| J15-C11 | Fail | Substantive assistant drafting/analysis conflicts with the restrictive writing/interpretation policy; eligibility needs direct editorial clarification (E8/E10). |
| J15-C12 | Fail | Single-anonymous author metadata absent; mandatory eventual public journal-review history is distinct from these AI reports (E1/E10). |
| J15-C13 | Unknown | Quoted RSOS APC and CC BY verified; institutional coverage/waiver, rights and actual author acceptance unknown (E10). |
| J15-C14 | Unknown | Preprint deposition allowed, but approved author declarations and exclusive submission package absent (E8/E10). |

### [J16 — PeerJ Computer Science](../journals/J16-peerj-computer-science.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J16-C01 | Pass | Computer-science empirical evaluation fits when measured model behavior, not website features, is foregrounded (E2/E4). |
| J16-C02 | Pass | Research Article is a reasonable original, reproducible benchmark route subject to substantive human ownership (E2/E8). |
| J16-C03 | Unknown | Abstract/title appear within verified caps, but whole-paper ceiling was not verified; final character count should accompany submission (E1). |
| J16-C04 | Fail | Required author cover page, US Letter/12-point format and line numbering are not current A4/10-point article (E1/E10). |
| J16-C05 | Partial | LaTeX supported and sources complete, but official template/file package requires adaptation (E10). |
| J16-C06 | Fail | Required author–year references are not current numeric plain style (E10). |
| J16-C07 | Fail | 41,789,224-byte reproduction ZIP exceeds 30-MB individual supplement cap, although below 50-MB total; split or archive and cite (E8). |
| J16-C08 | Fail | Code/data available but no required archived DOI for software hosted on a social platform; alternative supplement route must be confirmed (E8). |
| J16-C09 | Partial | Reproducible descriptives are strong; conditional bootstrap cannot support robust population claims without further justification (E5/E9). |
| J16-C10 | Fail | Qualifying human authors, coauthor confirmation and actual declarations absent (E1/E10). |
| J16-C11 | Fail | Substantive drafting creates conflict with adopted T&F restriction, and detailed tool/version/how/why disclosure is missing (E8/E10). |
| J16-C12 | Fail | Identified-author cover page absent; optional journal review-history publication remains an author decision (E1). |
| J16-C13 | Unknown | CC BY known; current APC/membership pricing inaccessible and actual author funding/rights unconfirmed (E10). |
| J16-C14 | Unknown | No cover letter normally needed, but genuine submitting/coauthor confirmations, exclusive submission and prior-posting declarations are absent (E8/E10). |

### [J17 — EPJ Data Science](../journals/J17-epj-data-science.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J17-C01 | Partial | Generative models are in scope, but the current benchmark offers limited evidence about human/social or techno-social systems (E2/E7). |
| J17-C02 | Fail | Current descriptive standard-method study does not yet demonstrate the required substantive human/social-system insight; editorial contribution judgment (E2/E7). |
| J17-C03 | Unknown | 194-token abstract is within 150–250, but Regular Article main-text ceiling unverified (E1). |
| J17-C04 | Fail | Required full title page, three-to-ten keywords, abbreviation list and Declarations headings absent (E1/E10). |
| J17-C05 | Partial | LaTeX supported with editable sources; double spacing and line numbers still need preparation (E10). |
| J17-C06 | Unknown | Exact template/editor reference style unresolved; formal URL/data identifier citations need adding (E8/E10). |
| J17-C07 | Fail | 41.8-MB ZIP exceeds 20-MB per-supplement limit; split/cite resources and verify 10-MB figures/300-word legends (E6/E8). |
| J17-C08 | Fail | Personal-site-only release lacks required recognized repository/supplement arrangement, archive identifier and explicit software licence (E8). |
| J17-C09 | Partial | Robust descriptive geometry exists, but inferential fragility and absent social-system mechanism limit significance claims (E5/E7/E9). |
| J17-C10 | Fail | Required Declarations and human authors/correspondence missing; actual funding/conflicts are unknown (E1/E10). |
| J17-C11 | Fail | Substantive AI research/writing use is not fully documented in Methods with human responsibility (E8/E10). |
| J17-C12 | Fail | Single-anonymous review expects visible author identities, currently absent (E1). |
| J17-C13 | Unknown | Quoted APC/options known; actual acceptance-date charge, tax, funder compatibility and rights agreement unknown (E10). |
| J17-C14 | Unknown | Required author-submitted cover letter/approval/exclusivity/related-work record absent; public PDF must be disclosed (E8/E10). |

### [J18 — Data Science Journal](../journals/J18-data-science-journal.md)

| Criterion | Status | Reason and evidence |
|---|---|---|
| J18-C01 | Partial | Auditable benchmark data and provenance fit research-data use/reuse, but current emphasis is geographic inference (E2/E8). |
| J18-C02 | Partial | Research Paper is plausible after demonstrating a transferable measurement/data-methodology lesson rather than only a map result (E2/E8). |
| J18-C03 | Partial | Abstract fits 250-word cap; exact 8,000-word count including references remains to be completed under venue convention (E1/E10). |
| J18-C04 | Partial | Logical sections fit and up-to-six keywords are optional; full author title page and final house style need completion (E1/E10). |
| J18-C05 | Pass | Initial PDF accepted and editable TeX can accompany; final editable-format route must be confirmed if accepted (E10). |
| J18-C06 | Partial | Initial flexibility exists, but final Harvard author–year/DOI references differ from current plain numbering (E10). |
| J18-C07 | Partial | Vector figures exist; supply separate compliant files and use 300+ dpi/EPS route to satisfy conflicting resolution statements (E6). |
| J18-C08 | Fail | Explicit dataset/source-code DOI requirement unmet; public Pages ZIP alone does not provide archival identification (E8). |
| J18-C09 | Partial | Evidence is reproducible and conclusions largely justified; local uncertainty and fixed-design inferential scope remain limited (E5/E9). |
| J18-C10 | Fail | Human author/contribution and competing-interest statements absent; ethics/funding facts require actual author confirmation (E1/E10). |
| J18-C11 | Unknown | Current AI endpoint inaccessible and indexed broad data-creation restriction needs clarification for genuine observed LLM outputs; full assistance disclosure also needed (E8/E10). |
| J18-C12 | Fail | Single-blind submission needs real author identity; these author-side AI reports must not be passed off as journal expert reports (E1/E8). |
| J18-C13 | Unknown | Official fee page conflicts between £770 and £790; obtain written quote and confirm CC BY rights/funding agreement (E10). |
| J18-C14 | Unknown | Preprints allowed with cover-letter link, but author/rights-holder approval, exclusivity and full submission record absent (E8/E10). |

## Review limits and completion

This review checked frozen source text, policy guides, selected primary-policy pages, declarations, file sizes and manuscript hashes. It relied on the recorded numerical validation rather than rerunning the full reconstruction/permutation pipeline. It did not inspect another new publication review, contact an editor, invent author facts, collect model outputs or alter the frozen manuscript. The five author-requested reviews are AI-assisted preparation aids, not statistically independent human referee opinions. The report and companion JSON explicitly cover all 252 requested assessments.
