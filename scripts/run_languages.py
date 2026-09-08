"""Prepare or resume a controlled multilingual experiment, with a shared rate limit."""
import argparse
import asyncio
import json
from pathlib import Path

from dotenv import load_dotenv

from atlas.data import digest, load_places, read_csv
from atlas.experiment import create_experiment, estimate
from atlas.languages import PROTOCOL_ID
from atlas.runner import Limiter, progress, run


def prepare(target, dataset='data/capitals-50-v2.csv', languages=('en', 'fr', 'es', 'ar', 'zh'),
            model='gemini-3.5-flash', samples=10, budget=15, rpm=900, shared_rpm=2400, concurrency=16):
    target = Path(target)
    if target.exists():
        raise ValueError('A language group already exists; resume it instead')
    from atlas.languages import PROMPTS
    if not languages or len(set(languages)) != len(languages) or any(l not in PROMPTS for l in languages):
        raise ValueError('Choose distinct supported languages')
    paths = []
    for language in languages:
        directory = create_experiment(dataset, model=model, language=language, samples=samples,
                                      protocol=PROTOCOL_ID, max_cost=budget, rpm=rpm, concurrency=concurrency,
                                      shared_rpm=shared_rpm)
        paths.append(str(directory))
        manifest = json.loads((directory/'manifest.json').read_text())
        print(language, str(directory), estimate(manifest, load_places(directory/'places.csv'),
                                                 read_csv(directory/'pairs.csv')), flush=True)
    group = {'paths': paths, 'shared_requests_per_minute': shared_rpm, 'protocol': PROTOCOL_ID}
    group['id'] = digest(group)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(group, indent=2))
    print('Prepared', target, flush=True)


async def collect(target, max_jobs=None):
    group = json.loads(Path(target).read_text())
    assert group['id'] == digest({k: v for k, v in group.items() if k != 'id'})
    shared = Limiter(group['shared_requests_per_minute'])
    paths = group['paths']
    for path in paths:
        manifest = json.loads((Path(path)/'manifest.json').read_text())
        if manifest['execution'].get('shared_requests_per_minute') != group['shared_requests_per_minute']:
            raise ValueError('Shared rate does not match the immutable run condition')
    async def one(path):
        result = await run(path, max_jobs=max_jobs, shared_limiter=shared)
        print(json.dumps({'finished': path, **result}), flush=True)
    jobs = {asyncio.create_task(one(path)) for path in paths}
    pending = jobs
    try:
        while pending:
            done, pending = await asyncio.wait(pending, timeout=30)
            for job in done:
                job.result()
            if pending:
                print(json.dumps({'progress': [{'run': path, **progress(path)} for path in paths],
                                  'shared_effective_rpm': 60/shared.interval}), flush=True)
    finally:
        for job in jobs:
            if not job.done():
                job.cancel()
        await asyncio.gather(*jobs, return_exceptions=True)


if __name__ == '__main__':
    load_dotenv('.env')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'run'])
    parser.add_argument('--group', default='runs/languages-50-v2.json')
    parser.add_argument('--max-jobs', type=int)
    parser.add_argument('--dataset', default='data/capitals-50-v2.csv')
    parser.add_argument('--languages', nargs='+', default=['en', 'fr', 'es', 'ar', 'zh'])
    parser.add_argument('--model', default='gemini-3.5-flash')
    parser.add_argument('--samples', type=int, default=10)
    parser.add_argument('--budget', type=float, default=15, help='USD cap per language')
    parser.add_argument('--rpm', type=int, default=900)
    parser.add_argument('--shared-rpm', type=int, default=2400)
    parser.add_argument('--concurrency', type=int, default=16)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.group, args.dataset, args.languages, args.model, args.samples, args.budget,
                args.rpm, args.shared_rpm, args.concurrency)
    else:
        asyncio.run(collect(args.group, args.max_jobs))
