"""Conditional language tests for a specified, immutable matched export cohort.

Null: response distributions are exchangeable between instruction languages within
EACH fixed capital pair. Independently pool and reassign the two sets of n answers;
sample-number labels are not paired observations. Tests condition on independent
API calls, fixed capitals, one prompt translation per language and collection period.
They do not establish a causal language effect, generalize to new capitals, or test
reconstructed map shape. The MAE-contrast permutation tests this strong distributional
null, not the weaker hypothesis of equal MAE with different response distributions.
"""
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

from atlas.comparison import language_condition
from atlas.data import digest


def holm(pvalues):
    p = np.asarray(pvalues, dtype=float)
    if p.ndim != 1 or np.any((p < 0) | (p > 1)) or not np.isfinite(p).all():
        raise ValueError('Expected finite p-values in [0, 1]')
    order = np.argsort(p)
    adjusted = np.empty_like(p)
    adjusted[order] = np.minimum(1, np.maximum.accumulate(p[order] * (len(p) - np.arange(len(p)))))
    return adjusted


def permutation_comparison(a, b, truth, permutations=4999, seed=20260911, batch=20):
    a, b, truth = np.asarray(a), np.asarray(b), np.asarray(truth)
    if a.ndim != 2 or a.shape != b.shape or a.shape[0] != len(truth) or min(a.shape) < 1:
        raise ValueError('Expected equal pair-by-sample matrices and a matching truth vector')
    if permutations < 1 or batch < 1 or not all(np.isfinite(x).all() for x in [a, b, truth]):
        raise ValueError('Invalid permutation inputs')
    n = a.shape[1]
    med_a, med_b = np.median(a, axis=1), np.median(b, axis=1)
    observed_disagreement = float(np.abs(med_a - med_b).mean())
    observed_accuracy = float(np.abs(med_b-truth).mean() - np.abs(med_a-truth).mean())
    pooled = np.concatenate([a, b], axis=1)
    rng = np.random.default_rng(seed)
    null_disagreement, null_accuracy = np.empty(permutations), np.empty(permutations)
    for start in range(0, permutations, batch):
        count = min(batch, permutations-start)
        order = np.argsort(rng.random((count, len(a), 2*n)), axis=-1)
        shuffled = np.take_along_axis(pooled[None], order, axis=-1)
        ma, mb = np.median(shuffled[:, :, :n], axis=-1), np.median(shuffled[:, :, n:], axis=-1)
        null_disagreement[start:start+count] = np.abs(ma-mb).mean(axis=-1)
        null_accuracy[start:start+count] = np.abs(mb-truth).mean(axis=-1) - np.abs(ma-truth).mean(axis=-1)
    return {'mean_absolute_median_disagreement_km': observed_disagreement,
                'null_disagreement_mean_km': float(null_disagreement.mean()),
                'null_disagreement_95pct_interval_km': np.quantile(null_disagreement, [.025, .975]).tolist(),
                'mae_difference_b_minus_a_km': observed_accuracy,
                'null_accuracy_difference_95pct_interval_km': np.quantile(null_accuracy, [.025, .975]).tolist(),
                'judgment_p': float((1+np.count_nonzero(null_disagreement >= observed_disagreement-1e-10))/(permutations+1)),
                'accuracy_p': float((1+np.count_nonzero(np.abs(null_accuracy) >= abs(observed_accuracy)-1e-10))/(permutations+1))}


def audit(paths, output_root='public/data/language-audits', permutations=4999, seed=20260911):
    results, sources = {}, {}
    for path in map(Path, paths):
        content = path.read_bytes()
        r = json.loads(content)
        lang = r['experiment']['language']
        if lang in results:
            raise ValueError('Choose one export per language, explicitly')
        results[lang] = r
        sources[lang] = {'path': str(path), 'sha256': hashlib.sha256(content).hexdigest(),
                             'experiment_id': r['experiment']['id'], 'export_id': path.parent.name}
    conditions = [language_condition(r) for r in results.values()]
    if len(results) < 2 or any(c is None or c != conditions[0] for c in conditions):
        raise ValueError('Language conditions must match including analysis settings and reported model version')
    languages = sorted(results, key=lambda l: (l != 'en', l))
    pairs = {l: {p['id']: p for p in r['pairs']} for l, r in results.items()}
    all_ids = sorted(pairs[languages[0]])
    n = results[languages[0]]['experiment']['sampling_count']
    if not all(set(ps) == set(all_ids) for ps in pairs.values()):
        raise ValueError('Pair sets differ')
    kept = [pid for pid in all_ids if all(len(pairs[l][pid]['samples']) == n for l in languages)]
    if not kept:
        raise ValueError('No common complete pairs; do not impute')
    truth = np.array([pairs[languages[0]][pid]['true_distance_km'] for pid in kept])
    if not all(np.array_equal(truth, [pairs[l][pid]['true_distance_km'] for pid in kept]) for l in languages):
        raise ValueError('Ground truth differs')
    values = {l: np.array([pairs[l][pid]['samples'] for pid in kept]) for l in languages}
    report = {'schema_version': 1, 'method': __doc__, 'seed': seed, 'permutations': permutations,
                  'condition': conditions[0], 'sources': sources, 'languages': languages,
                  'capital_count': len(results[languages[0]]['places']), 'total_pairs': len(all_ids),
                  'complete_pairs': len(kept), 'excluded_pair_ids': sorted(set(all_ids)-set(kept)),
                  'samples_per_pair': n, 'complete_pair_median_MAE_km': {
                      l: float(np.abs(np.median(x, axis=1)-truth).mean()) for l, x in values.items()},
                  'all_pairs_median_MAE_km': {l: r['layers']['median']['metrics']['mae_km'] for l, r in results.items()},
                  'comparisons': [], 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for i, (a, b) in enumerate(itertools.combinations(languages, 2)):
        item = dict(a=a, b=b, **permutation_comparison(values[a], values[b], truth, permutations, seed+i))
        report['comparisons'].append(item)
        print(json.dumps(item), flush=True)
    family_size = 2*len(report['comparisons'])
    corrected = holm([c[k] for c in report['comparisons'] for k in ['judgment_p', 'accuracy_p']])
    for i, c in enumerate(report['comparisons']):
        c.update(judgment_p_holm=float(corrected[2*i]), accuracy_p_holm=float(corrected[2*i+1]))
    report['holm_family_size'] = family_size
    report['id'] = digest(report)[:24]
    output = Path(output_root)/f"{report['id']}.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(report, indent=2, allow_nan=False) + '\n'
    if output.exists() and output.read_text() != content:
        raise ValueError('Refusing to replace a different immutable audit')
    output.write_text(content)
    return output
