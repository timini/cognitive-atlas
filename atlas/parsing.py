"""Strict numeric protocol; never extract a convenient number from prose."""
import math
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ParseResult:
    value: float | None
    quality: str


def parse_distance(raw, protocol="legacy"):
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
