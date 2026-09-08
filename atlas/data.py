import csv
import hashlib
import json
from itertools import combinations
from pathlib import Path

from geographiclib.geodesic import Geodesic


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    fields = fields or list(rows[0])
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def load_places(path):
    rows = read_csv(path)
    for p in rows:
        p["latitude"], p["longitude"] = float(p["latitude"]), float(p["longitude"])
        if not (-90 <= p["latitude"] <= 90 and -180 <= p["longitude"] <= 180):
            raise ValueError("Invalid coordinates")
    if len({p["id"] for p in rows}) != len(rows) or len(rows) < 3:
        raise ValueError("Need at least three uniquely identified capitals")
    return sorted(rows, key=lambda p: p["id"])


def geodesic(a, b):
    return Geodesic.WGS84.Inverse(a["latitude"], a["longitude"],
                                 b["latitude"], b["longitude"])["s12"] / 1000


def generate_pairs(places):
    return [{"id": f'{a["id"]}--{b["id"]}', "place_a_id": a["id"],
             "place_b_id": b["id"], "true_distance_km": geodesic(a, b)}
            for a, b in combinations(sorted(places, key=lambda p: p["id"]), 2)]
