import json
from pathlib import Path

from atlas.data import digest, generate_pairs, load_places, read_csv


def validate_inputs(directory):
    directory = Path(directory)
    manifest = json.loads((directory / "manifest.json").read_text())
    condition = {k: v for k, v in manifest.items() if k != "id"}
    if digest(condition)[:24] != manifest["id"]:
        raise ValueError("Experiment manifest was modified")
    places = load_places(directory / "places.csv")
    if digest(places) != manifest["dataset_sha256"]:
        raise ValueError("Dataset was modified")
    pairs = read_csv(directory / "pairs.csv")
    for p in pairs:
        p["true_distance_km"] = float(p["true_distance_km"])
    if digest(pairs) != digest(generate_pairs(places)):
        raise ValueError("Pair file was modified or is incomplete")
    return manifest, places, pairs
