"""Reproduce the 100-capital geometric checks without model calls.

Run from any directory using the repository's locked Python environment.
Only geometry.json beside this script is written. Fits are in-sample descriptive
diagnostics. Additional starts do not establish global optimality or uniqueness.
"""

import hashlib
import importlib.metadata
import json
import os
import platform
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from geographiclib.geodesic import Geodesic
from scipy.linalg import orthogonal_procrustes
from scipy.optimize import least_squares
from scipy.sparse import csr_matrix

ROOT = Path(__file__).resolve().parents[2]
RADIUS_KM = 6371.0088
SEED = 42
EXPORTS = {
    "en": "3b382690950b9511f5806ebc-114bbc2e2e5a9331",
    "ar": "b2e583773ba8111b0607ae88-3ef8ee3db9b488b1",
    "zh": "2ee0bcb921b94263ac26e635-bae2d55a858255c4",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def unit_vectors(latlon):
    lat, lon = np.radians(np.asarray(latlon)).T
    return np.column_stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])


def latlon(points):
    return np.degrees(np.column_stack([
        np.arcsin(np.clip(points[:, 2], -1, 1)), np.arctan2(points[:, 1], points[:, 0])
    ]))


def arc_distances(points):
    distance = RADIUS_KM * np.arccos(np.clip(points @ points.T, -1, 1))
    np.fill_diagonal(distance, 0)
    return distance


def normalized_stress(fitted, target):
    upper = np.triu_indices(len(target), 1)
    return float(np.sqrt(np.sum((fitted[upper] - target[upper]) ** 2) / np.sum(target[upper] ** 2)))


def displacement(first, second, align=True):
    rotation = orthogonal_procrustes(first, second)[0] if align else np.eye(3)
    rotated = first @ rotation
    # atan2 is stable for the sub-metre solver differences checked here.
    values = RADIUS_KM * np.arctan2(np.linalg.norm(np.cross(rotated, second), axis=1),
                                  np.sum(rotated * second, axis=1))
    return {
        "mean_km": float(values.mean()), "median_km": float(np.median(values)),
        "max_km": float(values.max()), "per_capital_km": values.tolist(),
        "rotation": rotation.tolist(),
    }


def nearest_three(distance, truth):
    # Explicitly exclude self, rather than relying on its sort position.
    d, t = distance.copy(), truth.copy()
    np.fill_diagonal(d, np.inf)
    np.fill_diagonal(t, np.inf)
    a, b = np.argsort(d, axis=1, kind="stable")[:, :3], np.argsort(t, axis=1, kind="stable")[:, :3]
    overlaps = [len(set(x) & set(y)) / 3 for x, y in zip(a, b)]
    return {"mean_fraction": float(np.mean(overlaps)), "per_capital_fraction": overlaps,
            "k": 3, "tie_policy": "stable order of canonical capital IDs"}


def triangle_checks(distance):
    triples = np.asarray(list(combinations(range(len(distance)), 3)))
    sides = np.sort(np.column_stack([
        distance[triples[:, 0], triples[:, 1]], distance[triples[:, 0], triples[:, 2]],
        distance[triples[:, 1], triples[:, 2]],
    ]), axis=1)
    excess = np.maximum(0, sides[:, 2] - sides[:, 0] - sides[:, 1])
    violation = excess > 1e-7
    positives = excess[violation]
    return {
        "triples": len(triples), "violation_tolerance_km": 1e-7,
        "violated_triples": int(violation.sum()), "violation_rate": float(violation.mean()),
        "mean_excess_all_triples_km": float(excess.mean()),
        "max_excess_km": float(excess.max()),
        "mean_excess_violated_triples_km": float(positives.mean()) if len(positives) else None,
        "conditional_violation_percentiles_km": {
            str(q): float(np.percentile(positives, q)) if len(positives) else None
            for q in [0, 25, 50, 75, 90, 95, 99, 100]
        },
    }


