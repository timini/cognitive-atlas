# Publication review 04 — Reproducibility, data and research integrity

**Verdict: not yet submission-ready at any of the 18 targets.** The downloadable research package is a substantial strength: I extracted it, verified its frozen contracts and ran its six paper-specific tests successfully. The outstanding barriers are human authorship and preparation disclosure, durable/reusable publication artifacts, venue-specific packaging, and scientific assumptions that software tests cannot settle. Transactions in GIS, PLOS ONE and Scientific Reports are the most practical first preparations in my judgment. TMLR is also plausible if its policy tension and anonymous package are resolved. This is not an acceptance prediction.

Reviewed independently against all 252 journal–criterion combinations on 9 September 2026, without reading the other four new reports. Manuscript: `5f9bdaa3641f684708ad914a721eecc25835ab64`; only the 100-capital English/Arabic/written-Chinese Gemini 3.5 Flash study. These are author-requested AI submission-readiness assessments, not commissioned journal reviews, human peer review, or journal decisions. No journal was contacted. Criteria refer to the supplied official-source guides; recommendations are my judgment. A later disclosure cannot make unknown historical facts true.

## Prioritized findings

1. **Human accountability and actual AI preparation are publication blockers (all C10/C11).** The author field is blank ([source L21](https://github.com/timini/cognitive-atlas/blob/5f9bdaa3641f684708ad914a721eecc25835ab64/paper/main.tex#L21)); L220 explicitly leaves identities unassigned. Discussion of ten AI reviews does not disclose assistant drafting, coding, analysis and translation. Create a truthful tool/version/task/affected-content/validation record, and obtain the actual human authors' contribution, funding, conflict and rights statements. Their identity or eligibility cannot be inferred from the GitHub account. Do not name an AI author or claim these checks were human review.
2. **Preserve the distinction between access, licensing and permanence (C08).** The released ZIP contains 121 files, is 41,789,224 bytes, and matches its manifest SHA-256 `bdbba8fd68facc1a8a45b47183d220ab97ddb0c0ea00397dc86bddc1762aedb7`. Extracted `paper.revision100.verify` and six `tests/test_paper.py` tests passed using the existing local Python environment. This is an actual package check, not a new clean-environment dependency installation, full PDF rebuild or repeat of expensive permutation analyses. No LICENSE path exists in the archive or root inventory. Natural Earth's public-domain source statement does not license newly authored software or the collected corpus. Human rights holders must choose suitable licenses, then archive a version with a DOI. DOI/software archive is explicit at J16/J18; recognized repository or supplements matter at J17; CC0/CC BY is explicit at J15. Elsewhere a DOI is often a recommendation, not an invented universal mandate.
3. **Correct a live-access fact without rewriting historical provenance (C08/C12/C14).** L214 says the repository is private at the revision. During this review the unauthenticated [GitHub API](https://api.github.com/repos/timini/cognitive-atlas) returned `private:false`, `visibility:public`, and the [repository page](https://github.com/timini/cognitive-atlas) displayed Public. The public publication manifest matches local PDF/ZIP hashes. Thus lack of access is not a present finding; the frozen privacy sentence is stale relative to current access. Do not erase history. Create an allowed anonymous artifact package for J01/J04/J06/J07/J10/J12, and distinguish public-preprint eligibility from identifying links in submitted materials. J01's cited online-identity restriction needs a separate editorial ruling.
4. **Policy eligibility precedes cosmetic formatting (C11).** Verified T&F first-draft wording conflicts with the assistant preparation history at J01/J04/J05 and, through incorporated policy, J16. J15 restricts replacement of scientific interpretation; J12 discourages use beyond grammar/translation. TMLR's FAQ and general policy need reconciliation for extensive assistance. J18's currently inaccessible policy needs clarification for empirical measurements of AI outputs, which are not fabricated observations. An honest disclosure or human rewrite is not established as a cure for every venue. Seek clarification only after humans can supply the real history; no inquiry has been sent here.
5. **The archive is not an automatically acceptable supplement (C05/C07).** It exceeds PeerJ's 30-MB per-file limit and EPJ's 20-MB limit, while fitting TMLR's 100-MB and RSOS's 350-MB ceilings. PLOS has a real format-free/LaTeX-page tension: prepare separate compliant figures and a flattened TeX source rather than assuming the generic PDF route suffices. JAIR's missing reproducibility checklist is a specific initial desk-return risk. Mandatory TACL/CL/JAIR/TMLR formats are absent. AI & SOCIETY expressly requests Word. Format-free journals should not be failed merely for a later production bibliography conversion.
6. **Computational reproduction is not experimental replication (C08/C09).** [L218](https://github.com/timini/cognitive-atlas/blob/5f9bdaa3641f684708ad914a721eecc25835ab64/paper/main.tex#L218) admits missing resumed-session collector snapshots/dirty-source state; L51 admits an unfrozen alias and unverified stationary independent requests. Hashes demonstrate byte identity of saved evidence, not historical execution identity or a reproducible future provider response. Preserve those statements. The observed parser is whole-response numeric validation without an output schema (L54); do not relabel the dataset using the newer collection protocol.
7. **Retain the scientific limitations in reviewed main text (C09).** Strong distributional-null randomization (L94–98) cannot establish unequal population median maps. The explicit rare-tail calibration failure (L263) means tight empirical intervals are not generally calibrated. Language and explanatory wording remain confounded; canonical entity names stay English (L47–51). For a bounded descriptive paper, keep estimates and diagnostic limits and consider demoting local significance emphasis. A broader language claim needs genuinely new randomized time-block/wording replication, not more Monte Carlo draws or additional code tests. No causal regional, cultural, navigation or policy claim is justified to manufacture journal fit.

## Evidence key and assessment rules

- **E1:** `paper/main.tex` L1–27 and L225: generic 10-point A4 class, blank author, approximately 194 abstract whitespace tokens, plain bibliography; inventory records 15 pages. Counts are not journal-certified.
- **E2:** L29–38: previous reconstruction work, bounded empirical contribution, operational behavioral interpretation and exploratory status.
- **E3:** L40–58: entities, WGS84, exact settings, translations, dispatch, parser, invalids and denominators.
- **E4:** L70–98: reconstruction/control/alignment, interpolation caveat, conditional null and multiplicity.
- **E5:** L213–220: availability, source locks, historical-execution gaps and unassigned human authors.
- **E6:** independent extracted-release verification above; `paper/input-lock.json`, `paper/release-lock.json`, `public/paper/publication.json`, `data/capitals-100-v3.sources.json`. Existing source permission statement covers Natural Earth; no project reuse license is present.
- **E7:** `publication/manuscript-inventory.json`: four vector PDF figures, ten floating tables and one longtable; 41.8-MB ZIP; no root license file. These counts include appendices; my direct source count finds ten display environments before the appendix, also above J14's eight-item main-text limit.
- **E8:** L181–211 and L258–265: regional estimands, limitations, bootstrap derivation and severe rare-tail undercoverage.

Each section below cites its own guide; every row's criterion means that journal's criterion, e.g. J13-C08. **Pass** means the inspected applicable item is satisfied, not overall readiness. **Partial** names unfinished work; **Fail** is an observed unmet requirement/policy conflict; **Unknown** preserves unverified policy or author facts. No criterion is genuinely N/A for the whole submission package. C10 failures concern absent records; the contents of future truthful declarations remain unknown. C13 uncertainty does not imply author inability to pay. C14 uncertainty does not accuse the authors of simultaneous submission.

## J01 — International Journal of Geographical Information Science

[Official-source criteria guide](../journals/j01-international-journal-of-geographical-information-science.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Geographic representation and uncertainty directly fit GIScience; E2 distinguishes facts from geometry. |
| C02 | Partial | E2 identifies antecedents; the repeated global benchmark needs a sharper IJGIS significance argument. |
| C03 | Unknown | J01 numerical caps were inaccessible; 15 generic pages and 194 abstract tokens prove no compliance. |
| C04 | Partial | Research structure is clear; keywords are absent and required heading/front-matter rules remain unknown. |
| C05 | Unknown | Source and PDF exist, but J01 LaTeX/format-free eligibility has not been established. |
| C06 | Unknown | E1 uses plain numeric references; the journal reference style remains unverified. |
| C07 | Partial | E4 separates fitted capitals from display warping; final artwork/accessibility rules need confirmation. |
| C08 | Partial | E5/E6 verify accessible data/code; persistent archive, reuse license and anonymous access remain missing. |
| C09 | Partial | E3/E4/E8 preserve key limits; request independence and rare-tail uncertainty remain scientifically unresolved. |
| C10 | Fail | E1/E5 leave human authors unassigned; genuine contributions, funding and conflicts remain unknown. |
| C11 | Fail | Assistant-drafted sections conflict with the verified first-draft restriction; disclosure alone is no cure. |
| C12 | Fail | E5 identifies the account/project online; blank author text does not satisfy double-anonymous materials. |
| C13 | Unknown | J01 APC/license choices and actual author funding eligibility have not been established. |
| C14 | Fail | Account-linked public dissemination conflicts with cited identity rule; editor ruling and author approval needed. |

## J02 — Transactions in GIS

[Official-source criteria guide](../journals/j02-transactions-in-gis.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E2/E4 study spatial representation and uncertainty, directly matching Transactions in GIS. |
| C02 | Partial | Original research is appropriate; emphasize geographic diagnostics rather than the deployed interface. |
| C03 | Fail | E1 abstract is about 194 words against the verified 150-word maximum; main-text cap remains unknown. |
| C04 | Fail | No 5–6 keywords or short running title; E1 is 10-point rather than preferred 12-point double spacing. |
| C05 | Partial | Free-format LaTeX is supported and sources exist; resolve the guide's initial-upload timing conflict. |
| C06 | Pass | E1/E2 supply a consistent numbered bibliography, allowed initially; production adaptation is separate. |
| C07 | Partial | Vector originals/captions exist; create separate revision tables and an explicitly cited supplement set. |
| C08 | Partial | E6 verifies available raw data and code; add durable archive and formal shared-data citation. |
| C09 | Partial | E3/E8 allow evaluation and expose failures; dependence assumptions need independent scientific assessment. |
| C10 | Fail | E1/E5 lack actual authors and required submitting-author ORCID; funding/conflict facts remain unknown. |
| C11 | Fail | E5 discloses AI reviews only, not substantive writing/code/analysis assistance required by Wiley policy. |
| C12 | Partial | Single-anonymous review permits identifying links; legitimate author/title metadata still need completion. |
| C13 | Unknown | OA versus standard route and funding are undecided; exact APC and rights eligibility remain unverified. |
| C14 | Unknown | Public posting is documented, but author approval, exclusivity and preprint treatment need confirmation. |

## J03 — Computers, Environment and Urban Systems

[Official-source criteria guide](../journals/j03-computers-environment-and-urban-systems.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Partial | Capital-distance judgments overlap geocomputation but demonstrate no urban/environmental-system application. |
| C02 | Partial | E2 is an empirical benchmark, not an evaluated urban tool; contribution/category need editorial checking. |
| C03 | Unknown | Blocked current guide leaves word/page/abstract limits unverified; do not import another journal's caps. |
| C04 | Unknown | Clear research sections exist; mandatory keywords, highlights and graphical abstract remain unverified. |
| C05 | Unknown | Editable TeX and figures exist; CEUS template and initial-upload acceptance remain unverified. |
| C06 | Unknown | The plain bibliography is internally consistent; current CEUS citation requirements are inaccessible. |
| C07 | Partial | E4 labels coastline interpolation and E7 supplies vector figures; CEUS file limits are unverified. |
| C08 | Partial | E6 supports computational reproduction; archive/license gaps remain and CEUS sharing tier is unknown. |
| C09 | Partial | Geodesic validity is documented; no tested routing/planning consequence supports an applied-use claim. |
| C10 | Fail | E1/E5 lack accountable human author and declaration records; actual funding/conflicts remain unknown. |
| C11 | Fail | Elsevier research and manuscript-preparation disclosures are absent beyond model and review descriptions. |
| C12 | Unknown | CEUS author-anonymity model is unverified; do not assume identifying E5 links are allowed or forbidden. |
| C13 | Unknown | Subscription/OA routes exist, but exact fees, licenses and author coverage are unverified. |
| C14 | Unknown | No verified author-approved package or exclusivity declaration; disclose E5 public posting under actual rules. |

## J04 — Cartography and Geographic Information Science

[Official-source criteria guide](../journals/j04-cartography-and-geographic-information-science.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E4 directly addresses cartographic representation and distinguishes observed geometry from interpolation. |
| C02 | Partial | Original research fits; visual appeal has not been evaluated as an interpretability or usability benefit. |
| C03 | Unknown | CaGIS numerical article/abstract limits remain inaccessible; current pagination cannot establish compliance. |
| C04 | Partial | E2/E4 give a literal question and display caveat; keywords and exact front-matter style need confirmation. |
| C05 | Unknown | Current LaTeX/template and format-free eligibility remain unverified despite a working source package. |
| C06 | Unknown | Source bibliography exists; CaGIS house style has not been verified. |
| C07 | Partial | Dynamic atlas and vector controls fit permitted displays; audit final accessibility and artwork rights. |
| C08 | Partial | E6 gives public observations/code; prepare durable licensed and anonymous artifact access if eligible. |
| C09 | Partial | E4 rejects topology/usability claims; quantitative interpretation is bounded but independence remains unverified. |
| C10 | Fail | Actual human authors and declarations are absent; Natural Earth attribution does not establish all reuse rights. |
| C11 | Fail | Recorded assistant drafting conflicts with the shared T&F first-draft restriction; seek honest eligibility ruling. |
| C12 | Fail | E5 names the public project and account; double-anonymous manuscript/supplements are not prepared. |
| C13 | Unknown | Hybrid option exists, but current APC and actual author license/funding choices remain unknown. |
| C14 | Unknown | ScholarOne route is known; prior-posting eligibility, package fields and all-author approval are unresolved. |

## J05 — Spatial Cognition & Computation

[Official-source criteria guide](../journals/j05-spatial-cognition-and-computation.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E2 operationally defines elicited cognitive maps, fitting spatial cognition and crosslinguistic expression. |
| C02 | Partial | Empirical route fits; no human comparison or transfer task yet tests competing representational explanations. |
| C03 | Unknown | Journal word/page/abstract caps remain unverified; generic 15-page layout is not compliance evidence. |
| C04 | Partial | Behavioral framing is clear; add keywords and check cognitive-science terminology/front-matter rules. |
| C05 | Unknown | Exact journal LaTeX acceptance and template could not be verified; preserve sources pending clarification. |
| C06 | Unknown | E2 cites close antecedents; journal-specific citation style remains unverified. |
| C07 | Partial | Static reference and residual figures exist; final-resolution/accessibility requirements remain unknown. |
| C08 | Partial | E6 preserves exact prompts and outputs; permanent identifier/license and allowed review access are missing. |
| C09 | Partial | E3 explicitly admits unvalidated wording; independence and inferential limits need specialist human review. |
| C10 | Fail | E1/E5 lack authors and contributions; genuine funding/conflict/ethics applicability facts remain unknown. |
| C11 | Fail | Substantive assistant drafting is incompatible with inspected T&F first-draft wording without editorial ruling. |
| C12 | Unknown | Anonymous referees are verified; author anonymity is not, so blank authors cannot be scored compliant. |
| C13 | Unknown | Open Select exists, but APC/license details and author funding decisions remain unverified. |
| C14 | Unknown | Public manuscript history must be declared; package rules, approval and prior-posting exceptions need checking. |

## J06 — Applied Spatial Analysis and Policy

[Official-source criteria guide](../journals/j06-applied-spatial-analysis-and-policy.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Fail | E2/E4 do not evaluate a policy decision or application central to this journal's applied scope. |
| C02 | Partial | Research-paper form fits, but a demonstrated policy contribution needs new evidence rather than added rhetoric. |
| C03 | Partial | About 194 abstract words fits 150–250; total count against the usual 8,000-word rule needs reconciliation. |
| C04 | Fail | No required 4–6 keywords; heading hierarchy is suitable but front matter is incomplete. |
| C05 | Partial | Editable LaTeX exists and is supported; port to recommended source structure and verify all source uploads. |
| C06 | Fail | E1 uses numeric plain citations instead of required author–year references with DOI links. |
| C07 | Partial | Numbered captions and vector files exist; prepare separate, captioned Online Resource supplements. |
| C08 | Partial | E5 is an availability section and E6 works; persistent licensed archive and anonymous review copy remain. |
| C09 | Partial | Statistical qualifications are explicit, but no decision consequence is measured for policy interpretation. |
| C10 | Fail | Human author/contribution/declaration record is absent; portal funding/conflict facts must come from authors. |
| C11 | Fail | Methods disclose Gemini elicitation but not substantive assistant writing/coding/analysis required here. |
| C12 | Fail | E5 public identifying links remain in materials intended for double-anonymous review. |
| C13 | Unknown | Subscription has no APC and OA quote is known; rights, route and author coverage are unapproved. |
| C14 | Unknown | Exclusive submission and coauthor approval cannot be established; public history needs accurate disclosure. |

## J07 — Transactions of the Association for Computational Linguistics

[Official-source criteria guide](../journals/J07-tacl.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Repeated multilingual model evaluation fits NLP resources/evaluation; E2 supplies the behavioral framing. |
| C02 | Partial | E2 distinguishes prior reconstruction; technical significance beyond one alias/wording still needs strengthening. |
| C03 | Unknown | Ten main pages plus constrained appendices must be counted in TACL format, not the current generic class. |
| C04 | Partial | Main argument is intelligible; optional keyword metadata and venue front matter remain unprepared. |
| C05 | Fail | E1 uses generic article rather than the mandatory official TACL format. |
| C06 | Partial | Primary references exist; apply ACL bibliography style and verify published antecedents survive conversion. |
| C07 | Partial | Critical evidence is in the paper; appendix allocation/anonymity and conflicting URL guidance need resolution. |
| C08 | Partial | E6 demonstrates existing artifacts, but permitted anonymous access and durable citation remain unprepared. |
| C09 | Partial | E3/E8 delimit inference; independent language/wording replication and request independence remain unresolved. |
| C10 | Fail | Required coauthor profiles and genuine human accountability records are absent; affiliations/interests unknown. |
| C11 | Fail | ACL content-assistance acknowledgment is absent; AI-review mention does not disclose drafting and coding. |
| C12 | Fail | E5 links directly to account-associated public material inside an otherwise unnamed manuscript. |
| C13 | Unknown | No submission/publication charge is verified; current agreement and author reuse rights still need approval. |
| C14 | Unknown | No verified author approval or ACL-family submission history; check nine/twelve-month restrictions and exclusivity. |

## J08 — Computational Linguistics

[Official-source criteria guide](../journals/J08-computational-linguistics.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Contemporary LM elicitation and evaluation fit CL; E2 avoids claiming evidence of human language processing. |
| C02 | Partial | A focused Short Paper is credible; linguistic insight must remain bounded by unvalidated prompt wording. |
| C03 | Unknown | Short-paper page guidance needs clv2025 reflow; generic pagination and unverified abstract cap are insufficient. |
| C04 | Fail | English structure is present, but required separate title/author/abstract metadata and 5–10 keywords are absent. |
| C05 | Fail | LaTeX is available, but E1 does not use the required current clv2025 class. |
| C06 | Fail | Generic plain bibliography is not the supplied CL citation/reference configuration. |
| C07 | Partial | Legible vector source figures exist; confirm CL supplement format/size and keep core findings self-contained. |
| C08 | Partial | Promised artifacts exist and E6 verifies them; add a persistent citation and explicit code/data reuse license. |
| C09 | Partial | Exploratory limits are explicit; no independent translation, time-block or human scientific validation exists. |
| C10 | Fail | Mandatory full names, affiliations and emails are absent; author contribution and disclosure facts are unknown. |
| C11 | Fail | ACL-required substantive content-assistance acknowledgment is absent from this preparation history. |
| C12 | Fail | Single-blind CL requires named authors on page one; the E1 blank author field demonstrably fails. |
| C13 | Unknown | OA and copyright checklist are known; explicit fee/current license and author-rights compliance remain unknown. |
| C14 | Unknown | Prior public posting is known; actual approval, exclusivity and any earlier archival-review history are unknown. |

## J09 — Journal of Artificial Intelligence Research

[Official-source criteria guide](../journals/J09-jair.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Consistency of learned-system judgments is an AI evaluation question, as framed in E2. |
| C02 | Partial | A full Article matches the analyses; a stronger general AI lesson is needed beyond applying established tools. |
| C03 | Unknown | No verified hard cap; current length is not disqualifying, but JAIR template count and abstract cap need checking. |
| C04 | Partial | Clear sections exist; structured abstract is optional, while JAIR front matter still needs preparation. |
| C05 | Fail | E1 is not the required JAIR-formatted submission PDF, despite possessing editable production sources. |
| C06 | Partial | E2 identifies close prior work; regenerate JAIR bibliography and prioritize published versions at production. |
| C07 | Partial | Vector plots exist; test monochrome readability and keep essential evidence outside unreviewed online appendices. |
| C08 | Fail | No completed JAIR reproducibility checklist is appended; verified E6 artifacts do not replace this requirement. |
| C09 | Partial | E6 supports recomputation, not fresh alias replication; E3/E8 expose independence and tail limitations. |
| C10 | Fail | Author identities and human scientific responsibility are unassigned; actual funding/conflicts remain unknown. |
| C11 | Fail | No adequate account of substantive assistant contribution or demonstrated human ownership of core contributions. |
| C12 | Partial | No verified double-anonymous rule; named JAIR author metadata are absent and must be legitimately supplied. |
| C13 | Unknown | Zero fees and final CC BY are verified; approval of publication agreement and underlying rights is unknown. |
| C14 | Fail | The three mandatory editorial questions are not answered; exclusivity and all-author approval remain unknown. |

## J10 — Transactions on Machine Learning Research

[Official-source criteria guide](../journals/J10-tmlr.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E2/E4 analyze learned-system behavior and visualization within the stated TMLR audience. |
| C02 | Partial | High ranking with inconsistent metrics is an intelligible empirical lesson; soundness still needs human assessment. |
| C03 | Unknown | Variable length is allowed; actual TMLR reflow and an unverified abstract ceiling prevent full certification. |
| C04 | Partial | Main methods clearly specify the null; template front matter and concise contribution summary need adaptation. |
| C05 | Fail | E1 uses generic article instead of the mandatory unmodified TMLR LaTeX template. |
| C06 | Partial | Bibliographic evidence exists; use the supplied template configuration rather than current plain defaults. |
| C07 | Partial | 41.8-MB ZIP fits 100-MB allowance, but E5 identifying content makes the current supplement non-anonymous. |
| C08 | Partial | E6 verification and six extracted-package tests pass; create and retest an anonymous licensed artifact copy. |
| C09 | Partial | Claims are bounded; fragile local intervals and unverified request independence still warrant human review. |
| C10 | Fail | Real author profiles, fixed author set and declarations are absent; applicable funding/conflict facts are unknown. |
| C11 | Fail | Required first-page AI disclosure is absent; extensive assistance also needs FAQ/policy eligibility clarification. |
| C12 | Fail | Direct identifying public links violate anonymous-submission preparation, even though public preprints are allowed. |
| C13 | Unknown | Zero fee is verified; author permission for CC BY 4.0 from submission and artifact rights is unestablished. |
| C14 | Unknown | Author quota, profiles, fixed author list, exclusivity and archival-overlap history are not established. |

## J11 — Artificial Intelligence (AIJ, Elsevier)

[Official-source criteria guide](../journals/J11-artificial-intelligence.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E2 distinguishes factual calibration and global consistency, relevant to broad AI knowledge evaluation. |
| C02 | Partial | The full study is mature in implementation, but broader conceptual novelty beyond one alias remains limited. |
| C03 | Unknown | No hard article cap in inspected FAQ; current publisher abstract limit is inaccessible and advice is not a cap. |
| C04 | Partial | English abstract/references exist; current mandatory highlights/keywords and author front matter need checking. |
| C05 | Partial | A4 single column fits preference, but 10-point is below recommended 11-point; elsarticle conversion is advised. |
| C06 | Unknown | Current AIJ publisher reference style was inaccessible; do not infer it from another Elsevier journal. |
| C07 | Partial | E7 supplies publication-quality vector candidates; final-size, monochrome and supplement rules need checking. |
| C08 | Partial | E5/E6 provide reproducibility evidence; AIJ sharing tier is unknown and durable archive/license remain absent. |
| C09 | Partial | Detailed computational evidence exists; temporal dependence and local bootstrap failure delimit the findings. |
| C10 | Fail | Actual human authors and ethical declarations are absent; source verification is not human accountability. |
| C11 | Fail | Elsevier preparation declaration before references and research-assistance Methods disclosure are missing. |
| C12 | Unknown | Current AIJ review anonymity is unverified; do not assume the public project links are acceptable or forbidden. |
| C13 | Unknown | Current APC, subscription charges and licenses were not verified; no author funding choice is established. |
| C14 | Unknown | Editorial Manager route is known; author-approved files, exclusive review and publication-history facts are not. |

## J12 — AI & SOCIETY

[Official-source criteria guide](../journals/J12-ai-and-society.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Fail | E2/E8 establish prompt-specific geography, not the societal/cultural question central to AI & SOCIETY. |
| C02 | Partial | A Research Article needs substantive social argument/evidence; speculative culture claims would overreach E8. |
| C03 | Partial | About 194 words fits ordinary abstract guidance; normal 10,000-word length is guidance, not a target to pad to. |
| C04 | Fail | Required 4–6 keywords are absent; clear existing headings need an accessible societal framing if pursued. |
| C05 | Fail | Current submission is LaTeX/PDF, whereas journal-specific instructions require editable Word. |
| C06 | Fail | E1 uses numeric plain references rather than the required author–year style and DOI links. |
| C07 | Partial | Numbered static figures/tables exist; provide captioned Online Resources and verify converted artwork. |
| C08 | Partial | E5 supplies availability prose and E6 data/code; anonymized licensed archival access still needs preparation. |
| C09 | Partial | Conditional caveats are clear; evidence cannot support a population-level cultural or societal inference. |
| C10 | Fail | Actual authors/contributions and declarations are absent; submission-interface facts must come from humans. |
| C11 | Fail | Substantive assistant use exceeds journal discouragement and is inadequately disclosed; eligibility needs ruling. |
| C12 | Fail | E5 identifying URLs remain in materials intended for double-blind review. |
| C13 | Unknown | No-APC subscription and optional OA quote are known; author choice, rights and funding approval remain unknown. |
| C14 | Unknown | Public prepublication needs acknowledgment; eligibility, Word package, exclusivity and author approval unresolved. |

## J13 — PLOS ONE

[Official-source criteria guide](../journals/J13-plos-one.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | A ground-truth empirical study of model outputs fits broad scientific research without claiming neural access. |
| C02 | Partial | Research Article is appropriate under soundness criteria; independent scientific accountability remains unfinished. |
| C03 | Partial | Abstract/title meet verified ceilings; required short-title metadata still needs preparation and exact count. |
| C04 | Fail | E1 lacks title-page author details, double spacing and continuous line numbering required by house style. |
| C05 | Partial | Format-free and LaTeX pages conflict; flatten source and prepare figure-free PDF plus separate figures. |
| C06 | Partial | Numeric citations exist; final Vancouver order must follow first citation instead of current plain alphabetic order. |
| C07 | Fail | Embedded PDF plots do not meet the specific separate TIFF/EPS LaTeX route; convert and validate fonts/size. |
| C08 | Partial | E6 confirms publicly available essential code/raw data; formal availability form, rights and durable deposit remain. |
| C09 | Partial | E3/E8 distinguish nulls and failed calibration; no current evidence justifies broad language-population claims. |
| C10 | Fail | Required authors/correspondence/ORCID/CRediT and form declarations are absent; actual financial facts unknown. |
| C11 | Fail | Methods omit preparation tool identities, affected content and human validation beyond measured-model settings. |
| C12 | Partial | Identified-author route is compatible with links, but real authors and peer-review-history choice are unassigned. |
| C13 | Unknown | Listed APC/CC BY are known; authors' ability to pay, assistance eligibility and rights approval are unknown. |
| C14 | Fail | No one-page cover letter or approved submission declarations; disclose public preprint and confirm exclusivity. |

## J14 — Scientific Reports

[Official-source criteria guide](../journals/J14-scientific-reports.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Empirical computer-science/geographic evaluation fits the broad audience; choose the handling category carefully. |
| C02 | Partial | Article is appropriate; already observed data cannot be relabeled a Registered Report or independent replication. |
| C03 | Partial | Title and approximately 194-word abstract fit; main-text count/typeset-page guidance need journal reflow. |
| C04 | Partial | Unstructured abstract and clear research sections exist; add front matter and up to six keywords if used. |
| C05 | Pass | Current approximately 1.1-MB combined PDF is below the verified 3-MB initial-file limit; revision source exists. |
| C06 | Partial | Only 18 cited works fit guidance; convert alphabetic plain numbering to Nature first-citation style. |
| C07 | Fail | Current main text has 10 displays, above eight; move extras and the appendix multipage table to supplements. |
| C08 | Partial | E6 verifies accessible evaluation inputs/code; submit formal availability statement and durable reuse terms. |
| C09 | Partial | Design and inferential limits are explicit; request dependence and finite-tail failure remain open validity issues. |
| C10 | Fail | Required human authors, contributions and explicit declarations are absent; genuine funding/interests unknown. |
| C11 | Fail | Measured Gemini is documented, but assistant preparation and Methods disclosure are incomplete; exceptions unverified. |
| C12 | Fail | Required identified-author title page is absent; detailed review options should be checked in current portal. |
| C13 | Unknown | Only a portfolio starting APC is verified; exact invoice, coverage, license rights and author funding unknown. |
| C14 | Fail | Cover letter and requested submission metadata are unprepared; all-author approval/exclusive consideration unknown. |

## J15 — Royal Society Open Science

[Official-source criteria guide](../journals/J15-royal-society-open-science.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | E2/E4 empirical geographic measurement fits science, engineering and mathematics. |
| C02 | Partial | Objective Research Article route is suitable; technical soundness and human scientific ownership need assessment. |
| C03 | Pass | About 194 abstract words is below 200; the inspected catalogue imposes no overall paper-length limit. |
| C04 | Fail | Full author title page and 3–10 keywords are absent; British-English consistency needs checking. |
| C05 | Pass | Format-free initial LaTeX PDF is supported; source flattening is a later production task, not initial rejection. |
| C06 | Partial | Current bibliography is coherent; final Vancouver first-citation order and archive citations need preparation. |
| C07 | Partial | 41.8-MB archive fits 350-MB cap; supply separate production artwork and human-approved supplement licensing. |
| C08 | Fail | No explicit CC0/CC BY grant exists for data/code; public download and source hashes do not satisfy licensing rule. |
| C09 | Partial | E6 supports computation; scientific independence and rare-tail limits persist despite readable conclusions. |
| C10 | Fail | Required human authors, submitting-author ORCID and declarations are absent; underlying author facts unknown. |
| C11 | Fail | Assistant interpretation/drafting exceeds inspected language-only allowance; disclose history and seek eligibility ruling. |
| C12 | Partial | Single-anonymous route permits identifying links; named authors and consent to mandatory review history remain. |
| C13 | Unknown | Verified APC/CC BY do not establish authors' funding, waiver, tax or rights eligibility. |
| C14 | Unknown | Preprints are allowed; genuine author approval, rights declarations and exclusive consideration remain unverified. |

## J16 — PeerJ Computer Science

[Official-source criteria guide](../journals/J16-peerj-computer-science.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Pass | Model-output evaluation and auditable computation fit computer science; website construction alone would not. |
| C02 | Partial | Research Article fits; scientific originality and human ownership remain to be assessed beyond software tests. |
| C03 | Pass | The 194-word abstract is below 500 words/3,000 characters; title is below the 250-character hard limit. |
| C04 | Fail | E1 uses A4 10-point, not the specified Letter/12-point setup; cover page and line numbers are absent. |
| C05 | Partial | LaTeX PDF and sources exist; use the official template and deliver the required complete source package. |
| C06 | Fail | Current numeric references do not match required author–year order by author/year/title. |
| C07 | Fail | The 41,789,224-byte ZIP exceeds the 30-MB per-file supplement cap; split or use an accepted archive route. |
| C08 | Fail | Code/data are accessible, but no DOI software archive satisfies the explicit social-platform archiving requirement. |
| C09 | Partial | QC/raw outputs are reproducible; dependence and bootstrap failures require scientific review beyond tests. |
| C10 | Fail | Qualifying human authors and confirmed coauthorship/declarations are absent; ethics/funding applicability unknown. |
| C11 | Fail | Tool/version/purpose disclosure is incomplete; incorporated T&F drafting restriction creates an eligibility hold. |
| C12 | Fail | An identified author cover page is required and absent; optional review-history publication is not yet chosen. |
| C13 | Unknown | CC BY is stated; current APC/membership offer and author funding/rights remain unverified. |
| C14 | Unknown | No cover letter is normally needed, but author submission, confirmations, exclusivity and posting facts need approval. |

## J17 — EPJ Data Science

[Official-source criteria guide](../journals/J17-epj-data-science.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Partial | Generative models fit scope; E8 does not establish insight into human/social systems from the judgments. |
| C02 | Fail | Current descriptive benchmark does not demonstrate the required substantive new social-system insight. |
| C03 | Pass | Approximately 194 abstract words meets 150–250; no verified numerical main-text ceiling is imposed here. |
| C04 | Fail | Title page, 3–10 keywords, abbreviation list and required Declarations headings are absent. |
| C05 | Partial | LaTeX/editable source is supported; supply line/page numbers and double spacing before submission. |
| C06 | Partial | Formal references exist, but dataset/code identifiers and the exact template reference configuration need work. |
| C07 | Fail | 41.8-MB ZIP exceeds the 20-MB per-supplement limit; individual PDF figures are already below 10 MB. |
| C08 | Fail | No recognized persistent archive identifier or software license; Pages alone does not satisfy this deposit route. |
| C09 | Partial | Computational checks are strong, but local inference is fragile and no social-behavior conclusion is established. |
| C10 | Fail | Required human correspondence, contributions, funding and competing-interest declarations are absent. |
| C11 | Fail | Substantive assistant preparation is not described in Methods; experimental model settings are insufficient. |
| C12 | Fail | Single-anonymous review requires visible legitimate authors; the current author field is empty. |
| C13 | Unknown | Current quote/license options are known; rights, funder compatibility, waivers and author approval remain unknown. |
| C14 | Fail | Required cover letter with policy, approval and exclusivity content is absent; human author must submit. |

## J18 — Data Science Journal

[Official-source criteria guide](../journals/J18-data-science-journal.md)

| Criterion | Status | Evidence and required action |
|---|---|---|
| C01 | Partial | E5/E6 offer a reusable measurement dataset; foreground data provenance and reuse rather than map appearance. |
| C02 | Partial | Research Paper is plausible if its general research-data contribution is developed beyond this one benchmark. |
| C03 | Partial | Abstract fits 250; count the entire article including references against the verified 8,000-word ceiling. |
| C04 | Partial | Logical sections exist; complete author title page and adapt house style before acceptance, not necessarily initially. |
| C05 | Partial | Initial PDF is acceptable and TeX source exists; final editable-format handling still needs confirmation. |
| C06 | Partial | Initial flexibility applies, but final Harvard author–year references and DOI citations require conversion. |
| C07 | Partial | Individual vector figures are below 20 MB; convert to acceptable EPS/300+ dpi and supply separate artwork. |
| C08 | Fail | No dataset/source-code DOI exists, explicitly required here; accessible E6 ZIP does not substitute for this identifier. |
| C09 | Partial | Evidence is carefully bounded; independent scientific review of dependence and bootstrap limits remains necessary. |
| C10 | Fail | Human authors/contributions and competing-interest declaration are absent; funding/ethics facts remain unknown. |
| C11 | Unknown | Current AI-policy endpoint is unavailable; clarify empirical LLM-output exception and complete preparation disclosure. |
| C12 | Partial | Single-blind route allows identity, but real authors remain unassigned; this AI review is not a journal review. |
| C13 | Unknown | Official fee prose/table conflict and author funding/rights are unresolved; CC BY alone is not an approved grant. |
| C14 | Unknown | Allowed preprint must be disclosed with link; cover letter, rights-holder approval and exclusivity are unverified. |

## Completion check

All 18 journals and all 14 criteria are assessed once: **252 unique cells**. Counts: Pass 19, Partial 99, Unknown 54, Fail 80. The companion JSON preserves each assessment for validation and comparison. No numerical measurement or manuscript text was changed in this review.

Review input contract verified after the availability correction: SHA-256 `d8cef93816476a3dcc5b4adb65e2953d369c02b3ff1bfcac6c6e690eafa6d462`; all 24 listed file hashes matched.
