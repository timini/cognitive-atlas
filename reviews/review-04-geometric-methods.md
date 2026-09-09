# Review 04: Geospatial reconstruction and geometric interpretation

Reviewed 9 September 2026 against working files at commit `e987efabad1a2b9a53f737e6bc71a13684ae3f9f`. Scope: the **frozen 50-capital manuscript**, the reconstruction/deformation implementation, and the website's presentation of those methods. New 100-capital results are a separate extension; none of the numerical checks below establishes their findings.

**Recommendation: minor manuscript revision, with two medium-priority website corrections.** I found no critical error in the spherical objective, analytic derivative, global alignment, or published spherical stress and triangle-violation values. The manuscript's restraint concerning latent dimensionality, identification and coastline interpretation is justified. The outstanding issues primarily concern making the diagnostic definitions and reference baselines equally clear in the public interface.

## Findings

### G1 — Medium: the same website label displays different stress normalizations

**Locations:** `atlas/reconstruct.py:18–29`, `atlas/reconstruct.py:103–104`, `atlas/analysis.py:103–111`, `app/page.tsx:44–45`; compare the explicit spherical definition in `paper/main.tex:79–83`.

Classical MDS and spherical fits use `sqrt(sum((fitted-target)^2)/sum(target^2))`. Metric MDS returns scikit-learn Stress-1, whose denominator is the sum of squared **fitted** distances. The installed scikit-learn implementation confirms this at `.venv/lib/python3.12/site-packages/sklearn/manifold/_mds.py:185–187`. The UI labels all three “Reconstruction stress” and does not display the exported `stress_definition`.

**Evidence:** for matched 50-capital English, metric MDS displays `0.15010570232048429`, whereas recomputing the paper's target-normalized definition on its saved raw coordinates gives `0.1484426800018594`. Arabic gives `0.15417352874225182` versus `0.15237324433270577`. These are both valid diagnostics, but switching algorithms changes the denominator as well as the fit. Nonmetric stress is separately labeled “Ordinal stress”; that distinction is already good.

**Correction:** export and show one common target-normalized residual for metric/classical/spherical comparisons, retaining optimizer Stress-1 under an explicit separate label. Alternatively expose the precise definition adjacent to each value and warn against comparing unlike normalizations. The manuscript's spherical tables are correct and do not require numerical correction.

### G2 — Medium: the website omits the Earth reference curve that protects the paper's dimensionality interpretation

**Locations:** `app/page.tsx:47`; `atlas/analysis.py:72,129–130`; `paper/scripts/build_assets.py:199–223`; `paper/main.tex:158,192`.

The website plots only the estimated-distance dimensionality curve even though the same export contains `true_earth_dimensionality`. The manuscript figure correctly includes the WGS84 curve and says that great-circle distances retain residual Euclidean stress. That protection is especially relevant to an exploratory interface asking about the “shape of the geometry.”

**Evidence:** in the matched English export, 3D target-normalized MDS stress is approximately `0.090295`; the corresponding WGS84 baseline is `0.08312498336`. At 10D they are approximately `0.090303` and `0.08313136884`. Much of the residual is therefore present in the actual distance geometry. This is not a direct estimate of an extra semantic component, and subtracting these values is not itself a validated decomposition.

**Correction:** draw the stored WGS84 curve on the website with the same axes and an explicit legend. Keep the paper's current caveat. Do not infer a latent dimensionality or an exact semantic-error fraction from either curve.

### G3 — Low: quantify the spherical-reference mismatch when presenting capital displacement

**Locations:** `paper/main.tex:42,73–83,192`; `atlas/reconstruct.py:98–109`.

The paper correctly notes that fixed-radius spherical fitting differs from ellipsoidal ground truth, but readers are not shown the magnitude of the resulting position baseline. Alignment also minimizes squared Euclidean **chord** residuals of unit vectors, not mean or squared geodesic displacement; the latter is measured afterward. This is a defensible extrinsic alignment, not an implementation error, and should be stated explicitly.

**Independent check on the frozen 50 capitals:** great-circle distances at the unchanged reference latitude/longitude have MAE `10.18270388 km` against WGS84, maximum error `35.57071653 km`, and target-normalized stress `0.00134817430`. Applying the actual spherical fitter to the WGS84 matrix produces stress `0.00037106645` and mean aligned displacement **`9.68763225 km`**, despite supplying ideal reference distances as judgments.

**Correction:** add the fitted-WGS84 spherical baseline to the supplement, and clarify that absolute fitted-capital displacement contains reference-model mismatch. Do not subtract 9.69 km from every observed displacement: the shifts are vectors and the mismatch varies by capital. Language-to-language comparisons share the reference convention, but that alone is not a proof that every baseline effect cancels. The existing language permutation tests concern distance judgments, not these baseline displacements.

The extrinsic Procrustes interpretation follows the [SciPy orthogonal Procrustes definition](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.orthogonal_procrustes.html), which minimizes a Frobenius norm using rotations/reflections.

### G4 — Low: negative cosine eigenmass alone cannot diagnose compatibility with a two-dimensional sphere

**Locations:** `atlas/statistics.py:49–62`; `paper/main.tex:69`.

