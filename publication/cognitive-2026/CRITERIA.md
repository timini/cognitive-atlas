# Cognitive-science publication review protocol

Review date: 9 September 2026. Review the actual latest 100-capital paper at commit `56fa5700fd65d7c0b911af1cce47debdbce62232`, not an imagined rewritten paper. Geography is the validation domain; the intended contribution concerns the structure, coherence, stability and context sensitivity of elicited spatial judgments. A proposed cognitive reframing is an action, not an accomplished change.

Five separately tasked AI reviewers each assess every one of 12 journals against all 15 criteria (180 cells per reviewer; 900 total). They are author-commissioned assessments, not journal peer review, independent human opinions, editorial acceptance predictions or a vote. Each reviewer reads the source, new official-source guides and current analysis evidence. Reviews remain independent of each other's reports.

## Criteria

| ID | Criterion |
|---|---|
| K01 | Scope and intended cognitive-science audience |
| K02 | Contribution threshold and suitable article type |
| K03 | Title, abstract, text and page limits; counting rules |
| K04 | Structure, keywords, readability and title-page content |
| K05 | Initial submission files, LaTeX/template and final production |
| K06 | References, citation system and data citation |
| K07 | Figures, tables, accessibility and supplements |
| K08 | Data, code, reproducibility, archives and reuse rights |
| K09 | Methods, estimands, controls and justified conclusions |
| K10 | Human authorship, contributions, ethics, funding and conflicts |
| K11 | AI assistance eligibility, disclosure and human accountability |
| K12 | Peer review, anonymity and existing public project |
| K13 | Access model, charges, licenses and author funding decision |
| K14 | Cover letter, prior posting, submission declarations and approvals |
| K15 | Cognitive theory, rhetorical tone and explanatory value |

## Ratings and evidence

Use Pass, Partial, Fail, Unknown or N/A. Every cell needs a concrete reason and evidence (file/section and/or official URL). Unknown applies to unavailable policy text or missing author facts; never substitute an assumed requirement. Separate reviewer judgment about fit from explicit journal rules. Formatting changes required only at acceptance are not initial-submission failures. A journal's human-cognition scope does not automatically mandate a new participant experiment. Invitation/topic-only venues must be marked conditional, not presented as immediately open routes.

K15 must inspect actual prose: the research question, introduction's theoretical argument, operational definition of cognitive map, distinction between descriptive and explanatory claims, hypotheses, and discussion. Merely replacing 'geography' with 'cognition' is insufficient. Do not equate an output-derived geometry with a measured hidden representation, human cognitive process, subjective experience, or cultural mechanism. Neither a human comparison nor mechanistic access is universally required, but state which claim each would permit.

Respect the corrected evidence: error-sign controls are descriptive, preserve pairwise absolute errors, and do not validate an inferential null; response-distribution permutations do not isolate a language effect or test equal population median maps; regional estimates show no observed absolute advantage and have no reliable significance claim. New proposed work is not current evidence. No outdated smaller-capital runs belong in this assessment.

Do not contact journals, start paid API collections, invent author declarations, or revise the frozen paper as part of reviewing. Prior AI drafting and review history must remain accurately disclosed. Public access does not establish reuse permission. Policy queries may be recommended where needed; do not portray them as sent.

## Review deliverables

Each reviewer writes `reviews/review-NN-ROLE.md` (under 60,000 characters for a GitHub issue) and a companion JSON:

```json
{"reviewer_id":"R01","role":"...","manuscript_commit":"56fa5700fd65d7c0b911af1cce47debdbce62232","summary":"...","assessments":[{"journal_id":"C01","criterion_id":"K01","status":"Partial","reason":"...","evidence":["paper/main.tex: Introduction","journals/C01-....md"]}]}
```

Include 12 journal-specific verdicts and all 180 criterion reasons in the Markdown as well as JSON. Lead with substantive scientific/tone findings, then the matrix. Prioritize research needed to discriminate explanations, and explain whether adding model families alone changes the verdict. The root synthesis may disagree with a review where evidence warrants it.
