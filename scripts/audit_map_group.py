"""Direct map-shape tests from explicit saved language exports; no API calls."""
import argparse

from atlas.map_inference import audit_maps

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results', nargs='+')
    parser.add_argument('--permutations', type=int, default=999)
    parser.add_argument('--seed', type=int, default=20260912)
    parser.add_argument('--workers', type=int, default=3)
    args = parser.parse_args()
    print(audit_maps(args.results, permutations=args.permutations, seed=args.seed, workers=args.workers), flush=True)