def cosine_checks(distance):
    eigenvalues = np.linalg.eigvalsh(np.cos(distance / RADIUS_KM))
    tolerance = 100 * len(distance) * np.finfo(float).eps * max(1.0, float(np.max(np.abs(eigenvalues))))
    positive = eigenvalues[eigenvalues > tolerance][::-1]
    negative = eigenvalues[eigenvalues < -tolerance]
    absolute_mass = float(np.abs(eigenvalues).sum())
    domain = {
        "all_finite": bool(np.isfinite(distance).all()),
        "symmetric_max_abs_error_km": float(np.max(np.abs(distance - distance.T))),
        "diagonal_max_abs_error_km": float(np.max(np.abs(np.diag(distance)))),
        "min_offdiagonal_km": float(distance[np.triu_indices(len(distance), 1)].min()),
        "max_offdiagonal_km": float(distance.max()),
        "max_short_arc_km": float(np.pi * RADIUS_KM),
        "above_short_arc_limit_pairs": int(np.sum(distance[np.triu_indices(len(distance), 1)] > np.pi * RADIUS_KM)),
    }
    domain_valid = (domain["all_finite"] and domain["symmetric_max_abs_error_km"] < 1e-7
                    and domain["diagonal_max_abs_error_km"] < 1e-7
                    and domain["min_offdiagonal_km"] >= 0 and domain["above_short_arc_limit_pairs"] == 0)
    return {
        "domain": domain, "domain_valid": domain_valid,
        "eigenvalues_ascending": eigenvalues.tolist(), "eigenvalue_tolerance": tolerance,
        "tolerance_definition": "100 * N * machine_epsilon * max(1, spectral_radius)",
        "negative_eigenvalue_count": len(negative), "positive_rank": len(positive),
        "negative_eigenmass_fraction": float(np.abs(negative).sum() / absolute_mass),
        "positive_eigenmass_beyond_rank3": float(positive[3:].sum()),
        "positive_eigenmass_beyond_rank3_fraction_of_all_absolute_mass": float(positive[3:].sum() / absolute_mass),
        "rank3_psd_residual_frobenius_relative": float(
            np.sqrt(np.sum(negative ** 2) + np.sum(positive[3:] ** 2)) / np.linalg.norm(eigenvalues)
        ),
        "exact_sphere_compatible_within_tolerance": bool(domain_valid and not len(negative) and len(positive) <= 3),
        "interpretation": "Short-arc distances on this fixed-radius two-sphere require a PSD cosine Gram matrix of rank at most three. Negative mass alone does not test rank. Rank-three truncation need not preserve a unit diagonal, so its residual is a diagnostic, not a fitted spherical stress.",
    }


def angular_jacobian(angles):
    lat, lon = np.asarray(angles).reshape(-1, 2).T
    points = np.column_stack([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])
    dlat = np.column_stack([-np.sin(lat) * np.cos(lon), -np.sin(lat) * np.sin(lon), np.cos(lat)])
    dlon = np.column_stack([-np.cos(lat) * np.sin(lon), np.cos(lat) * np.cos(lon), np.zeros_like(lat)])
    i, j = np.triu_indices(len(lat), 1)
    dot = np.sum(points[i] * points[j], axis=1)
    values = np.column_stack([
        np.sum(dlat[i] * points[j], axis=1), np.sum(dlon[i] * points[j], axis=1),
        np.sum(points[i] * dlat[j], axis=1), np.sum(points[i] * dlon[j], axis=1),
    ]) * (-1 / np.sqrt(np.maximum(1 - dot * dot, 1e-14)))[:, None]
    columns = np.column_stack([2 * i, 2 * i + 1, 2 * j, 2 * j + 1])
    return csr_matrix((values.ravel(), (np.repeat(np.arange(len(i)), 4), columns.ravel())),
                      shape=(len(i), 2 * len(lat)))


