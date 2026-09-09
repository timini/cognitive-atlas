# Academic review 01: empirical claims and numerical fidelity

**Recommendation:** minor revision for the numerical reporting reviewed here. I found no incorrect empirical point estimate, sample total, reported confidence interval, or adjusted significance value in the frozen 50-capital paper. This is not an endorsement of generalization beyond the stated sampling assumptions.

**Scope:** `paper/main.tex`, every generated numerical table, `paper/results/`, the nine experiments pinned by `paper/experiment-index.json`, their raw response CSVs, and their reconstructed coordinates. Reviewed on 9 September 2026 against source HEAD `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`. The newer 100-capital collection is a separate study and was not substituted into the historical paper. Related-work attribution, typography, and the mathematical adequacy of alternative inferential methods are outside this review's primary remit.

## Findings requiring revision

### 1. Medium — the data-availability statement no longer describes the deployed study

**Evidence:** `paper/main.tex:201` says the hosted atlas is an access-controlled interface and disclaims public data availability. The current project instead advertises a public GitHub Pages atlas at `README.md:9`, and `README.md:53` identifies its downloadable original responses, matrices, coordinates, metadata, and audits. The manuscript's private repository statement is a different question from whether the exported research data are publicly accessible. `paper/README.md:93` should also be reconciled with the actual distinction between publicly downloadable data and a permanent archive.

**Consequence:** an outside reader is incorrectly told that the evidence supporting the numerical claims is inaccessible. The manuscript also fails to identify the public location at which its frozen exports can be obtained.

**Correction:** identify the public atlas and the exact frozen dataset/export identifiers, separately state the source repository's actual access status, and retain the accurate qualification that there is no permanent archival DOI. Do not imply that a live deployment is a preservation archive. If preserving the original PDF unchanged as a dated historical artifact, add a dated availability addendum rather than quietly changing its empirical study.

### 2. Minor — the abstract describes differences as “substantial” without providing their magnitude

**Evidence:** `paper/main.tex:26` uses “substantial changes in individual estimates” immediately after the adjusted permutation significance result. `paper/main.tex:153` supplies the more informative Mandarin comparison: 122.3469 km mean absolute disagreement of pair medians and only 0.6999 km difference in aggregate median-based MAE. `paper/generated/pairwise-table.tex:1` through its final row show disagreement ranging from 80.5724 to 133.5874 km across the ten comparisons. These are changes in elicited distance estimates, not a direct estimate of the separation of reconstructed city positions.

**Consequence:** readers scanning the abstract can confuse detectability with a large visible change in the reconstructed world. This is especially relevant to interpreting the English and Arabic maps.

**Correction:** replace the qualitative adjective with a numerical effect-size statement, for example: “Mean absolute disagreement between language-specific pair medians ranged from 80.6 to 133.6 km, while similar aggregate accuracy could conceal different pairwise errors.” Preserve the distinction from an inferential test of whole-map geometry; the historical paper correctly says that it did not perform one at `paper/main.tex:190`.

## Claims that pass verification

I independently recomputed descriptive quantities from accepted rows in the **raw CSV files**, rather than only comparing manuscript numbers with generated result summaries. For every pinned experiment, each exported pair's sample list equaled the raw CSV's accepted values. Recomputed WGS84 distances had a maximum discrepancy of **0 km** from the stored ground truth at the precision represented by the input coordinates.

### Sample accounting and provenance

- `paper/main.tex:40`–`42`: the main sample has 50 capitals, 1,225 unordered pairs, and six inhabited continents. The appendix lists the actual 50 selected cities. The 20-capital pilot is separately identified.
- `paper/main.tex:51`: response timestamps run from 16:56:25 UTC to 17:35:52 UTC on 8 September 2026, supporting the stated approximate collection window.
- `paper/main.tex:54`–`56`: the language study contains **61,251 attempts, 61,250 terminal sample slots, and 61,237 accepted estimates**. There are 11 range failures, two numeric-format failures, and one transport timeout. The timeout is not an extra completed sample.
- The complete-case subset contains **1,223 pairs × 10 responses × 5 languages = 61,150 observations**. Exactly `AR--VN` and `KR--RU` are excluded. The retried `ET--PE` transport timeout does not require excluding that pair because its replacement was valid.
- `paper/main.tex:199`: summing recorded usage estimates gives **US$9.856872**, supporting the stated approximate US$9.86 and its qualification as an estimate rather than an invoice.

### Full-matrix model and language results

The following quantities were recomputed from CSV pair medians and GeographicLib ground truth. All agree with the rounded tables at `paper/generated/model-table.tex:1` and `paper/generated/language-table.tex:1`.

| Condition | Valid observations | Median-matrix MAE, km | Spearman | Violated triangles, % |
|---|---:|---:|---:|---:|
| Original English 2.5 Flash-Lite | 12,241 | 937.983002 | 0.967032225 | 17.030612 |
| Original English 3 Flash Preview | 12,250 | 163.223031 | 0.998212922 | 10.127551 |
| Original English 3.5 Flash | 12,250 | 159.044837 | 0.998614704 | 9.260204 |
| Matched English | 12,244 | 164.575721 | 0.998536108 | 10.045918 |
| Matched French | 12,246 | 157.782991 | 0.998550732 | 9.607143 |
| Matched Spanish | 12,248 | 167.395980 | 0.998553792 | 9.908163 |
| Matched Arabic | 12,249 | 186.847346 | 0.998220149 | 12.204082 |
| Matched Mandarin | 12,250 | 165.241056 | 0.998388784 | 10.045918 |

