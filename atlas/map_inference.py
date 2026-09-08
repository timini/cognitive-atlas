"""Direct randomization test of spherical reconstructed capital geometry.

For each language pair, preserve the observed number of VALID answers in each
city pair and language. Pool valid answers within a city pair, shuffle labels,
recompute both median distance matrices, and refit both fixed-radius spherical
maps using the same four-start algorithm and optimizer seed as the observed fits.
The statistic is mean capital displacement after a single global orthogonal
alignment between maps (rotation/reflection, no scale or individual anchoring).

Null: conditional on validity and sample counts, valid-response distributions are
exchangeable between these instruction languages within every fixed city pair.
Assumes independent API calls. Invalid answers are retained in source CSVs but
not imputed; the test does not assess language effects on invalid-answer rates.
This tests the fitted capital geometry, not coastline interpolation, literal neural
representations, or a population of languages, cities, prompts, dates or models.
"""
import hashlib
import itertools
import json
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
from scipy.linalg import orthogonal_procrustes

from atlas.comparison import language_condition
from atlas.data import digest
from atlas.inference import holm
from atlas.reconstruct import RADIUS_KM, spherical, unit_vectors

_CONTEXT = None


def map_displacement(a, b):
    x, y = unit_vectors(a), unit_vectors(b)
    rotation, _ = orthogonal_procrustes(y, x)
    return float((RADIUS_KM*np.arccos(np.clip(np.sum(x*(y@rotation), axis=1), -1, 1))).mean())


def make_groups(samples_a, samples_b):
    groups = defaultdict(list)
    for i, (a, b) in enumerate(zip(samples_a, samples_b, strict=True)):
        if not a or not b:
            raise ValueError('Every pair needs at least one valid answer in both languages')
        groups[len(a), len(b)].append((i, list(a)+list(b)))
    return [(np.array([i for i, _ in rows]), na, np.array([x for _, x in rows], dtype=float))
            for (na, _), rows in groups.items()]


def permuted_medians(groups, pair_count, seed):
    rng = np.random.default_rng(seed)
    a, b = np.empty(pair_count), np.empty(pair_count)
    for indices, na, pooled in groups:
        order = np.argsort(rng.random(pooled.shape), axis=1)
        shuffled = np.take_along_axis(pooled, order, axis=1)
        a[indices], b[indices] = np.median(shuffled[:, :na], axis=1), np.median(shuffled[:, na:], axis=1)
    return a, b


def fit_vectors(a, b, ij, reference, solver_seed):
    n = len(reference)
    matrices = [np.zeros((n, n)), np.zeros((n, n))]
    fitted, convergence, stresses = [], [], []
    for values, matrix in zip([a, b], matrices, strict=True):
        matrix[ij] = values
        matrix += matrix.T
        coordinates, detail = spherical(matrix, reference, seed=solver_seed, starts=4)
        fitted.append(coordinates)
        convergence.append(detail['converged'])
        stresses.append(detail['stress'])
    return map_displacement(*fitted), all(convergence), stresses


def _initialize(context):
    global _CONTEXT
    _CONTEXT = context


def _replicate(seed):
    groups, pair_count, ij, reference, solver_seed = _CONTEXT
    a, b = permuted_medians(groups, pair_count, seed)
    return fit_vectors(a, b, ij, reference, solver_seed)


def audit_maps(paths, output_root='public/data/map-audits', permutations=999, seed=20260912, workers=3):
    if permutations < 1 or workers < 1:
        raise ValueError('Positive permutation and worker counts required')
    results, sources = {}, {}
    for path in map(Path, paths):
        raw = path.read_bytes()
        r = json.loads(raw)
        language = r['experiment']['language']
        if language in results:
            raise ValueError('Choose one explicit export per language')
        results[language] = r
        sources[language] = {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
                             'export_id': path.parent.name, 'experiment_id': r['experiment']['id']}
    conditions = [language_condition(r) for r in results.values()]
    if len(results) < 2 or any(c is None or c != conditions[0] for c in conditions):
        raise ValueError('Choose matching language conditions and analysis settings')
    languages = sorted(results, key=lambda l: (l != 'en', l))
    first = results[languages[0]]
    ids = {p['id']: i for i, p in enumerate(first['places'])}
    reference = np.array([[p['latitude'], p['longitude']] for p in first['places']])
    pairs = {l: {p['id']: p for p in r['pairs']} for l, r in results.items()}
    pair_ids = sorted(pairs[languages[0]])
    if len(pair_ids) != len(ids)*(len(ids)-1)//2 or not all(set(p) == set(pair_ids) for p in pairs.values()):
        raise ValueError('A complete unordered pair set is required')
    ij = tuple(np.array([ids[p.split('--')[k]] for p in pair_ids]) for k in [0, 1])
    solver_seed = first['analysis_parameters']['seed']
    report = {'schema_version': 1, 'method': __doc__, 'sources': sources, 'condition': conditions[0],
              'capital_count': len(ids), 'total_pairs': len(pair_ids), 'seed': seed,
              'permutations': permutations, 'solver_seed': solver_seed, 'solver_starts': 4,
              'comparisons': [], 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for ci, (a, b) in enumerate(itertools.combinations(languages, 2)):
        samples = [[pairs[l][p]['samples'] for p in pair_ids] for l in [a, b]]
        groups = make_groups(*samples)
        medians = [np.array([np.median(x) for x in s]) for s in samples]
        observed, converged, stresses = fit_vectors(*medians, ij, reference, solver_seed)
        saved = map_displacement(*[results[l]['layers']['median']['reconstructions']['spherical']['inferred_latlon'] for l in [a, b]])
        if not converged or abs(observed-saved) > .001:
            raise ValueError('Observed refit failed or does not reproduce the published map displacement')
        context = (groups, len(pair_ids), ij, reference, solver_seed)
        with ProcessPoolExecutor(max_workers=workers, initializer=_initialize, initargs=(context,)) as pool:
            replicates = list(pool.map(_replicate, (seed+ci*1_000_000+i for i in range(permutations)), chunksize=5))
        if not all(r[1] for r in replicates):
            raise ValueError('A permuted map did not converge; no p-value is published')
        null = np.array([r[0] for r in replicates])
        item = {'a': a, 'b': b, 'observed_mean_capital_shift_km': observed,
                'null_mean_capital_shift_km': float(null.mean()),
                'null_shift_95pct_interval_km': np.quantile(null, [.025, .975]).tolist(),
                'map_p': float((1+np.count_nonzero(null >= observed-1e-10))/(permutations+1)),
                'all_fits_converged': True, 'observed_stresses': stresses,
                'valid_answer_counts': {l: sum(len(x) for x in samples[i]) for i, l in enumerate([a, b])},
                'unequal_sample_count_pairs': sum(len(x) != len(y) for x, y in zip(*samples, strict=True)),
                'null_statistics_km': null.tolist()}
        report['comparisons'].append(item)
        print(json.dumps({k:v for k,v in item.items() if k!='null_statistics_km'}), flush=True)
    corrected = holm([c['map_p'] for c in report['comparisons']])
    for c, p in zip(report['comparisons'], corrected, strict=True):
        c['map_p_holm'] = float(p)
    report['holm_family_size'] = len(corrected)
    report['id'] = digest(report)[:24]
    output = Path(output_root)/f"{report['id']}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(report, indent=2, allow_nan=False)+'\n'
    if output.exists() and output.read_text() != content:
        raise ValueError('Refusing to replace an immutable map audit')
    output.write_text(content)
    return output
