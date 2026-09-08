import argparse
import asyncio
import json
from pathlib import Path

from dotenv import load_dotenv

from atlas.analysis import analyze, export
from atlas.comparison import export_comparisons
from atlas.data import load_places, read_csv
from atlas.experiment import create_experiment, estimate
from atlas.languages import LANGUAGE_LABELS, PROTOCOL_ID
from atlas.models import MODEL_PROFILES
from atlas.runner import progress, run


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="CSV-based reproducible geographic experiments")
    sub = parser.add_subparsers(dest="command", required=True)
    new = sub.add_parser("create")
    new.add_argument("--dataset", default="data/capitals-v1.csv")
    new.add_argument("--samples", type=int, default=10)
    new.add_argument("--rpm", type=float, default=120)
    new.add_argument("--concurrency", type=int, default=4)
    new.add_argument("--budget", type=float, default=1)
    new.add_argument("--language", choices=list(LANGUAGE_LABELS), default="en")
    new.add_argument("--protocol", choices=["legacy", PROTOCOL_ID], default="legacy")
    new.add_argument("--model", choices=list(MODEL_PROFILES), default="gemini-2.5-flash-lite")
    new.add_argument("--max-tokens", type=int, default=128)
    for command in ["estimate", "run", "status", "analyze", "export"]:
        child = sub.add_parser(command)
        child.add_argument("directory", type=Path)
        if command == "run":
            child.add_argument("--max-jobs", type=int)
        if command == "export":
            child.add_argument("analysis_directory", type=Path)
    sub.add_parser("compare")
    args = parser.parse_args()
    if args.command == "create":
        print(create_experiment(args.dataset, samples=args.samples, max_cost=args.budget,
                                rpm=args.rpm, concurrency=args.concurrency, language=args.language,
                                model=args.model, max_tokens=args.max_tokens, protocol=args.protocol))
    elif args.command == "estimate":
        manifest = json.loads((args.directory / "manifest.json").read_text())
        print(json.dumps(estimate(manifest, load_places(args.directory / "places.csv"),
                                  read_csv(args.directory / "pairs.csv")), indent=2))
    elif args.command == "run":
        print(json.dumps(asyncio.run(run(args.directory, max_jobs=args.max_jobs)), indent=2))
    elif args.command == "status":
        print(json.dumps(progress(args.directory), indent=2))
    elif args.command == "analyze":
        print(analyze(args.directory))
    elif args.command == "compare":
        print(export_comparisons())
    elif args.command == "export":
        print(export(args.directory, args.analysis_directory))


if __name__ == "__main__":
    main()
