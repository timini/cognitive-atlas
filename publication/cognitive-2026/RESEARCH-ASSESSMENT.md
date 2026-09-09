# What is interesting, and what evidence would change the paper?

Assessment of the 100-capital manuscript at `56fa5700fd65d7c0b911af1cce47debdbce62232`, 9 September 2026. This is an editorial and experimental-design judgment, not an acceptance prediction. No proposed experiment below has been run.

## The present contribution

There is a worthwhile cognitive-science question here: **how much of a language model's spatial knowledge behaves like a coherent, reusable geometry, and how much depends on the act of eliciting it?** Geography supplies an external reference that makes this question unusually testable. The map is a visualization of relational judgments; its appearance is not itself evidence for a psychological mechanism.

The present data are a substantial exploratory foundation, but I would not yet submit this version as a strong explanatory cognitive-science article. The main limitation is discrimination between explanations, not the number of observations. Reconstructing geography from language already has a direct cognitive-science precedent: Louwerse and Zwaan compared linguistic estimates of city locations and population with human judgments. Our contribution cannot be the first discovery that language carries spatial structure. [Original article](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1551-6709.2008.01003.x)

| Observation in the current paper | Why it is useful | What it does not establish |
|---|---|---|
| Pair-median MAE is 216–234 km; rank correlations exceed .998. | Provides a strong baseline of global order and numerical calibration against which structured errors can be studied. | Human-like cognition, use of coordinates, or novelty on its own. |
| 10.7–13.3% of triangles violate the triangle inequality. | Lets us examine the relation between locally accurate facts and collective consistency. | An exceptional cognitive deficit: the absolute-error-preserving sign controls average 11.5–12.3%. |
| English and Chinese have fewer violations than their artificial sign controls; Arabic has more. | The arrangement of signed errors deserves a planned replication, beyond comparing absolute error magnitudes. | A validated inferential finding about language, a neural mechanism, or evidence that the control is the true response process. |
| Fitted configurations differ by about 79–88 km per capital between instruction conditions. | Suggests a measurable elicitation-sensitivity question despite visually similar world maps. | Separate language effects, stable population median-map differences, or practical importance established by a small probability alone. |
| Neither regional group shows an observed absolute accuracy advantage under its associated translated prompt. | Prevents an attractive but unsupported linguistic-familiarity story and motivates a better operationalization. | A universal absence of language-related familiarity effects. The two-case Chinese group is especially narrow. |
| Ten observations per pair expose variation and occasional invalid answers. | Supports an analysis of the reliability of this measurement procedure. | Gaussian response laws, independent stationary sampling, calibrated rare-tail uncertainty, or replication across dates. |

These are fixed-dataset descriptions, drawn from the paper's Results and the saved error-control analysis. The response-distribution randomization results rely on exchangeability and cannot distinguish central-value changes from dispersion changes. The regional bootstrap audit failed an artificial rare-tail calibration; this is a warning about the method, not a discovery that the actual model has that tail law.

## Reframe the contribution before expanding it

A defensible working title is **“The Geometry of Spatial Judgments in a Language Model: Coherence, Distortion and Elicitation Context.”** Keep the singular until a matched multi-model experiment exists.

The introduction should develop competing accounts: coherent metric organization, ordinal relational knowledge with imperfect numerical calibration, and context-sensitive retrieval or heuristics. These accounts can coexist; experiments should compare their predictions rather than label one a proven internal implementation. Tversky's map-memory experiments illustrate how systematic spatial distortions can motivate explanations of judgment. They do not license attributing the same human heuristics to our model without corresponding tests. [Original paper](https://www.sciencedirect.com/science/article/pii/0010028581900165)

The discussion should ask which regularities survive changes in task, wording and collection occasion, and where coherence fails. Move execution audits to supplements while preserving methodological facts needed to assess the conclusions. Avoid an abstract dominated by call counts or an introduction organized chiefly around geospatial benchmarks. Keep effect sizes and null-model definitions visible. Neither caution nor an interactive atlas replaces a theoretical argument.

