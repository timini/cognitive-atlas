# Cognitive Atlas

**What geography is implied by a language model’s judgments of distance?**

Cognitive Atlas asks a model to estimate distances between national capitals, then reconstructs the configuration of cities that best fits its answers. Repeated estimates distinguish geographic accuracy from internal consistency: a model can know many individual distances without describing a coherent world.

[Explore the atlas](https://timini.github.io/cognitive-atlas/) · [Read the paper](paper/cognitive-atlas-paper.pdf) · [Methods and reproduction](paper/README.md) · [Response to reviews](paper/REVIEW-RESPONSE.md)

## The study

Gemini 3.5 Flash estimates every unordered pair among **100 capitals**, with **ten responses per pair** under **English, Arabic, and written Chinese instructions**. The complete collection contains 148,500 answers; 148,491 pass the recorded validation rules. Instructions are translated while city and country names remain in English.

| Instructions | Pair-median mean absolute error | Spearman correlation | Triples violating triangle inequality |
|---|---:|---:|---:|
| English | 215.9 km | 0.99825 | 10.69% |
| Arabic | 234.0 km | 0.99809 | 13.30% |
| Chinese | 222.0 km | 0.99810 | 10.74% |

The error measure compares each pair’s median answer with its WGS84 geodesic distance. Strong rank agreement coexists with geometric inconsistency: among violated triples, the mean excess is approximately 323–421 km.

## What the maps show

Fitting the judgments to a sphere places capitals approximately **150–158 km** from their reference positions on average. The same method applied to the WGS84 reference distances gives a 9.5 km baseline displacement because the fitted sphere differs from the reference ellipsoid.

The English and Arabic maps differ by **81 km per capital** after global alignment; English and Chinese differ by **88 km**. These changes are subtle on a world map. Randomization tests reject a common response-distribution baseline, but cannot establish different underlying median maps: response variability can also contribute to rejection.

Exploratory regional comparisons show no observed accuracy gain under Arabic for pairs involving the 15 sampled Arab States capitals, or under Chinese for pairs involving Beijing or Singapore. The paper reports distance balancing, capital omissions, exclusion sensitivities, and the limitations of conditional uncertainty estimates.

## Explore the evidence

The atlas offers warped coastlines, fitted capitals, displacement vectors, error and variability layers, a pair explorer, and downloadable observations and matrices. Coastline deformation is an interpolation between fitted city positions; it is not directly elicited evidence about borders or land shapes.

The [paper](paper/README.md) contains the complete protocol, all 100 capitals, reference controls, statistical methods, and reproducible figures. Its conclusions concern observable judgments under these particular prompts. They do not identify a literal hidden neural map or establish a general effect of language.

## Scope and limitations

The capital sample is purposive. There is one assistant-authored translation per language, one model alias, and one collection period. Language and wording effects are inseparable, and provider-side independence is unverified.

This collection used whole-response numeric validation, not a provider-enforced output schema. Raw invalid responses are retained. New collection commands use a separate schema-constrained JSON condition. Ten observations per pair can miss rare answers; the paper’s method-calibration study demonstrates how unseen tails can undermine bootstrap uncertainty estimates.

To view the site locally, run `npm ci` followed by `npm run dev`. For collection, analysis, tests, and deployment, see the [development guide](docs/development.md). Geographic source hashes and capital-selection decisions accompany the [100-capital dataset](data/capitals-100-v3.sources.json).

The [submission dossier](publication/README.md) compares 18 journals, records their submission criteria and style requirements, and contains five AI-assisted assessments of the paper's publication readiness.