All **19,600** triples were independently enumerated for each 50-capital condition, verifying the denominator at `paper/main.tex:69`. I also reconstructed spherical pairwise arc distances directly from the exported inferred latitude/longitude coordinates and recomputed the normalized stress formula at `paper/main.tex:79`. All eight main-study spherical stress values agree with the reported values, to floating-point precision. This checks reported fit residuals; it does not prove global optimality of the optimizer.

### Global language inference and the Mandarin claim

- All ten absolute median disagreements and signed MAE differences in `paper/generated/pairwise-table.tex:1` were independently recomputed on the common subset.
- English versus Arabic: disagreement **107.255724 km**, Arabic-minus-English MAE **+20.882787 km**.
- English versus Mandarin: disagreement **122.346852 km**, Mandarin-minus-English MAE **+0.699946 km**. This supports `paper/main.tex:153`: distinguishably different judgments can have almost identical overall error.
- I reran all 4,999 permutations for each of the ten comparisons, intercepting output writes to compare the generated report with the saved audit. The audit reproduced **exactly**, including every null summary, Monte Carlo tail count, and all twenty Holm-adjusted values. All ten disagreement tests have adjusted **p = 0.004**. This equality is indeed a consequence of the discrete Monte Carlo calculation and adjustment, not identical effect sizes.
- The strong exchangeability null and the restriction on interpreting the MAE-contrast test are stated accurately at `paper/main.tex:93`–`95`. This numerical reproduction does not validate unobserved independence of provider requests.

### Local-language effects, intervals, and sensitivity

The local estimates at `paper/main.tex:163`–`183` and both local/sensitivity tables match independent recomputation from single-response absolute errors:

| Language | Associated complete pairs | Associated-pair gain, km | Interaction, km |
|---|---:|---:|---:|
| French | 190 | −5.000842 | −11.027976 |
| Spanish | 278 | +17.358247 | +24.522612 |
| Arabic | 190 | −22.696178 | +0.280602 |
| Mandarin | 97 | −10.536281 | −6.342536 |

Spanish-associated error falls from **248.980111** to **231.621864 km**, a **6.971740%** reduction. Its other-pair gain is **−7.164365 km**, so the positive 24.522612 km interaction is arithmetically correct. Removing each associated capital gives Spanish gains of **13.113919–25.055014 km** and interactions of **20.278284–32.219379 km**. The stated French and Mandarin sign changes also occur.

I reran the full 9,999-replicate local bootstrap, again preventing file writes. It reproduced the saved audit **exactly**, including all intervals, analytic/bootstrap standard errors, and adjusted p values. Spanish's gain interval is **[9.720182, 25.135946] km**; its interaction interval is **[16.192988, 32.785560] km**. Both adjusted p values are **0.0008**. The manuscript correctly separates pointwise intervals from multiplicity-adjusted tests and the single-response estimand from the median-matrix estimand.

### Geographic signal and distributional wording

`paper/main.tex:123` and `paper/main.tex:133` pass. All three 9,999 city-label permutation audits reproduced exactly, yielding **p = 0.0001** each. The original 3.5 Flash condition has exactly **154/1,225** pairs with ten identical responses. London–Paris is **344 km** in all ten, compared with **341.149815 km** WGS84 truth. The wording rules out an *unrounded continuous* Gaussian account of these reported numbers while correctly declining to infer the underlying response distribution from ten samples. It does not claim that rounding a continuous latent variable is impossible.

## Reproduction procedure

Descriptive checks used Python's `csv` reader, NumPy medians/absolute errors, SciPy `spearmanr`, GeographicLib's WGS84 inverse solution, explicit combinations of three capital IDs, and the exported spherical coordinates. No model calls were made and no data or implementation files were edited.

The following command reproduces the three saved inferential audits without overwriting them. Exact equality includes reported point estimates, intervals, and p values; a source hash alone is not treated as evidence of numerical agreement.

```sh
.venv/bin/python - <<'PY'
import contextlib, io, json, runpy
from pathlib import Path

def compare_only(path, content, *args, **kwargs):
    before, after = json.loads(path.read_text()), json.loads(content)
    assert before == after, str(path)
    return len(content)

Path.write_text = compare_only
for script in ['check_distance_structure.py',
               'check_language_differences.py', 'local_language.py']:
    with contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path('paper/scripts/' + script, run_name='__main__')
    print('Reproduced:', script)
PY
```

## Interpretation

The numerical evidence supports the paper's deliberately conditional conclusions: strong geographic signal, observable differences between these particular language prompts, and an exploratory Spanish-associated accuracy benefit in this fixed sample. It does **not** establish different literal neural maps, a general cultural mechanism, population-wide language advantages, or normal response distributions. The manuscript generally draws these boundaries correctly. The two requested revisions concern current availability and clearer effect-size communication, not reversal of the reported empirical results.
