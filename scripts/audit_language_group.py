"""Audit explicit matching published exports; update the website's audit index."""
import argparse

from atlas.inference import audit

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results', nargs='+', help='Explicit public/data/<export>/result.json paths')
    parser.add_argument('--permutations', type=int, default=4999)
    parser.add_argument('--seed', type=int, default=20260911)
    args = parser.parse_args()
    print(audit(args.results, permutations=args.permutations, seed=args.seed), flush=True)