“Psychogeography” can convey the motivation to explore a distorted, elicited world. Its historical formulation also concerns environments' effects on emotion and behavior; those are not measured by capital-distance answers. Use cognitive geography or elicited spatial representation for the operational claim, and explain the relationship to psychogeography without claiming subjective experience. [Debord's original essay, in translation](https://www.theanarchistlibrary.org/library/guy-debord-introduction-to-a-critique-of-urban-geography)

## Would other models help?

**Yes—two additional model families would materially strengthen generalizability. They would not, by themselves, supply a cognitive explanation.** Two more Gemini versions mostly address within-family/version variation. A better comparison spans a Google model, a model from another provider, and an open-weight model with a pinned checkpoint where feasible. An OpenAI or Anthropic system is an example of the second family, not a claim that any particular currently marketed model is available in this repository. Verify availability, output-schema support, terms, settings and prices when preparing the run. Do not select models after seeing which yields the most striking distortion.

Select models before collection using a declared criterion, such as accessible general-purpose instruction models in a specified cost band. Treat them as three named systems, not a random sample supporting conclusions about all LLMs. Freeze exact served identifiers where supported and retain requested and returned IDs, timestamps and inference configuration. Identical numeric temperature settings do not guarantee comparable stochasticity across providers; report provider-specific sampling and reasoning controls as part of each condition.

Use the same 100 capitals and pairs. Retain the existing observations as the exploratory study. A new matched comparison should recollect the reference model alongside the added systems: comparing a new model today with an older alias snapshot confounds model with collection period and protocol. Use structured numeric output for all new conditions where supported, with raw responses and invalid attempts retained. The existing paper's collection was unconstrained text with whole-response validation; do not retrospectively describe it as schema-enforced. A schema requirement itself changes elicitation and belongs in the new condition metadata.

## What can be learned before another paid collection

The existing matrices could support an explicitly exploratory held-out-edge analysis: fit the spatial model using a training graph checked for connectivity and adequate geometric identifiability and compare predictions for the model's withheld pair judgments with prespecified calibration and geographic baselines. The prediction target is the elicited judgment, not the known reference distance, for which reference geography would trivially be correct. Repeating the split can describe sensitivity to which relationships were supplied. Because these data have already been inspected, this is not a confirmatory holdout or new task validation, and response-level splits do not manufacture independent model replications. It could nevertheless reveal whether geometric reconstruction improves prediction within the current numeric task and help design a more informative new collection. This analysis is proposed here, not reported as completed.

## The highest-value next experiment

My first choice is **a matched three-model experiment combining numerical distance judgments with independent comparative judgments, repeated across time blocks**. CogEval already demonstrates why behavioral cognitive claims benefit from multiple tasks and control conditions. A fitted map alone does not show that relational knowledge is used in a second task. [CogEval](https://arxiv.org/abs/2309.15129)

1. **Recover geometry from numerical judgments, then predict separately elicited choices.** Ask “Which is closer to A: B or C?” in fresh single-turn requests, with balanced option order. Select triplets in advance across reference-distance margins, regions and within/between-region relationships. Include diagnostic disagreements defined from training or pilot data and an unselected evaluation set; keep evaluation answers out of selection and tuning. Do not select only current dramatic errors. Compare choice predictions from reference geography, the training-only numeric geometry, and prespecified simpler baselines. Evaluate on held-out queries. A map that predicts systematic departures from reference geography is more informative about expressed judgment than one that merely looks like Earth. It still does not prove the model internally consulted the fitted map.
2. **Test numerical calibration separately from ordering.** Fit a scale or monotone calibration using training pairs only; compare held-out raw and calibrated errors with ordinal-choice performance. Accurate ordering combined with unstable kilometer estimates supports a behavioral calibration account. Because non-metric MDS still uses the ordering of the same numeric answers, the existing non-metric reconstruction is not this independent task test.
3. **Replicate elicitation, not just response slots.** Randomize model, language, pair and option order within synchronized collection blocks; spread ten repeats over, for example, five prespecified blocks of two. Repeated requests and time blocks remain nested within named models and fixed entities. Use additional wordings on a prespecified subset to estimate wording sensitivity. Native-speaker review should verify equivalent semantic content, including shortest surface distance and response instructions. Localized place names are a separate factor, not silently bundled with prompt language.
4. **Evaluate transfer with a defensible holdout.** Withheld pair edges can test prediction for the same capitals if the remaining graph supports fitting. Withholding an entire capital requires explicit anchor distances or a separate placement procedure; otherwise its location cannot be inferred from an empty row. Keep tuning and fitting out of the evaluation answers. Holdout results describe the declared entities/tasks, not unobserved countries or arbitrary cognitive domains.
5. **Prespecify the estimand and uncertainty procedure.** For a primary outcome, use held-out comparative-choice prediction by the elicited numeric geometry versus reference and calibration baselines, including effect size and block sensitivity. Plan sample size using simulations spanning ties, unequal variance, dependence and plausible rare responses. Resample at the level justified by the target claim; 4,950 pair edges are not independent people, and ten response slots are not ten independent models. A pair bootstrap alone does not address capital, wording, date or model generalization. Do not promise that an alternative bootstrap automatically repairs the current calibration problem.

This design can produce an informative negative result: if fitted distortions fail to predict fresh judgments while reference geography succeeds, the map may primarily summarize task-specific numerical error. If its departures predict choices across prompts and occasions, the case for stable behavioral organization becomes stronger. New-model convergence would then broaden that conclusion beyond one system.

## A practical staged budget

The arithmetic below counts logical response slots, not billed tokens or successful independent observations. Each new run still needs token/cost estimation and an approved spending cap; retries and provider-side thinking may add usage. These are planning examples, not power calculations or authorized execution.

| Stage | Design | Logical calls |
|---|---|---:|
| Family comparison alone, English | 3 models × 4,950 pairs × 10 repeats, including a fresh reference run | 148,500 |
| Full matched numeric study | 3 models × 3 languages × 4,950 pairs × 10 repeats | 445,500 |
| Independent comparative task | 3 models × 3 languages × 300 prespecified triplets × 10 repeats | 27,000 |
| Two extra instruction wordings | 3 models × 3 languages × 300 prespecified pairs × 2 additional wordings × 10 repeats | 54,000 |
| Additional tail/stability sampling | 3 models × 3 languages × 100 prespecified pairs × 40 additional repeats | 36,000 |

The full numeric design plus the three supplements totals **562,500** calls; the English-only alternative is not added again. Spread a fixed repeat budget across blocks rather than accidentally multiplying it by the block count. The subset sizes above need revision after design simulation. A lower-cost starting point is the English family comparison plus the comparative task in English (9,000 further calls), then expand language replication if the basic cross-task question is informative. That sequence should not suppress publication of an uninteresting first result.

Adding two models only to the existing three-language dataset would cost 297,000 logical numeric slots, but leaves the old/new period and protocol mismatch. I favor the fresh matched design over treating that cheaper comparison as a controlled model effect. No new requests have been made for this review task.

## A further discriminating study: novel relations

R05 proposes a separate controlled-learning extension: introduce unfamiliar place labels and a known artificial relational structure, change an edge or category cue, and test previously unprovided relations. This can challenge an explanation based solely on memorized capital-distance facts. It measures use of supplied relations in context, not the same construct as pre-existing world knowledge, and cannot retrospectively establish how the current capital answers were generated. It is a prospective option, not synthetic evidence inserted into the real-data paper.

## Optional human comparison and mechanism work

A matched human-judgment study would substantially improve a claim about human-like spatial distortions. Participants need not answer all 4,950 pairs: balanced incomplete blocks can cover prespecified diagnostic pairs and triplets, with geography familiarity and language proficiency measured. Participant sampling, burden, consent, ethics and power require a separate prospective design; current data cannot supply these facts. Human comparison is particularly useful for human-cognition venues, but is not a universal requirement for studying computational spatial cognition.

A pinned open-weight model also permits a separate mechanistic study with interventions. A recent preprint combines behavioral and mechanistic analyses of GPT-2 models trained on grid-navigation paradigms; that differs from observing general-purpose API distance judgments. Cite it as a preprint unless its publication status is verified, and do not borrow its causal conclusions for our system. [Baumgartner and colleagues, 2025](https://arxiv.org/abs/2511.13371)

The immediate priority is cross-task predictive validity and matched replication. Human comparison or mechanistic intervention should follow the intended explanatory claim, not become an arbitrary list of hurdles. More capitals, more decorative warping or more tiny p-values would be lower priorities now.
