# Review 03: Academic writing, organization, and interpretation

**Recommendation:** Revise before submission. The manuscript has a defensible research question and unusually explicit limits, but its presentation still mixes a research article with a software delivery report. The main revision should make the scientific question, measured effects, and evidential limits easier to follow.

**Scope:** Close reading of `paper/main.tex` and its generated model, language, pairwise, and local-effect tables at repository commit `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`. This review evaluates prose and whether the presentation follows the reported evidence. It does not independently reproduce statistical computations, verify every external citation, or review PDF layout. Line references below refer to that source snapshot.

## Findings

### 1. Medium: Lead with the research contribution, rather than storage and infrastructure

**Locations:** `paper/main.tex:26`, `paper/main.tex:32`, `paper/main.tex:197`.

The abstract introduces a “file-based experimental pipeline.” The introduction describes the contribution principally as an “auditable repeated-sampling implementation,” and the availability section announces “There is no database.” These details do not explain why the experiment matters. The storage medium has no bearing on the main questions about geographic consistency or language dependence. The long queue/retry/checkpoint paragraph also displaces information a research reader needs first: what observations exist, what can be reanalyzed, and where those materials can be obtained.

**Suggested abstract opening:**

> We reconstruct the geographic geometry implied by repeated distance judgments between national capitals. The study separates accuracy against WGS84 reference distances, geometric consistency, and variation across instruction languages.

**Suggested contribution sentence:**

> Repeated sampling allows us to distinguish differences between language conditions from variation across calls and to separate changes in the pattern of distance estimates from changes in their overall accuracy.

Retain implementation and checkpoint details in technical documentation or a short supplementary implementation section. In the article, identify the deposited materials and explain which analyses can be reproduced without new model calls. This preserves the valuable provenance information without treating infrastructure preferences as findings.

### 2. Medium: Put effect sizes before significance in the abstract and conclusion

**Locations:** `paper/main.tex:26`, `paper/main.tex:153`, `paper/main.tex:204`; `paper/generated/pairwise-table.tex`.

The abstract foregrounds the common adjusted permutation probability but does not state the magnitude of the global language differences. The phrase “substantial changes” leaves practical magnitude undefined. The conclusion similarly says that languages change the matrix “detectably,” which can leave readers equating a small conditional probability with a visibly different world map. The result paragraph at line 153 handles this better by contrasting Mandarin's 122.3 km median disagreement with its 0.7 km difference in median-based MAE.

**Suggested abstract replacement:**

> Across the ten language comparisons, average absolute differences between pair medians ranged from 80.6 to 133.6 km and exceeded the within-pair permutation baseline (Holm-adjusted Monte Carlo p = 0.004). For Mandarin and English, the average disagreement was 122.3 km, although their overall median-based MAEs differed by only 0.7 km.

These values match the generated pairwise table; this review has not independently recomputed them. Remove “substantial” unless a scale or practical criterion is supplied. Keep the existing warning that the tests concern judgments, not an inferential comparison of whole reconstructed maps.

### 3. Medium: Give the geometry question an explicit results answer

**Locations:** `paper/main.tex:36`, `paper/main.tex:69`, `paper/main.tex:71`, `paper/main.tex:123`, `paper/main.tex:136`, `paper/main.tex:158`.

The first stated research question asks whether the estimates admit a useful reconstruction. Yet the results mainly emphasize correlations, language tests, and the exploratory Spanish finding. Triangle violations and spherical stress appear in tables, while the dimensionality curve is largely explained in a figure caption. A reader can reach the conclusion without a clear account of what the reconstruction contributes beyond pairwise accuracy.

Add a short results paragraph interpreting the displayed geometry diagnostics. For example:

> In the matched language conditions, spherical stress ranged from 0.0261 to 0.0322, while 9.61–12.20% of capital triples violated a triangle inequality. Thus high rank agreement with actual distances coexisted with measurable inconsistency in the estimated matrices.

Then describe the dimensionality curve relative to its WGS84 baseline without asserting a selected intrinsic dimension. Explain in prose that the triangle percentage counts triples with a violation, if that is the implemented denominator. Do not assign a qualitative label such as “good fit” without a reference or stated criterion.

### 4. Medium: Rewrite the availability statement to match the published access route

**Locations:** `paper/main.tex:201`; corroborating repository text: `README.md:160` in the inspected working copy.

The manuscript says the atlas is “an access-controlled exploration interface.” The repository documentation now states that the GitHub Pages website is public. A private source repository and a public data-bearing website are different access arrangements, so the current prose can incorrectly tell readers that the research materials are inaccessible.

**Suggested revision, after confirming the currently published files:**

