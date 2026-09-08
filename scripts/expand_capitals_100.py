"""Build the frozen 100-capital superset from reviewed Natural Earth records.

Usage: python scripts/expand_capitals_100.py PLACES.geojson COUNTRIES.geojson
The original 50 records (including coordinates and decisions) are preserved.
"""
import hashlib
import json
import sys
from pathlib import Path

from atlas.data import load_places, write_csv

ADDITIONS = {
    'AT': 'Vienna', 'BE': 'Brussels', 'CH': 'Bern', 'CZ': 'Prague', 'DK': 'København',
    'HU': 'Budapest', 'IE': 'Dublin', 'RO': 'Bucharest', 'RS': 'Belgrade', 'IS': 'Reykjavík',
    'AE': 'Abu Dhabi', 'BH': 'Manama', 'IQ': 'Baghdad', 'IR': 'Tehran', 'JO': 'Amman',
    'KH': 'Phnom Penh', 'KW': 'Kuwait City', 'LA': 'Vientiane', 'LB': 'Beirut',
    'MN': 'Ulaanbaatar', 'NP': 'Kathmandu', 'OM': 'Muscat', 'QA': 'Doha', 'UZ': 'Tashkent',
    'BW': 'Gaborone', 'CM': 'Yaoundé', 'DJ': 'Djibouti', 'MG': 'Antananarivo',
    'MR': 'Nouakchott', 'MZ': 'Maputo', 'NA': 'Windhoek', 'RW': 'Kigali', 'TN': 'Tunis',
    'UG': 'Kampala', 'ZM': 'Lusaka', 'ZW': 'Harare', 'CI': 'Yamoussoukro', 'BF': 'Ouagadougou',
    'BO': 'Sucre', 'CR': 'San José', 'CU': 'Havana', 'EC': 'Quito', 'GT': 'Guatemala City',
    'PA': 'Panama City', 'UY': 'Montevideo',
    'PG': 'Port Moresby', 'SB': 'Honiara', 'TO': "Nuku'alofa", 'VU': 'Port Vila', 'WS': 'Apia',
}
DECISIONS = {
    'CH': 'Bern is the federal city and seat of government; treated as the canonical capital.',
    'BO': 'Constitutional capital Sucre selected; government seat La Paz excluded.',
    'CI': "Political capital Yamoussoukro selected; economic centre and former capital Abidjan excluded.",
    'DK': 'Canonical English name Copenhagen; source name København retained as an alternative.',
}


def build(places_path, countries_path):
    places_path, countries_path = Path(places_path), Path(countries_path)
    features = json.loads(places_path.read_text())['features']
    countries = json.loads(countries_path.read_text())['features']
    rows = load_places('data/capitals-50-v2.csv')
    for iso, name in ADDITIONS.items():
        matches = [f['properties'] for f in features if f['properties']['ISO_A2'] == iso
                   and f['properties']['NAME'] == name and f['properties']['ADM0CAP'] == 1]
        if len(matches) != 1:
            raise ValueError(f'Ambiguous reviewed source match for {iso}: {name}')
        p = matches[0]
        country = next((c['properties'] for c in countries if c['properties']['ADM0_A3'] == p['ADM0_A3']), None)
        if country is None:
            country = {
                'BH': dict(ADMIN='Bahrain', CONTINENT='Asia', SUBREGION='Western Asia'),
                'TO': dict(ADMIN='Tonga', CONTINENT='Oceania', SUBREGION='Polynesia'),
                'WS': dict(ADMIN='Samoa', CONTINENT='Oceania', SUBREGION='Polynesia'),
            }[iso]  # Small states absent from Natural Earth's 110m country polygons.
        alternatives = '|'.join(filter(None, [p['NAMEALT'], name if iso == 'DK' else '']))
        rows.append(dict(id=iso, country_id=iso, country_name=country['ADMIN'],
                         capital_name='Copenhagen' if iso == 'DK' else name,
                         latitude=p['LATITUDE'], longitude=p['LONGITUDE'],
                         continent=country['CONTINENT'], region=country['SUBREGION'], iso_code=iso,
                         alternative_spellings=alternatives,
                         localized_names=json.dumps({k[5:].lower(): v for k, v in p.items()
                                                     if k.startswith('NAME_') and v}, ensure_ascii=False),
                         decision=DECISIONS.get(iso, 'One national capital selected for the 100-capital purposive sample.'),
                         source_id=str(p['NE_ID'])))
    assert len(rows) == len({r['id'] for r in rows}) == 100
    write_csv('data/capitals-100-v3.csv', sorted(rows, key=lambda p: p['id']))
    metadata = dict(dataset_version='capitals-100-v3', capital_count=100,
                    parent_dataset='capitals-50-v2',
                    selection='Preserves the original 50 capitals and adds 50 across all inhabited continents: 10 Europe, 14 Asia, 14 Africa, 7 Americas, 5 Oceania. Purposive geographic coverage, not a random or population-weighted sample. Selection fixed before collection; all added entities are UN member states.',
                    coordinate_source='Natural Earth 10m populated places', license='Public domain',
                    sources=[dict(url='https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/' + name,
                                  sha256=hashlib.sha256(path.read_bytes()).hexdigest()) for path, name in [
                        (places_path, 'ne_10m_populated_places.geojson'),
                        (countries_path, 'ne_110m_admin_0_countries.geojson')]],
                    decision_sources=['https://www.aboutswitzerland.eda.admin.ch/en/political-system',
                                      'https://www.dfat.gov.au/sites/default/files/boli.pdf',
                                      'https://france.diplomatie.gouv.ci/fiche_signaletique.php'])
    Path('data/capitals-100-v3.sources.json').write_text(json.dumps(metadata, indent=2) + '\n')


if __name__ == '__main__':
    build(*sys.argv[1:])
