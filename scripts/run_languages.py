"""Prepare or resume a controlled five-language experiment, with a shared rate limit."""
import argparse
import asyncio
import json
from pathlib import Path

from dotenv import load_dotenv

from atlas.data import digest, load_places, read_csv
from atlas.experiment import create_experiment, estimate
from atlas.languages import PROTOCOL_ID
from atlas.runner import Limiter, progress, run


def prepare(target):
    target = Path(target)
    if target.exists():
        raise ValueError('A language group already exists; resume it instead')
    paths = []
    for language in ['en', 'fr', 'es', 'ar', 'zh']:
        directory = create_experiment('data/capitals-50-v2.csv', model='gemini-3.5-flash', language=language,
                                      protocol=PROTOCOL_ID, max_cost=15, rpm=900, concurrency=16,
                                      shared_rpm=2400)
        paths.append(str(directory))
        manifest = json.loads((directory/'manifest.json').read_text())
        print(language, str(directory), estimate(manifest, load_places(directory/'places.csv'),
                                                 read_csv(directory/'pairs.csv')), flush=True)
    group = {'paths': paths, 'shared_requests_per_minute': 2400, 'protocol': PROTOCOL_ID}
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
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.group)
    else:
        asyncio.run(collect(args.group, args.max_jobs))