def fit_sphere(distance, reference, starts):
    # Independent instrumentation of the archived algorithm; no atlas imports.
    eigenvalues, eigenvectors = np.linalg.eigh(np.cos(distance / RADIUS_KM))
    initial_points = eigenvectors[:, -3:] * np.sqrt(np.maximum(eigenvalues[-3:], 1e-12))
    initial_points /= np.linalg.norm(initial_points, axis=1)[:, None]
    initial = np.radians(latlon(initial_points)).ravel()
    upper = np.triu_indices(len(distance), 1)
    rng = np.random.default_rng(SEED)
    points_by_start, records = [], []

    def points(angles):
        return unit_vectors(np.degrees(angles.reshape(-1, 2)))

    def residual(angles):
        return (arc_distances(points(angles))[upper] - distance[upper]) / RADIUS_KM

    for index in range(starts):
        initial_angles = initial if index == 0 else initial + rng.normal(0, 0.3, initial.shape)
        fit = least_squares(residual, initial_angles, jac=angular_jacobian, max_nfev=1000,
                            ftol=1e-9, xtol=1e-9, gtol=1e-9)
        fitted = points(fit.x)
        points_by_start.append(fitted)
        records.append({
            "start": index + 1, "converged": bool(fit.success), "status": int(fit.status),
            "message": str(fit.message), "function_evaluations": int(fit.nfev),
            "jacobian_evaluations": int(fit.njev), "optimality": float(fit.optimality),
            "cost_half_sum_squared_angular_residuals": float(fit.cost),
            "sum_squared_km_residuals": float(2 * fit.cost * RADIUS_KM ** 2),
            "normalized_target_stress": normalized_stress(arc_distances(fitted), distance),
            "aligned_true_displacement": displacement(fitted, reference),
        })
    best_four = min(range(4), key=lambda i: records[i]["cost_half_sum_squared_angular_residuals"])
    best_all = min(range(starts), key=lambda i: records[i]["cost_half_sum_squared_angular_residuals"])
    for index, record in enumerate(records):
        record["aligned_displacement_from_best_start"] = displacement(points_by_start[index], points_by_start[best_all])
    return {
        "starts": records, "all_starts_converged": all(r["converged"] for r in records),
        "best_first_four_start": best_four + 1, "best_all_start": best_all + 1,
        "first_four_to_all_displacement": displacement(points_by_start[best_four], points_by_start[best_all]),
        "best_first_four_stress": records[best_four]["normalized_target_stress"],
        "best_all_stress": records[best_all]["normalized_target_stress"],
        "best_aligned_true_displacement": displacement(points_by_start[best_all], reference),
        "best_aligned_inferred_latlon": latlon(points_by_start[best_all] @ orthogonal_procrustes(points_by_start[best_all], reference)[0]).tolist(),
    }, points_by_start[best_four], points_by_start[best_all]


def matrices(result, places):
    ids = {place["id"]: i for i, place in enumerate(places)}
    truth = np.zeros((len(places), len(places)))
    median = truth.copy()
    assert len(result["pairs"]) == len(places) * (len(places) - 1) // 2
    seen = set()
    for pair in result["pairs"]:
        i, j = ids[pair["place_a_id"]], ids[pair["place_b_id"]]
        assert i != j and tuple(sorted((i, j))) not in seen
        seen.add(tuple(sorted((i, j))))
        truth[i, j] = truth[j, i] = pair["true_distance_km"]
        median[i, j] = median[j, i] = np.median(pair["samples"])
        assert median[i, j] == pair["median"]
    return truth, median