> The interactive atlas is available at https://timini.github.io/cognitive-atlas/. The source repository remains private. The website provides downloadable experiment exports; no permanent archival DOI has been assigned.

If historical access status is scientifically relevant, distinguish the collection snapshot from publication status. Check the actual downloadable materials before making the final availability claim; this writing review inspected repository documentation rather than testing every public URL. Update `paper/README.md` consistently if necessary.

### 5. Medium: Make the change of accuracy estimand visible at the point of comparison

**Locations:** `paper/main.tex:62`, `paper/main.tex:109`, `paper/main.tex:163`, `paper/main.tex:169`, `paper/main.tex:183`.

The manuscript correctly distinguishes error of the pair median from mean error of individual responses. However, readers encounter “MAE,” “median-matrix accuracy,” “median-based MAE,” “English error,” and “Local error” across nearby sections. The local table's short headings can be mistaken for the same statistic as the global tables. The apparent change from English error near 165 km to 249 km for Spanish-associated pairs reflects both a different pair subset and a different estimand.

Use one consistent label, such as **pair-median MAE**, for the global statistic and **mean single-response absolute error** for the local statistic. In the local table caption or a table note, explicitly say both the subset and aggregation change. Introduce the subsection with:

> The global analysis evaluates the median of ten responses for each pair. The following exploratory analysis evaluates the expected error of one response on language-associated pairs.

The existing equation and bootstrap rationale should remain; this is a signposting issue, not a request to change the estimand or rerun the analysis.

### 6. Low: Reduce repeated defensive framing while preserving substantive limitations

**Locations:** `paper/main.tex:32`, `paper/main.tex:56`, `paper/main.tex:95`, `paper/main.tex:123`, `paper/main.tex:133`, `paper/main.tex:186`–`194`, `paper/main.tex:221`.

The paper repeatedly explains what was not claimed, not deleted, not inferred, or not chosen to maximize a result. Much of the content is scientifically useful, especially the strong exchangeability null, post hoc question formulation, and limited generalization. The cumulative phrasing nevertheless gives parts of the article the tone of a response to anticipated objections rather than a connected argument.

Replace rebuttal-like wording where the affirmative design statement already conveys the constraint. For example, replace “Our application of MDS to prompted geography is therefore not claimed as a first” with a direct account of how this study extends the cited prompting/MDS work. Replace the final sentence at line 221 with “All ten comparisons use the same complete-case subset.” Keep methodological limitations adjacent to the relevant methods, and reserve the discussion for their implications rather than repeating them verbatim.

Do not remove the distinction between behavioral geometry and hidden neural representations or the caveat that conditional call-level uncertainty is not population uncertainty across cities. Those are central interpretive safeguards, not unnecessary disclaimers.

### 7. Low: Tighten the scope of claims about language and local advantage

**Locations:** `paper/main.tex:47`, `paper/main.tex:162`, `paper/main.tex:165`, `paper/main.tex:186`, `paper/main.tex:204`.

The methods clearly state that one translated wording was used per language and English place names remained fixed. Later phrases such as “language-sensitive behavior” and “all instruction languages change the distance matrix” compress that limitation. “A general rule ... is therefore unsupported” can also be read as rejecting the rule broadly rather than finding insufficient support in this benchmark.

**Suggested conclusion wording:**

> Within this fixed 50-capital benchmark, the five translated instruction conditions produced distinguishable distance judgments under the conditional permutation test, even where aggregate accuracy was similar. An exploratory analysis found lower single-response error for Spanish-associated pairs under the Spanish prompt. The other language groups did not show the same benefit, so this study does not establish a general local-language advantage.

Use “translated instruction conditions” when discussing the estimated intervention and reserve broader language claims for proposed replication. This keeps the conclusion consistent with the actual design without adding more hedging sentences.

## Strengths to preserve

- The introduction clearly distinguishes accuracy, consistency, and stability, and acknowledges closely related prompting/MDS work.
- The paper explains that inference from API behavior does not identify hidden neural representations or a particular cognitive mechanism.
- Methods explicitly separate the old English model-comparison run from the new matched language baseline.
- The global permutation null and its limits are stated unusually clearly, including the distinction from a general equal-accuracy null.
- The local analysis discloses its exploratory timing, operational city-language groups, different estimand, and conditional uncertainty.
- The discussion appropriately avoids causal claims about training exposure or culture, and does not claim a unique latent dimensionality or global optimization guarantee.

## Suggested revision order

1. Rewrite the abstract and contribution paragraph around the questions and measured effects.
2. Add a concise geometry-results interpretation and standardize accuracy terminology.
3. Correct availability and move infrastructure detail to the supplement.
4. Consolidate repeated caveats while preserving the specific inferential limits.

No source, data, or manuscript files were modified by this reviewer.
