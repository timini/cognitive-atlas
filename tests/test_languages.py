import json
from string import Formatter

import pytest

from atlas.data import load_places, read_csv, write_csv
from atlas.experiment import create_experiment, prompt_for
from atlas.languages import ENTITY_NAME_POLICY, PARSER_ID, PROMPTS, PROTOCOL_ID
from atlas.parsing import parse_distance
from atlas.providers import Reply
from atlas.runner import Limiter, history, run


def test_translated_conditions_only_change_instruction_language(tmp_path):
    write_csv(tmp_path/'places.csv', load_places('data/capitals-50-v2.csv')[:3])
    manifests = []
    for language, template in PROMPTS.items():
        assert {field for _, field, _, _ in Formatter().parse(template) if field} == {'city_a', 'country_a', 'city_b', 'country_b'}
        directory = create_experiment(tmp_path/'places.csv', root=tmp_path/'runs', language=language,
                                      model='gemini-3.5-flash', protocol=PROTOCOL_ID)
        manifest = json.loads((directory/'manifest.json').read_text())
        places = {p['id']: p for p in load_places(directory/'places.csv')}
        pair = read_csv(directory/'pairs.csv')[0]
        prompt = prompt_for(manifest, pair, places)
        assert all(places[pair[key]]['capital_name'] in prompt for key in ['place_a_id', 'place_b_id'])
        assert manifest['entity_name_policy'] == ENTITY_NAME_POLICY
        assert manifest['response_parser'] == PARSER_ID
        manifests.append(manifest)
    for key in ['parameters', 'dataset_sha256', 'sampling_count', 'prompt_family', 'response_parser']:
        assert all(m[key] == manifests[0][key] for m in manifests)


@pytest.mark.parametrize('text', ['1,234', '1.234,5', '١٢٣٤', '1 234', '1234 km', '1234公里', 'about 1234'])
def test_format_rule_cannot_silently_change_magnitude(text):
    assert parse_distance(text, PARSER_ID).quality == 'invalid_numeric_format'


def test_shared_throttle_and_numeric_protocol():
    assert parse_distance('1234.5', PARSER_ID).value == 1234.5
    assert parse_distance('0', PARSER_ID).quality == 'non_positive_or_non_finite'
    assert parse_distance('25000', PARSER_ID).quality == 'beyond_earth_diameter_arc'
    limiter = Limiter(2400)
    limiter.backoff(5)
    interval = limiter.interval
    limiter.backoff(5)
    assert interval == .05 and limiter.interval == interval


async def test_runner_uses_recorded_parser(tmp_path):
    write_csv(tmp_path/'places.csv', load_places('data/capitals-50-v2.csv')[:3])
    directory = create_experiment(tmp_path/'places.csv', root=tmp_path/'runs', language='fr',
                                  protocol=PROTOCOL_ID, samples=1, rpm=1e9)
    class Provider:
        async def query(self, *args):
            return Reply('1,234', {'fixture': True}, 20, 2, 'test', 1, 'STOP')
    await run(directory, Provider())
    assert history(directory)[0]['quality'] == 'invalid_numeric_format'