The implementation exports the negative eigenmass of `cos(D/R)` but neither its spectrum nor the positive mass beyond its leading three eigenvalues. For an exact embedding on `S²`, the cosine Gram matrix must be positive semidefinite **and have rank at most three**, subject to the angular-distance domain. A zero negative eigenmass alone only addresses the first condition. The paper calls these quantities diagnostics and explicitly avoids an identification claim, so this is a completeness improvement, not a refutation of its text.

**Counterexample:** four cities with every off-diagonal distance equal to `R*pi/2` have cosine Gram matrix equal to the 4×4 identity up to floating-point error. The exported spherical negative eigenmass is `0.0`, but rank is four, precluding an exact `S²` embedding. The current fitter with twelve starts obtains residual stress approximately `0.21634690`. This constructed matrix is a mathematical test case, not a model measurement.

**Correction:** retain the full eigenvalue spectrum or report positive tail mass beyond rank three, along with an explicit numerical tolerance and distance-domain check. Avoid labeling negative eigenmass alone as “spherical validity.”

### G5 — Low: save per-start optimization diagnostics for future difficult datasets

**Locations:** `atlas/reconstruct.py:90–107`; `paper/main.tex:77,192`.

Only the winning spherical fit's convergence flag and function-evaluation count are retained. The four starts are one spectral initialization and three perturbations with standard deviation 0.3 radians; they are not four unrelated global initializations. The paper correctly says that four starts do not prove global optimality. Keeping all start costs, termination reasons and optimality measures would make the local-minimum sensitivity auditable, particularly for the expanded dataset or less coherent future models.

**Independent robustness check:** refitting the matched English and Arabic matrices with seed `20260909` and **12 starts**, then globally aligning each new fit to its saved fit, gives:

| Language | Saved stress | 12-start stress | Mean capital shift | Maximum capital shift |
|---|---:|---:|---:|---:|
| English | 0.02605303926478105 | 0.026053039263791374 | 0.002357 km | 0.025575 km |
| Arabic | 0.03216020628355307 | 0.03216020628276333 | 0.001625 km | 0.014289 km |

Both refits converge. This supports numerical stability for these two frozen matrices; it does not prove global optimality or validate every other aggregation/cohort.

## Verified strengths and boundaries

- Recomputed all eight 50-capital median spherical stresses directly from saved inferred coordinates and distance matrices: agreement within `2.8e-17`. All saved winning fits report convergence. Triangle-violation recomputation agrees with the exports; 19,600 triples are exhaustively enumerated for 50 capitals.
- The sparse analytic Jacobian matches the angular residual, and the fitting objective never uses true city positions as anchors. Reference coordinates enter only after fitting, through a single orthogonal transform. Fixed-radius alignment preserves the fitted pairwise spherical distances.
- The manuscript correctly distinguishes arc distances from Euclidean chords, imposed symmetry from tested symmetry, numerical stress from latent-dimensionality identification, and distance-level inference from whole-map inference.
- Piecewise-affine deformation is continuous on adjacent mesh triangles because they share mapped vertices. It is not guaranteed injective or topology preserving. The original median 2.5/3/3.5 model fits report respectively 5/1/0 folded triangles; all five matched-language median fits report 0. The paper and UI already disclose folds and the illustrative status of coastlines. Fixed frame pins and the equirectangular seam remain display assumptions, not elicited knowledge.
- `python -m pytest -q tests/test_comparison.py tests/test_pipeline.py` using `.venv/bin/python`: **24 passed**. This includes independent finite-difference derivative checking, sphere reconstruction, rotation invariance and planar alignment.

## Reproduction of the numerical checks

Use only the entries in `paper/experiment-index.json`, not the changing public experiment index. For each exported `result.json`, construct symmetric matrices from `pairs[*].median` and `pairs[*].true_distance_km` using the order in `places`.

```python
import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.spatial.distance import pdist, squareform
from atlas.reconstruct import RADIUS_KM, spherical, spherical_distances, stress, unit_vectors

# r is a frozen result.json, d its median matrix, truth its WGS84 matrix.
layer = r["layers"]["median"]
saved = layer["reconstructions"]["spherical"]
assert abs(stress(spherical_distances(unit_vectors(saved["inferred_latlon"])), d)
           - saved["stress"]) < 1e-12
xy = np.array(layer["reconstructions"]["metric"]["raw_coordinates"])
print(stress(squareform(pdist(xy)), d))  # Common target-normalized metric stress.
ll = np.array([[p["latitude"], p["longitude"]] for p in r["places"]])
print(spherical(truth, ll, seed=42, starts=4)[1])  # Spherical WGS84 baseline.
new_ll, detail = spherical(d, ll, seed=20260909, starts=12)
x, y = unit_vectors(new_ll), unit_vectors(saved["inferred_latlon"])
rotation, _ = orthogonal_procrustes(x, y)
shifts = RADIUS_KM * np.arccos(np.clip(np.sum((x @ rotation) * y, axis=1), -1, 1))
print(detail["stress"], shifts.mean(), shifts.max())
```

No model calls, synthetic research observations, edits to research results, or changes to the manuscript were made in this review.
