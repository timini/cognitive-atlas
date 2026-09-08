"""One process owns an experiment file; bounded async workers perform independent calls.

CSV checkpoints are flushed and fsynced per attempt. A crash between API completion and
fsync can require a repeated paid call: exactly-once delivery is not promised by Gemini.
"""
import asyncio
import csv
import fcntl
import json
import os
import random
import time
from collections import Counter
from pathlib import Path

from atlas.data import digest, read_csv
from atlas.experiment import prompt_for, utcnow
from atlas.parsing import parse_distance
from atlas.providers import PROVIDERS, ProviderError
from atlas.validation import validate_inputs

FIELDS = ["response_id", "experiment_id", "pair_id", "sample_number", "attempt", "timestamp",
          "prompt", "raw_response", "parsed_distance_km", "quality", "terminal", "retryable",
          "latency_ms", "input_tokens", "output_tokens", "estimated_cost_usd", "reserved_cost_usd",
          "model_version", "finish_reason", "provider_payload"]


class Limiter:
    def __init__(self, rpm):
        self.interval, self.next = 60 / rpm, 0
        self.lock = asyncio.Lock()

    async def wait(self):
        async with self.lock:
            now = time.monotonic()
            await asyncio.sleep(max(0, self.next - now))
            self.next = time.monotonic() + self.interval


def history(directory):
    path = Path(directory) / "responses.csv"
    if not path.exists():
        return []
    rows = read_csv(path)
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        raise ValueError("Incomplete CSV checkpoint. Preserve the file and repair its last row before resuming.")
    return rows


def progress(directory):
    rows = history(directory)
    return {"attempts": len(rows), "completed_samples": sum(r["terminal"] == "True" for r in rows),
            "valid_samples": sum(r["quality"] == "valid" for r in rows),
            "quality": dict(Counter(r["quality"] for r in rows)),
            "estimated_cost_usd": sum(float(r["estimated_cost_usd"]) for r in rows)}


async def run(directory, provider=None, max_jobs=None):
    directory = Path(directory)
    validate_inputs(directory)
    if max_jobs is not None and max_jobs < 0:
        raise ValueError("max_jobs must be nonnegative")
    manifest = json.loads((directory / "manifest.json").read_text())
    places_list = read_csv(directory / "places.csv")
    places = {p["id"]: p for p in places_list}
    # Canonical hash uses numeric coordinates, as at experiment creation.
    canonical = [{**p, "latitude": float(p["latitude"]), "longitude": float(p["longitude"])} for p in places_list]
    if digest(canonical) != manifest["dataset_sha256"]:
        raise ValueError("Dataset was modified after experiment creation")
    pairs = read_csv(directory / "pairs.csv")
    with (directory / ".runner.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another runner owns this experiment") from None
        rows = history(directory)
        complete = {(r["pair_id"], int(r["sample_number"])) for r in rows if r["terminal"] == "True"}
        attempts = Counter((r["pair_id"], int(r["sample_number"])) for r in rows)
        reserved = sum(float(r["reserved_cost_usd"]) for r in rows)
        config, pricing = manifest["execution"], manifest["pricing"]
        queue = asyncio.Queue(maxsize=config["concurrency"] * 2)
        limiter = Limiter(config["requests_per_minute"])
        stop = asyncio.Event()
        owned = provider is None
        provider = provider or PROVIDERS[manifest["provider"]]()
        path = directory / "responses.csv"
        exists = path.exists()
        with path.open("a", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            if not exists:
                writer.writeheader()
                stream.flush()
                os.fsync(stream.fileno())

            async def produce():
                queued = 0
                for pair in pairs:
                    for sample in range(manifest["sampling_count"]):
                        key = (pair["id"], sample)
                        if key in complete or stop.is_set():
                            continue
                        if max_jobs is not None and queued >= max_jobs:
                            break
                        await queue.put((pair, sample))
                        queued += 1
                for _ in range(config["concurrency"]):
                    await queue.put(None)

            async def worker():
                nonlocal reserved
                while (job := await queue.get()) is not None:
                    pair, sample = job
                    prompt = prompt_for(manifest, pair, places)
                    reserve = ((len(prompt.encode()) + 256) * pricing["input_per_million_usd"] +
                               manifest["parameters"]["max_tokens"] * pricing["output_per_million_usd"]) / 1e6
                    key = (pair["id"], sample)
                    for attempt in range(attempts[key] + 1, config["max_attempts"] + 1):
                        if stop.is_set() or reserved + reserve > config["max_cost_usd"]:
                            stop.set()
                            break
                        reserved += reserve
                        await limiter.wait()
                        row = dict.fromkeys(FIELDS, "")
                        row.update(response_id=digest([manifest["id"], *key, attempt]),
                                   experiment_id=manifest["id"], pair_id=pair["id"], sample_number=sample,
                                   attempt=attempt, timestamp=utcnow(), prompt=prompt,
                                   estimated_cost_usd=0, reserved_cost_usd=reserve, retryable=False)
                        delay = 0
                        try:
                            reply = await provider.query(manifest["model"], prompt, manifest["parameters"])
                            parsed = parse_distance(reply.text)
                            if reply.finish_reason != "STOP":
                                parsed = type(parsed)(None, "refusal_or_truncated")
                            row.update(raw_response=reply.text, parsed_distance_km=parsed.value,
                                       quality=parsed.quality, terminal=True, latency_ms=reply.latency_ms,
                                       input_tokens=reply.input_tokens, output_tokens=reply.output_tokens,
                                       model_version=reply.model_version, finish_reason=reply.finish_reason,
                                       provider_payload=json.dumps(reply.payload, ensure_ascii=False),
                                       estimated_cost_usd=(reply.input_tokens * pricing["input_per_million_usd"] +
                                                           reply.output_tokens * pricing["output_per_million_usd"]) / 1e6)
                        except ProviderError as exc:
                            row.update(quality=exc.code, retryable=exc.retryable,
                                       terminal=not exc.retryable or attempt == config["max_attempts"])
                            delay = min(120, max(exc.retry_after, 2 ** attempt + random.random()))
                            if not exc.retryable:
                                stop.set()
                        if row["provider_payload"] and manifest.get("schema_version", 1) >= 2:
                            # Completed usage replaces the in-flight upper reservation. Unknown
                            # transport attempts retain their full reservation across restarts.
                            actual_cost = float(row["estimated_cost_usd"])
                            reserved += actual_cost - reserve
                            row["reserved_cost_usd"] = actual_cost
                        writer.writerow(row)
                        stream.flush()
                        os.fsync(stream.fileno())
                        if row["terminal"]:
                            break
                        await asyncio.sleep(delay)
            try:
                await asyncio.gather(produce(), *(worker() for _ in range(config["concurrency"])))
            finally:
                if owned:
                    await provider.close()
        return progress(directory)
