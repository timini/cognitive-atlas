"""Strict numeric protocol; never extract a convenient number from prose."""
import json
import math
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ParseResult:
    value: float | None
    quality: str


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def _reject_constant(value):
    raise ValueError('Non-standard JSON constant')


def parse_distance(raw, protocol="legacy"):
    if protocol == 'json_distance_v3':
        try:
            parsed = json.loads(raw, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
        except (ValueError, TypeError):
            return ParseResult(None, 'invalid_json')
        if not isinstance(parsed, dict) or set(parsed) != {'distance_km'} or type(parsed['distance_km']) not in (int, float):
            return ParseResult(None, 'invalid_response_schema')
        try:
            value = float(parsed['distance_km'])
        except OverflowError:
            return ParseResult(None, 'non_positive_or_non_finite')
        if not math.isfinite(value) or value <= 0:
            return ParseResult(None, 'non_positive_or_non_finite')
        if value > 20040:
            return ParseResult(None, 'beyond_earth_diameter_arc')
        return ParseResult(value, 'valid')
    if protocol == "ascii_decimal_v2":
        text = raw.strip()
        if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", text):
            return ParseResult(None, "invalid_numeric_format")
        return parse_distance(text)
    if protocol != "legacy":
        raise ValueError("Unknown response parser")
    text = raw.strip()
    if re.search(r"\b(miles?|mi|metres?|meters?)\b", text, re.IGNORECASE):
        return ParseResult(None, "wrong_units")
    # English thousands separators only. Decimal commas need a separate protocol.
    pattern = r"[+\-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+\-]?\d+)?"
    match = re.fullmatch(pattern + r"\s*(?:km|kilometres|kilometers)?", text, re.IGNORECASE)
    if not match:
        count = len(re.findall(r"\d+(?:\.\d+)?", text))
        return ParseResult(None, "multiple_numbers" if count > 1 else "non_numeric")
    value = float(re.match(pattern, text).group().replace(",", ""))
    if not math.isfinite(value) or value <= 0:
        return ParseResult(None, "non_positive_or_non_finite")
    if value > 20040:
        return ParseResult(None, "beyond_earth_diameter_arc")
    return ParseResult(value, "valid")
