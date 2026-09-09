"""Conditional error-sign controls, kept separate from every LLM observation.

Each artificial distance retains its pair's observed absolute median error.
Only the sign is randomized, independently where both signs satisfy the same
positive, <=20,040-km reporting domain. This is a descriptive benchmark, not a
model of response sampling or a test of an identified cognitive mechanism.
"""
from itertools import combinations

import numpy as np

from paper.revision100.common import PAPER, load_results, write_report

LIMIT_KM = 20040.0


def sign_control(truth, observed, rng):
    truth, observed = np.asarray(truth), np.asarray(observed)
    if truth.ndim != 1 or not truth.size or truth.shape != observed.shape or not np.all(np.isfinite(truth + observed)):
        raise ValueError('Expected matching finite distance vectors')
    if np.any(truth <= 0) or np.any(observed <= 0) or np.any(observed > LIMIT_KM):
        raise ValueError('Distances must be positive and observations within the QC domain')
    error = np.abs(observed - truth)
    low, high = truth - error, truth + error
    low_ok, high_ok = low > 0, high <= LIMIT_KM
    if not np.all(low_ok | high_ok):
        raise ValueError('No admissible error sign')
    use_high = rng.integers(0, 2, len(truth)).astype(bool)
    use_high = np.where(~low_ok, True, np.where(~high_ok, False, use_high))
    return np.where(use_high, high, low), int(np.sum(low_ok != high_ok))


def triangle_summary(vector, edges):
    sides = vector[edges]
    excess = np.maximum(0, 2 * sides.max(axis=1) - sides.sum(axis=1))
    return {'violation_rate': float(np.mean(excess > 1e-7)),
            'mean_excess_all_triples_km': float(excess.mean())}


def main():
    runs = load_results()
    report = {'kind': 'synthetic conditional error-sign controls; not LLM responses',
              'seed': 20260909, 'replicates_per_condition': 999,
              'domain_km': [0, LIMIT_KM], 'zero_excluded': True,
              'interpretation': 'Control percentiles describe artificial sign assignments, not confidence intervals or causal tests.',
              'conditions': {}}
    for language, run in runs.items():
        ids = [p['id'] for p in run['places']]
        lookup = {frozenset((p['place_a_id'], p['place_b_id'])): i
                  for i, p in enumerate(run['pairs'])}
        edges = np.array([[lookup[frozenset(pair)] for pair in combinations(triple, 2)]
                          for triple in combinations(ids, 3)])
        truth = np.array([p['true_distance_km'] for p in run['pairs']])
        observed = np.array([p['median'] for p in run['pairs']])
        rng = np.random.default_rng(report['seed'])
        controls = []
        maximum_error_drift = 0.0
        for _ in range(report['replicates_per_condition']):
            artificial, forced = sign_control(truth, observed, rng)
            maximum_error_drift = max(maximum_error_drift, float(np.max(
                np.abs(np.abs(artificial - truth) - np.abs(observed - truth)))))
            controls.append(triangle_summary(artificial, edges))
        report['conditions'][language] = {
            'pairs': len(truth), 'triples': len(edges), 'forced_sign_pairs': forced,
            'pair_median_mae_km': float(np.mean(np.abs(observed - truth))),
            'maximum_absolute_error_preservation_drift_km': maximum_error_drift,
            'observed': triangle_summary(observed, edges),
            'reference': triangle_summary(truth, edges),
            'controls': controls,
            'summary': {key: {'mean': float(np.mean([c[key] for c in controls])),
                              'central_95pct_range': np.quantile([c[key] for c in controls], [.025, .975]).tolist()}
                        for key in controls[0]}}
    write_report(PAPER / 'revision100/error_control.json', report, __file__)
    for language, condition in report['conditions'].items():
        print(language, condition['observed'], condition['summary'], 'forced signs', condition['forced_sign_pairs'])


if __name__ == '__main__':
    main()