def main():
    paths = {language: ROOT / "public/data" / export / "result.json" for language, export in EXPORTS.items()}
    results = {language: json.loads(path.read_text()) for language, path in paths.items()}
    places = results["en"]["places"]
    assert len(places) == 100
    assert all(r["places"] == places for r in results.values())
    reference = unit_vectors([[p["latitude"], p["longitude"]] for p in places])
    truth, _ = matrices(results["en"], places)
    independent_truth = np.zeros_like(truth)
    for i, j in combinations(range(len(places)), 2):
        a, b = places[i], places[j]
        independent_truth[i, j] = independent_truth[j, i] = Geodesic.WGS84.Inverse(
            a["latitude"], a["longitude"], b["latitude"], b["longitude"]
        )["s12"] / 1000
    truth_difference = float(np.max(np.abs(truth - independent_truth)))
    assert truth_difference < 1e-7
    angles = np.radians(latlon(reference)).ravel()
    jacobian = angular_jacobian(angles).toarray()
    checked_columns = np.linspace(0, len(angles) - 1, 8, dtype=int)
    upper = np.triu_indices(len(places), 1)
    derivative_errors = []
    step = 1e-6
    for column in checked_columns:
        plus, minus = angles.copy(), angles.copy()
        plus[column] += step
        minus[column] -= step
        finite_difference = (
            arc_distances(unit_vectors(np.degrees(plus.reshape(-1, 2))))[upper]
            - arc_distances(unit_vectors(np.degrees(minus.reshape(-1, 2))))[upper]
        ) / (2 * step * RADIUS_KM)
        derivative_errors.append(float(np.max(np.abs(finite_difference - jacobian[:, column]))))
    assert max(derivative_errors) < 2e-5
    reference_arcs = arc_distances(reference)
    assert triangle_checks(reference_arcs)["violated_triples"] == 0
    assert cosine_checks(reference_arcs)["exact_sphere_compatible_within_tolerance"]
    assert displacement(reference, reference)["max_km"] < 1e-7
    report = {
        "schema_version": 1, "scope": "Frozen 100-capital English, Arabic, and Mandarin median matrices; in-sample descriptive geometry",
        "source_script_sha256": sha256(Path(__file__)),
        "sources": {language: {"path": str(path.relative_to(ROOT)), "sha256": sha256(path)} for language, path in paths.items()},
        "environment": {"python": sys.version, "platform": platform.platform(),
                        "packages": {name: importlib.metadata.version(name) for name in ["numpy", "scipy", "geographiclib"]},
                        "thread_environment": {key: os.environ.get(key) for key in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"]}},
        "capital_ids": [p["id"] for p in places], "capitals": 100, "pairs": 4950,
        "radius_km": RADIUS_KM, "seed": SEED,
        "independent_WGS84_max_difference_from_saved_km": truth_difference,
        "implementation_checks": {
            "analytic_jacobian_finite_difference_columns": checked_columns.tolist(),
            "finite_difference_step_radians": step, "derivative_max_abs_errors": derivative_errors,
            "derivative_error_tolerance": 2e-5,
            "actual_fixed_radius_spherical_arcs_have_no_triangle_violations": True,
            "actual_fixed_radius_spherical_arcs_have_rank3_PSD_cosine_Gram": True,
            "self_alignment_max_displacement_below_1e_minus7_km": True,
        },
        "stress_definition": "sqrt(sum over unordered pairs of (fitted-target)^2 / sum target^2), common target-distance normalization for every reported fit",
        "solver": {"name": "scipy.optimize.least_squares", "jacobian": "analytic sparse angular derivative",
                   "max_nfev": 1000, "ftol": 1e-9, "xtol": 1e-9, "gtol": 1e-9,
                   "initialization": "cosine eigenspace followed by seeded N(0,0.3^2) angular perturbations", "alignment": "one global orthogonal transform, reflections permitted, fixed radius"},
        "cautions": ["No claim of global optimum or unique geometry follows from converged multiple starts.",
                     "WGS84 is ellipsoidal; its fixed-radius spherical fit need not have zero stress or displacement.",
                     "Nearest-neighbor ties use deterministic capital order.",
                     "Positive cosine spectral tails beyond rank three are reported separately from negative mass.",
                     "No new model measurements or whole-map significance tests are produced here."],
        "conditions": {},
    }
    for language in ["truth", "en", "ar", "zh"]:
        print(f"Fitting {language}", flush=True)
        if language == "truth":
            target = truth
        else:
            other_truth, target = matrices(results[language], places)
            assert np.array_equal(truth, other_truth)
        fit, first_four, best = fit_sphere(target, reference, 4 if language == "truth" else 12)
        fitted_matrix = arc_distances(best)
        item = {
            "fit": fit, "input_nearest_three_preservation": nearest_three(target, truth),
            "fitted_nearest_three_preservation": nearest_three(fitted_matrix, truth),
            "input_triangle_checks": triangle_checks(target), "fitted_triangle_checks": triangle_checks(fitted_matrix),
            "input_cosine_checks": cosine_checks(target), "fitted_cosine_checks": cosine_checks(fitted_matrix),
            "fitted_distances_stress_against_WGS84": normalized_stress(fitted_matrix, truth),
            "input_matrix_stress_against_WGS84": normalized_stress(target, truth),
        }
        if language != "truth":
            saved = results[language]["layers"]["median"]["reconstructions"]["spherical"]
            delta = displacement(first_four, unit_vectors(saved["inferred_latlon"]))
            stress_delta = abs(fit["best_first_four_stress"] - saved["stress"])
            item["archived_four_start_verification"] = {
                "aligned_map_displacement": delta, "stress_absolute_difference": stress_delta,
                "pass": bool(delta["max_km"] < 0.001 and stress_delta < 1e-10),
            }
            assert item["archived_four_start_verification"]["pass"], language
        report["conditions"][language] = item
        print(json.dumps({"condition": language, "stress": fit["best_all_stress"],
                          "displacement_km": fit["best_aligned_true_displacement"]["mean_km"],
                          "four_to_all_shift_km": fit["first_four_to_all_displacement"]["mean_km"],
                          "all_starts_converged": fit["all_starts_converged"]}), flush=True)
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(output, flush=True)


if __name__ == "__main__":
    main()
