# Where to submit Cognitive Atlas

This dossier compares **18 journals** for the current **100-capital study** and contains five independently prepared AI-assisted submission-readiness reviews. Each reviewer assesses all 14 criteria for every journal, covering scientific fit, methods, presentation, data, authorship, AI-use policy and the submission package.

Start with **Transactions in GIS**, **PLOS ONE**, and **Scientific Reports**. **TMLR** is a promising AI-facing alternative with an AI-policy clarification to resolve. This ordering is our judgment about fit and preparation effort, not an acceptance prediction. Several other journals have good topical fit but substantial eligibility or contribution concerns. Inclusion below does not imply that an unchanged manuscript is eligible.

The reviewed manuscript is fixed at [`5f9bdaa`](https://github.com/timini/cognitive-atlas/tree/5f9bdaa3641f684708ad914a721eecc25835ab64/paper). Requirements were checked against official sources on **9 September 2026**. The existing paper and measured data have not been changed by this assessment.

## Target journals and individual style guides

| ID | Journal and submission guide | Proposed article | Main consideration |
|---|---|---|---|
| J02 | [Transactions in GIS](journals/j02-transactions-in-gis.md) | Original research | Strongest geographic audience fit; 150-word abstract and complete author/disclosure package needed. |
| J13 | [PLOS ONE](journals/J13-plos-one.md) | Research Article | Soundness-focused empirical route; clarify competing general/LaTeX formatting instructions. |
| J14 | [Scientific Reports](journals/J14-scientific-reports.md) | Article | Broad scientific audience; split main displays from supplements and verify full current AI policy. |
| J10 | [Transactions on Machine Learning Research](journals/J10-tmlr.md) | Original empirical research | Useful evidence-based scope; mandatory template, anonymity and AI-policy clarification. |
| J08 | [Computational Linguistics](journals/J08-computational-linguistics.md) | Short Paper | Focused language-model finding; strengthen NLP contribution and use the required class. |
| J07 | [Transactions of the Association for Computational Linguistics](journals/J07-tacl.md) | Original empirical paper | Demanding NLP target; ten-page main text, anonymity and appendix restrictions. |
| J09 | [Journal of Artificial Intelligence Research](journals/J09-jair.md) | Article | Needs a convincing general AI lesson and mandatory reproducibility checklist. |
| J17 | [EPJ Data Science](journals/J17-epj-data-science.md) | Regular Article | LLMs explicitly in scope, but a substantive human/social-system insight is required. |
| J18 | [Data Science Journal](journals/J18-data-science-journal.md) | Research Paper | Benchmark/data-methodology framing; archive DOI required, AI wording and conflicting fees need clarification. |
| J11 | [Artificial Intelligence](journals/J11-artificial-intelligence.md) | Full Research Paper | Ambitious general-AI contribution; several current journal-specific rules remain unverified. |
| J05 | [Spatial Cognition & Computation](journals/j05-spatial-cognition-and-computation.md) | Research Article | Strong conceptual fit, but first-draft AI policy creates a submission hold. |
| J04 | [Cartography and Geographic Information Science](journals/j04-cartography-and-geographic-information-science.md) | Research Article | Geographic representation and visualization fit; same AI-drafting hold. |
| J01 | [International Journal of Geographical Information Science](journals/j01-international-journal-of-geographical-information-science.md) | Research Article | Strong topical but demanding contribution fit; AI drafting and public-identity concerns. |
| J16 | [PeerJ Computer Science](journals/J16-peerj-computer-science.md) | Research Article | Computing audience; inherited AI-policy concern and software-archive requirements. |
| J15 | [Royal Society Open Science](journals/J15-royal-society-open-science.md) | Research Article | Soundness-based scope, but restrictive AI-writing/scientific-task policy creates a hold. |
| J12 | [AI & SOCIETY](journals/J12-ai-and-society.md) | Research Article | Weak current societal argument; strong AI-use caution and Word-only submission. |
| J03 | [Computers, Environment and Urban Systems](journals/j03-computers-environment-and-urban-systems.md) | Research Article | Requires demonstrated urban/environmental relevance beyond capital geography. |
| J06 | [Applied Spatial Analysis and Policy](journals/j06-applied-spatial-analysis-and-policy.md) | Original research | Requires an actual applied or policy contribution, not speculative implications. |

Each guide separates **verified requirements**, **publisher advice**, **our recommendations**, and **unverified rules**. It also distinguishes initial submission from final production. Numerical fees are dated estimates in the publisher's listed currency; actual author coverage, tax and waiver eligibility are unknown. Missing prices are not treated as free publication.

## Five publication-readiness reviews

1. [Editorial structure and readiness](reviews/review-01-editorial.md)
2. [Methods, statistical inference and claims](reviews/review-02-methods.md)
3. [Contribution, geographic interpretation and audience](reviews/review-03-contribution.md)
4. [Reproducibility, data and research integrity](reviews/review-04-reproducibility.md)
5. [Writing, style and submission-policy compliance](reviews/review-05-style-policy.md)

These roles provide different emphases; **each report still covers all 18 journals and all 14 criteria**. Companion JSON files give the reason for every assessment. [Coverage verification](coverage.json) checks all 1,260 cells. It is not an acceptance score, a vote among independent human experts, or proof that every policy interpretation is correct.

See [review synthesis and recommended actions](RECOMMENDATIONS.md) and the [GitHub issue index](github-issues.json) for the posted reports. The source [research notes](research/) retain access failures and conflicting policies so that unresolved details remain visible.

## How to use this dossier

Choose a primary venue, then complete its specific package rather than applying every journal's formatting rules simultaneously. Human authors must establish and attest to their actual contributions, validate the science, supply identity/funding/conflict information, and accurately disclose the assistance used in writing, analysis, code and translation. Reviewers cannot fill these facts in by assumption.

The reproduction ZIP and GitHub repository both provide public access to the data and analysis code. Live checks on 9 September 2026 show that the repository is public; the frozen manuscript’s private-repository statement needs updating. A permanent archive and a reuse license are distinct missing pieces. An archive DOI is compulsory for some shortlisted venues and advisable for others; the guide identifies which.

The five reports are **author-requested AI-assisted assessments**, not journal-appointed peer reviews, editorial endorsements, or submissions. Nothing has been sent to a journal, no authorship statement has been invented, and no publication charge has been agreed. Any actual submission should recheck current instructions and disclose the existing public PDF.

## Recheck coverage

From the repository root:

```sh
python publication/validate.py
```

This verifies the [input contract](review-inputs.json), the 18 guides, the five reviewer identities, the 252 unique assessments per reviewer, and report checksums. The [criterion definitions](CRITERIA.md) and [manuscript inventory](manuscript-inventory.json) explain the assessment scope and measurable preparation facts.
