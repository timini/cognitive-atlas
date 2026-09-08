import numpy as np
from scipy.linalg import orthogonal_procrustes
from scipy.optimize import least_squares
from scipy.spatial.distance import pdist, squareform
from sklearn.manifold import MDS

RADIUS_KM = 6371.0088


def classical(d, dimensions=2):
    j = np.eye(len(d)) - np.ones_like(d) / len(d)
    eig, vectors = np.linalg.eigh(-0.5 * j @ (d ** 2) @ j)
    order = np.argsort(eig)[::-1][:dimensions]
    return vectors[:, order] * np.sqrt(np.maximum(eig[order], 0))


def stress(actual, target):
    idx = np.triu_indices(len(actual), 1)
    return float(np.sqrt(np.sum((actual[idx] - target[idx]) ** 2) / np.sum(target[idx] ** 2)))


def planar(d, dimensions=2, metric=True, seed=42):
    fit = MDS(n_components=dimensions, metric=metric, dissimilarity="precomputed", n_init=4,
              max_iter=1000, eps=1e-7, normalized_stress=True, random_state=seed)
    coords = fit.fit_transform(d)
    return coords, {"stress": float(fit.stress_), "iterations": int(fit.n_iter_),
                    "stress_definition": "sklearn_normalized_stress_against_distances" if metric else
                    "sklearn_normalized_stress_against_monotone_disparities"}


def align_planar(coords, reference):
    x, y = coords - coords.mean(axis=0), reference - reference.mean(axis=0)
    rotation, _ = orthogonal_procrustes(x, y)
    scale = np.sum((x @ rotation) * y) / np.sum(x * x)
    aligned = scale * x @ rotation + reference.mean(axis=0)
    return aligned, {"scale": float(scale), "rotation": rotation.tolist(),
                     "translation": (reference.mean(axis=0) - scale * coords.mean(axis=0) @ rotation).tolist(),
                     "residual_rmse": float(np.sqrt(np.mean(np.sum((aligned - reference) ** 2, axis=1))))}


def unit_vectors(latlon):
    lat, lon = np.radians(np.asarray(latlon)).T
    return np.column_stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])


def to_latlon(x):
    return np.degrees(np.column_stack([np.arcsin(np.clip(x[:, 2], -1, 1)), np.arctan2(x[:, 1], x[:, 0])]))


def spherical_distances(x):
    d = RADIUS_KM * np.arccos(np.clip(x @ x.T, -1, 1))
    np.fill_diagonal(d, 0)
    return d


def spherical(d, reference_latlon, seed=42, starts=4):
    # Initial geometry comes exclusively from judgments, never geographic reference.
    eig, vectors = np.linalg.eigh(np.cos(d / RADIUS_KM))
    x = vectors[:, -3:] * np.sqrt(np.maximum(eig[-3:], 1e-12))
    x /= np.linalg.norm(x, axis=1)[:, None]
    initial = np.radians(to_latlon(x)).ravel()
    idx = np.triu_indices(len(d), 1)
    rng = np.random.default_rng(seed)

    def points(angles):
        return unit_vectors(np.degrees(angles.reshape(-1, 2)))

    def residual(angles):
        return (spherical_distances(points(angles))[idx] - d[idx]) / RADIUS_KM

    best = None
    for attempt in range(starts):
        start = initial if attempt == 0 else initial + rng.normal(0, 0.3, initial.shape)
        fit = least_squares(residual, start, max_nfev=1000, ftol=1e-9, xtol=1e-9, gtol=1e-9)
        if best is None or fit.cost < best.cost:
            best = fit
    inferred = points(best.x)
    reference = unit_vectors(reference_latlon)
    # Orthogonal transform only: rotations/reflections of a fixed-radius sphere.
    rotation, _ = orthogonal_procrustes(inferred, reference)
    aligned = inferred @ rotation
    displacement = RADIUS_KM * np.arccos(np.clip(np.sum(aligned * reference, axis=1), -1, 1))
    return to_latlon(aligned), {"stress": stress(spherical_distances(inferred), d),
                              "stress_definition": "sqrt(sum((fitted-target)^2)/sum(target^2))",
                              "radius_km": RADIUS_KM, "starts": starts, "seed": seed,
                              "converged": bool(best.success), "function_evaluations": int(best.nfev),
                              "rotation": rotation.tolist(), "displacement_km": displacement.tolist(),
                              "mean_displacement_km": float(displacement.mean())}


def dimensionality(d, max_dimensions=10, seed=42):
    results = []
    for dimensions in range(1, min(max_dimensions, len(d) - 1) + 1):
        coords, detail = planar(d, dimensions, seed=seed)
        results.append({"dimensions": dimensions, "stress": stress(squareform(pdist(coords)), d),
                        "optimizer_stress": detail["stress"]})
    return results
