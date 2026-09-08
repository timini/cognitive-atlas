"""Import reviewed MVP controls from a Natural Earth source snapshot.

Run with source GeoJSON paths; outputs retain input hashes and geographic provenance.
Adding more reviewed sovereign-state records changes data, not runner architecture.
"""
import hashlib
import json
import sys
from pathlib import Path

from atlas.data import write_csv

SELECTION = {"US": "Washington, D.C.", "CA": "Ottawa", "MX": "Mexico City", "BR": "Brasília",
             "AR": "Buenos Aires", "GB": "London", "FR": "Paris", "DE": "Berlin", "EG": "Cairo",
             "KE": "Nairobi", "NG": "Abuja", "ZA": "Pretoria", "IN": "New Delhi", "CN": "Beijing",
             "JP": "Tokyo", "TH": "Bangkok", "AU": "Canberra", "NZ": "Wellington", "FJ": "Suva",
             "SA": "Riyadh"}


def main():
    places_path, countries_path = map(Path, sys.argv[1:])
    features = json.loads(places_path.read_text())["features"]
    countries = json.loads(countries_path.read_text())["features"]
    rows = []
    for iso, name in SELECTION.items():
        matches = [f for f in features if f["properties"]["ISO_A2"] == iso and
                   (f["properties"]["ADM0CAP"] == 1 or f["properties"]["CAPALT"] == 1)]
        matches = [f for f in matches if " ".join(f["properties"]["NAME"].split()) == name]
        if len(matches) != 1:
            raise ValueError(f"Review capital choice for {iso}: {[f['properties']['NAME'] for f in matches]}")
        p = matches[0]["properties"]
        country = next(f["properties"] for f in countries if f["properties"]["ADM0_A3"] == p["ADM0_A3"])
        rows.append({"id": iso, "country_id": iso, "country_name": country["ADMIN"], "capital_name": name,
                     "latitude": p["LATITUDE"], "longitude": p["LONGITUDE"], "continent": country["CONTINENT"],
                     "region": country["SUBREGION"], "iso_code": iso, "alternative_spellings": p["NAMEALT"] or "",
                     "localized_names": json.dumps({k[5:].lower(): v for k, v in p.items() if k.startswith("NAME_") and v}, ensure_ascii=False),
                     "decision": "Executive capital; legislative Cape Town and judicial Bloemfontein excluded" if iso == "ZA" else "One national capital selected for pilot",
                     "source_id": str(p["NE_ID"])})
    write_csv("data/capitals-v1.csv", sorted(rows, key=lambda p: p["id"]))
    Path("public/data").mkdir(parents=True, exist_ok=True)
    world = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {
        "name": f["properties"]["ADMIN"]}, "geometry": f["geometry"]} for f in countries]}
    Path("public/data/world.json").write_text(json.dumps(world, separators=(",", ":")))
    Path("public/data/capitals.json").write_text(json.dumps(rows, ensure_ascii=False))
    sources = {"dataset_version": "pilot-v1", "license": "Natural Earth public domain", "sources": [
        {"url": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/" + name,
         "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path, name in [
            (places_path, "ne_10m_populated_places.geojson"), (countries_path, "ne_110m_admin_0_countries.geojson")]]}
    Path("data/sources.json").write_text(json.dumps(sources, indent=2))


if __name__ == "__main__":
    main()
