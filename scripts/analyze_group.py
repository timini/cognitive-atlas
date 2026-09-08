"""Analyze completed file-backed runs, then export them sequentially to avoid index races."""
import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from atlas.analysis import analyze, export
from atlas.comparison import export_comparisons
from atlas.data import digest
from atlas.runner import progress
from atlas.validation import validate_inputs


def analyze_group(group_path, workers=3):
    group = json.loads(Path(group_path).read_text())
    if group['id'] != digest({k: v for k, v in group.items() if k != 'id'}):
        raise ValueError('The experiment group was modified')
    paths = group['paths']
    for path in paths:
        manifest, _, pairs = validate_inputs(path)
        if progress(path)['completed_samples'] != len(pairs)*manifest['sampling_count']:
            raise ValueError(f'Collection is incomplete: {path}')
    with ProcessPoolExecutor(max_workers=workers) as pool:
        analyses = list(pool.map(analyze, paths))
    for path, analysis in zip(paths, analyses):
        print('Exported', export(path, analysis), flush=True)
    print('Compared', export_comparisons(), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('group')
    parser.add_argument('--workers', type=int, default=3)
    args = parser.parse_args()
    analyze_group(args.group, args.workers)
