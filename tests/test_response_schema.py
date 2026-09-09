import copy
import json
from string import Formatter

import httpx
import pytest

from atlas import languages, response_schema
from atlas.comparison import language_condition
from atlas.data import digest, load_places, write_csv
from atlas.experiment import create_experiment
from atlas.parsing import parse_distance
from atlas.providers import Gemini
from atlas.runner import history, run


@pytest.mark.parametrize('raw,quality', [
    ('{"distance_km":"1,234"}', 'invalid_response_schema'),
    ('{"distance_km":true}', 'invalid_response_schema'),
    ('{"distance_km":null}', 'invalid_response_schema'),
    ('[1234]', 'invalid_response_schema'),
    ('1234', 'invalid_response_schema'),
    ('{"distance_km":1234,"units":"km"}', 'invalid_response_schema'),
    ('{"distance_km":1,"distance_km":2}', 'invalid_json'),
    ('{"distance_km":NaN}', 'invalid_json'),
    ('{"distance_km":Infinity}', 'invalid_json'),
    ('{"distance_km":١٢٣٤}', 'invalid_json'),
    ('```json\n{"distance_km":1234}\n```', 'invalid_json'),
    ('{"distance_km":0}', 'non_positive_or_non_finite'),
    ('{"distance_km":-1}', 'non_positive_or_non_finite'),
    ('{"distance_km":1e999}', 'non_positive_or_non_finite'),
    ('{"distance_km":21000}', 'beyond_earth_diameter_arc'),
])
def test_json_schema_rejects_ambiguous_or_invalid_observations(raw, quality):
    result = parse_distance(raw, response_schema.PARSER_ID)
    assert result.value is None and result.quality == quality


def test_json_parser_never_uses_regex(monkeypatch):
    import atlas.parsing
    def forbidden(*args, **kwargs):
        raise AssertionError('JSON observations must not pass through regex parsing')
    for name in ['match', 'fullmatch', 'search', 'findall']:
        monkeypatch.setattr(atlas.parsing.re, name, forbidden)
    for raw in ['{"distance_km":1234.5}', '{"distance_km":1.2345e3}']:
        assert parse_distance(raw, response_schema.PARSER_ID).value == 1234.5


async def test_schema_reaches_provider_and_raw_json_survives_resume(tmp_path):
    write_csv(tmp_path/'places.csv', load_places('data/capitals-v1.csv')[:3])
    directory = create_experiment(tmp_path/'places.csv', root=tmp_path/'runs', samples=1,
                                  model='gemini-3.5-flash', protocol=response_schema.PROTOCOL_ID,
                                  rpm=1e9)
    manifest = json.loads((directory/'manifest.json').read_text())
    assert manifest['id'] == digest({k: v for k, v in manifest.items() if k != 'id'})[:24]
    assert manifest['parameters']['response_json_schema'] == response_schema.SCHEMA
    calls = []
    raw = '{"distance_km":1234.5}'
    def handler(request):
        body = json.loads(request.content)
        config = body['generationConfig']
        assert config['responseMimeType'] == 'application/json'
        assert config['responseJsonSchema'] == response_schema.SCHEMA
        assert 'minimum' not in config['responseJsonSchema']['properties']['distance_km']
        assert 'maximum' not in config['responseJsonSchema']['properties']['distance_km']
        calls.append(body)
        return httpx.Response(200, json={'candidates': [{'content': {'parts': [{'text': raw}]},
                              'finishReason': 'STOP'}], 'usageMetadata': {'promptTokenCount': 50,
                              'candidatesTokenCount': 8}, 'modelVersion': 'test-version'})
    provider = Gemini('test-key', transport=httpx.MockTransport(handler))
    try:
        await run(directory, provider, max_jobs=1)
        await run(directory, provider)
        await run(directory, provider)
    finally:
        await provider.close()
    assert len(calls) == 3
    rows = history(directory)
    assert len(rows) == 3
    assert all(r['raw_response'] == raw and float(r['parsed_distance_km']) == 1234.5 for r in rows)
    assert all(r['quality'] == 'valid' for r in rows)


def test_json_language_conditions_are_matched_but_separate_from_text(tmp_path):
    write_csv(tmp_path/'places.csv', load_places('data/capitals-v1.csv')[:3])
    conditions = []
    for language, template in response_schema.PROMPTS.items():
        assert {f for _, f, _, _ in Formatter().parse(template) if f} == {
            'city_a', 'country_a', 'city_b', 'country_b'}
        directory = create_experiment(tmp_path/'places.csv', root=tmp_path/'runs', language=language,
                                      protocol=response_schema.PROTOCOL_ID)
        manifest = json.loads((directory/'manifest.json').read_text())
        result = {'experiment': manifest, 'resolved_model_versions': ['test'], 'analysis_parameters': {}}
        condition = language_condition(result)
        assert condition is not None
        conditions.append(condition)
        changed = copy.deepcopy(result)
        changed['experiment']['parameters']['response_json_schema']['additionalProperties'] = True
        assert language_condition(changed) is None
    assert all(condition == conditions[0] for condition in conditions)
    result['experiment'].update(prompt_family=languages.PROTOCOL_ID, response_parser=languages.PARSER_ID,
                                prompt_template=languages.PROMPTS[language])
    assert digest(language_condition(result)) != digest(conditions[0])


async def test_historical_provider_requests_do_not_gain_a_schema():
    def handler(request):
        config = json.loads(request.content)['generationConfig']
        assert 'responseJsonSchema' not in config and 'responseMimeType' not in config
        return httpx.Response(200, json={})
    provider = Gemini('test-key', transport=httpx.MockTransport(handler))
    try:
        await provider.query('gemini-3.5-flash', 'test', {'temperature': 1, 'top_p': .95, 'max_tokens': 128})
    finally:
        await provider.close()
