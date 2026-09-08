"""Create a reviewed 50-capital superset without modifying the original pilot."""
import hashlib
import json
import sys
from pathlib import Path

from atlas.data import load_places, write_csv

ADDITIONS = {
    "ES": "Madrid", "IT": "Rome", "PT": "Lisbon", "NL": "Amsterdam", "SE": "Stockholm",
    "NO": "Oslo", "FI": "Helsinki", "PL": "Warsaw", "GR": "Athens", "TR": "Ankara",
    "RU": "Moscow", "UA": "Kyiv", "MA": "Rabat", "DZ": "Algiers", "ET": "Addis Ababa",
    "GH": "Accra", "SN": "Dakar", "CD": "Kinshasa", "TZ": "Dodoma", "AO": "Luanda",
    "PK": "Islamabad", "BD": "Dhaka", "KR": "Seoul", "VN": "Hanoi", "PH": "Manila",
    "MY": "Kuala Lumpur", "SG": "Singapore", "CL": "Santiago", "PE": "Lima", "CO": "Bogota",
}
DECISIONS = {
    "NL": "Constitutional capital Amsterdam; government seat The Hague excluded.",
    "MY": "National capital Kuala Lumpur; federal administrative centre Putrajaya excluded.",
    "TZ": "Dodoma is the capital under the Dodoma Capital City (Declaration) Act 2018; override Natural Earth's older primary-capital flag for Dar es Salaam.",
    "SG": "City-state; Singapore city point is the canonical capital. Too small for the 110m country-outline dataset.",
}


def main():
    places_path, country_path = map(Path, sys.argv[1:])
    places = json.loads(places_path.read_text())["features"]
    countries = json.loads(country_path.read_text())["features"]
    old = load_places("data/capitals-v1.csv")
    rows = list(old)
    for iso, name in ADDITIONS.items():
        found = [f["properties"] for f in places if f["properties"]["ISO_A2"] == iso and f["properties"]["NAME"] == name]
        if len(found) != 1:
            raise ValueError(f"Ambiguous source match for {iso}: {name}")
        p = found[0]
        country = next((c["properties"] for c in countries if c["properties"]["ADM0_A3"] == p["ADM0_A3"]), None)
        if country is None and iso == "SG":
            country = {"ADMIN": "Singapore", "CONTINENT": "Asia", "SUBREGION": "South-Eastern Asia"}
        if country is None:
            raise ValueError(f"Missing reviewed country metadata for {iso}")
        rows.append({"id": iso, "country_id": iso, "country_name": country["ADMIN"],
                     "capital_name": "Bogotá" if iso == "CO" else name,
                     "latitude": p["LATITUDE"], "longitude": p["LONGITUDE"],
                     "continent": country["CONTINENT"], "region": country["SUBREGION"], "iso_code": iso,
                     "alternative_spellings": p["NAMEALT"] or "",
                     "localized_names": json.dumps({k[5:].lower(): v for k, v in p.items() if k.startswith("NAME_") and v}, ensure_ascii=False),
                     "decision": DECISIONS.get(iso, "One national capital selected for expanded purposive sample."),
                     "source_id": str(p["NE_ID"])})
    assert len(rows) == len({r["id"] for r in rows}) == 50
    write_csv("data/capitals-50-v2.csv", sorted(rows, key=lambda p: p["id"]))
    metadata = {"dataset_version": "capitals-50-v2", "capital_count": 50,
                "selection": "Original 20 capitals plus 30 purposively selected capitals across regions; not a random or population-weighted sample.",
                "coordinate_source": "Natural Earth 10m populated places", "license": "Public domain",
                "source_hashes": {"places": hashlib.sha256(places_path.read_bytes()).hexdigest(),
                                  "countries": hashlib.sha256(country_path.read_bytes()).hexdigest()},
                "decision_sources": ["https://oagmis.oag.go.tz/portal/acts/52",
                                     "https://www.dfat.gov.au/geo/heads-of-government/netherlands",
                                     "https://www.pmo.gov.my/en/perdana-putra/"]}
    Path("data/capitals-50-v2.sources.json").write_text(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
