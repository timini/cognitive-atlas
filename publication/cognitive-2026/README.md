# Cognitive-science publication assessment

The research question is **what coherent spatial organization is expressed by a language model's judgments, and how stable is that organization across tasks and elicitation contexts?** Geography is the domain in which the answer can be checked against known structure.

This dossier replaces the earlier geography-led submission strategy. It assesses the actual [100-capital paper at `56fa570`](https://github.com/timini/cognitive-atlas/tree/56fa5700fd65d7c0b911af1cce47debdbce62232/paper), including its existing framing weaknesses; it does not pretend a cognitive rewrite or new experiment has already been completed. Official requirements were checked on **9 September 2026**. The measured dataset and paper are unchanged by this review round.

## Journal selection and individual guides

My practical first target is **Cognitive Processing**, subject to a substantial cognitive argument and evidence revision. **Cognitive Science** is the stronger aspirational intellectual target. **Cognitive Research: Principles and Implications** is plausible if the study develops a real use-inspired cognitive contribution. These are editorial judgments about fit, not claims that the current paper is submission-ready or predictions of acceptance.

| Journal | Guide | Fit and condition |
|---|---|---|
| Cognitive Processing | [C10](journals/C10-cognitive-processing.md) | Explicitly includes artificial cognition; strongest practical scope match. Needs a clearer explanatory question and independent validation. |
| Cognitive Science | [C01](journals/C01-cognitive-science.md) | Excellent conceptual home for spatial knowledge expressed through language; requires a stronger multidisciplinary cognitive contribution. |
| Cognitive Research: Principles and Implications | [C05](journals/C05-cognitive-research-principles-and-implications.md) | Plausible use-inspired route. Needs a substantive Significance Statement and cognitive account, not a software-use claim. |
| Spatial Cognition & Computation | [C09](journals/C09-spatial-cognition-and-computation.md) | Excellent intellectual fit; current publisher rule against AI first drafting creates an unresolved eligibility conflict with preparation history. |
| Psychonomic Bulletin & Review | [C06](journals/C06-psychonomic-bulletin-and-review.md) | Ambitious short empirical route, demanding a broad theoretical point and substantial compression. |
| Cognition | [C03](journals/C03-cognition.md) | Stretch target after tests that constrain cognitive explanations. Several current formatting rules were inaccessible and remain unknown. |
| Cognitive Psychology | [C04](journals/C04-cognitive-psychology.md) | Stretch target requiring a substantial cognitive-theory advance; model replication alone is insufficient. |
| Memory & Cognition | [C07](journals/C07-memory-and-cognition.md) | Conditional on a concrete contribution to human cognition; computational work is possible, but the bridge must be tested. |
| Behavior Research Methods | [C08](journals/C08-behavior-research-methods.md) | Alternative methods paper only if the elicitation/reconstruction instrument gains convincing validation and cognitive-research utility. |
| Frontiers in Psychology — Cognition | [C12](journals/C12-frontiers-in-psychology-cognition.md) | Conditional on a psychological theoretical basis and contribution to human cognition; general AI relevance alone does not meet the section scope. |
| Journal of Environmental Psychology | [C11](journals/C11-journal-of-environmental-psychology.md) | Conditional on an actual human–environment question. Calling distorted output “psychogeography” is insufficient. |
| Topics in Cognitive Science | [C02](journals/C02-topics-in-cognitive-science.md) | Thematic-collection possibility; does not accept unsolicited standalone original articles. Not a normal immediate submission route. |

The set includes viable directions, ambitious targets and explicitly conditional alternatives. They are not twelve interchangeable destinations for the unchanged paper. No blanket requirement for newly collected human-participant data has been inferred from a journal's name. Where human comparisons are recommended, the guide explains which cognitive claim they would strengthen.

Each guide distinguishes verified requirements, publisher policy, editorial advice and unavailable rules. Check its scope, article type, tone, abstract/text limits, references, files, figures, anonymity, AI disclosure, data requirements and charges. Unknown fees are not zero fees, and format-free initial submission does not remove later production requirements. Historical substantive AI drafting and analysis must remain accurately disclosed; a rewrite cannot erase that history.

## Five fresh reviews

Each reviewer assessed all **12 journals × 15 criteria**, including a dedicated cognitive-theory and tone criterion. The roles emphasize different questions while sharing the full coverage requirement.

1. [Cognitive theory and editorial contribution](reviews/review-01-theory.md) — [GitHub issue #16](https://github.com/timini/cognitive-atlas/issues/16)
2. [Statistical methods and construct validity](reviews/review-02-methods.md) — [GitHub issue #17](https://github.com/timini/cognitive-atlas/issues/17)
3. [Writing, tone and psychogeographic framing](reviews/review-03-tone.md) — [GitHub issue #18](https://github.com/timini/cognitive-atlas/issues/18)
4. [Reproducibility and submission integrity](reviews/review-04-reproducibility.md) — [GitHub issue #19](https://github.com/timini/cognitive-atlas/issues/19)
5. [Research value and next-experiment priorities](reviews/review-05-research.md) — [GitHub issue #20](https://github.com/timini/cognitive-atlas/issues/20)

The [review synthesis](RECOMMENDATIONS.md) separates manuscript changes from new evidence and unresolved author facts. The [research assessment and proposed experiments](RESEARCH-ASSESSMENT.md) explain the strongest present observations, why additional model families help, and why an independent comparative-judgment task would add more explanatory value than another map alone. The [GitHub issue index](github-issues.json) links each posted report.

These are separately tasked **AI-assisted author reviews**, not journal-appointed peer review or statistically independent human opinions. Reviewers did not read each other's reports. Guide preparation preceded reviewing and supplied a common evidence base; three agents prepared guides and performed reviews, and two further agents reviewed that shared dossier. Agreement should not be interpreted as independent expert consensus.

## Evidence and validation

The [protocol](CRITERIA.md) defines all 15 criteria. [Manuscript inventory](manuscript-inventory.json) records the inspected release. [Input lock](review-inputs.json) fixes the manuscript bytes, guides and research-source notes; the [coverage report](coverage.json) checks all **900 assessments**, reasons and report hashes. Scope and policy interpretations still require judgment; a successful completeness check does not certify every claim or predict acceptance.

Run `python publication/cognitive-2026/validate.py` from the repository root. Historical manuscript bytes are read from the stated Git commit, so later edits do not silently turn these into reviews of a newer version.

No journal has been contacted, no submission made and no new model responses collected for this assessment. Actual human author information, scientific sign-off, rights choices and funding/conflict declarations remain necessary before submission.
