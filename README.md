# Cognitive Atlas

**What geography is implied by a language model’s judgments of distance?**

Cognitive Atlas asks models to estimate distances between national capitals, then reconstructs the configuration of cities that best fits their answers. Repeated estimates let us distinguish geographic accuracy from internal consistency: a model can know many individual distances without describing a coherent world.

The interactive atlas compares the reconstructed cities with Earth and shows how the results change across models and prompt languages. Warped coastlines illustrate the inferred geometry; the city positions and distance matrices provide the underlying evidence.

[Explore the atlas](https://timini.github.io/cognitive-atlas/) · [Read the paper](paper/cognitive-atlas-paper.pdf) · [Paper source and analyses](paper/README.md) · [Review reports](reviews/README.md)

## The experiments

Every study asks about all unordered pairs in a fixed set of capitals, with ten separately sampled answers per pair. The language experiments change the full instructions while keeping city and country names in English.

| Study | Capitals | Pairs per condition | Conditions |
|---|---:|---:|---|
| Pilot | 20 | 190 | Gemini 2.5 Flash-Lite, English |
| Model comparison | 50 | 1,225 | Gemini 2.5 Flash-Lite, 3 Flash Preview, and 3.5 Flash; English |
| Language comparison | 50 | 1,225 | Gemini 3.5 Flash; English, French, Spanish, Arabic, and Mandarin Chinese |
| Expanded language comparison | 100 | 4,950 | Gemini 3.5 Flash; English, Arabic, and Mandarin Chinese |

The 100-capital collection contains 148,500 answers, of which 148,491 pass the recorded validation rules. Its analysis is separate from the paper’s original 50-capital study. Earlier experiments remain available in the atlas.

## What the results show

In the 50-capital model comparison, the mean absolute error of pairwise median estimates is approximately 938 km for Gemini 2.5 Flash-Lite, 163 km for Gemini 3 Flash Preview, and 159 km for Gemini 3.5 Flash. These are comparisons of particular model configurations, including different thinking controls.

In the expanded 100-capital study, the English and Arabic spherical maps differ by about **81 km per capital** after global alignment; English and Chinese differ by about **88 km**. These shifts are subtle on a world map. Randomization tests using map displacement reject exchangeability of the sampled response distributions (Holm-adjusted p = 0.003 for both comparisons). They do not distinguish changes in underlying median judgments from changes in response variability.

Different judgments do not necessarily imply a large change in accuracy. In the 100-capital comparison, Arabic’s median-based mean absolute error is about **18 km higher** than English’s; Chinese’s is about **6 km higher**, using pairs with ten valid answers in all three conditions. These are observed contrasts from one collection, not evidence that a language is generally better at geography.

The paper reports the original 50-capital comparisons and exploratory tests of regional language associations. The expanded study and direct map tests are subsequent analyses, with separate downloadable statistical audits in the atlas.

These findings describe the geography elicited by specific prompts and model runs. They do not establish a universal effect of language or reveal a literal representation inside a neural network.

## How the maps are reconstructed

1. **Elicit distances.** Each request asks for the shortest distance over Earth’s surface between two capitals. The complete responses, prompt text, settings, and returned model identifiers are retained.
2. **Measure accuracy and consistency.** Estimates are compared with WGS84 geodesic distances. The analysis examines sampling variation, distance correlations, triangle inequalities, and robust alternatives to averaging.
3. **Recover geometry.** Classical, metric, and non-metric multidimensional scaling provide planar reconstructions. A separate optimization fits cities on a sphere. Stress curves examine representations in one through ten dimensions.
4. **Align and compare.** Spherical fits are aligned using a single global rotation or reflection. Individual cities are not pulled toward their true positions during fitting. Capital displacement and distance disagreement quantify the remaining differences.

The coastlines are deformed using the fitted capitals as control points. That interpolation adds visual artifacts of its own, so the atlas also provides capital-only views, pair-level observations, uncertainty layers, and downloadable coordinates.

## Interpretation and limitations

The capitals are a geographically dispersed, purposive sample, not a representative sample of every place on Earth. Each language has one assistant-authored prompt translation, without independent native-speaker validation; wording and language effects cannot be separated. City names remain in English.

The published collections used unconstrained text responses followed by whole-response numeric validation, **not provider-enforced output schemas**. New collections default to a separate, versioned JSON-schema condition; historical observations are unchanged. Malformed responses and estimates above the recorded 20,040 km limit are excluded from fitted matrices but preserved in the source observations. The statistical analyses state their treatment of incomplete pairs. This selection rule can affect inference and is part of the experimental condition.

The significance tests condition on these capitals, translations, and observations, assuming independent calls. They do not capture uncertainty across new prompts, collection dates, or model releases. Saved observations make the reported calculations reproducible; an API model alias does not guarantee that a future collection will use identical weights.

## Explore or reproduce the work

The [atlas](https://timini.github.io/cognitive-atlas/) provides the original responses, distance matrices, reconstructed coordinates, experiment metadata, and statistical audits for each published condition. The [paper directory](paper/README.md) contains the LaTeX manuscript, figures, analysis scripts, and its frozen list of source experiments.

To view the site locally:

```sh
npm ci
npm run dev
```

For running experiments, reproducing analyses, tests, and deployment, see the [development guide](docs/development.md). Geographic sources and capital-selection decisions are recorded alongside the [capital datasets](data/).

## Sources

Capital coordinates and coastlines come from [Natural Earth](https://www.naturalearthdata.com/). Ground-truth distances use [GeographicLib](https://geographiclib.sourceforge.io/Python/doc/code.html); planar reconstructions use [scikit-learn’s MDS implementation](https://scikit-learn.org/1.7/modules/generated/sklearn.manifold.MDS.html). Related research and methodological references are collected in the [paper bibliography](paper/references.bib).
