"""Explicit model profiles; verified against Google's API catalogue and pricing."""
MODEL_PROFILES = {
    "gemini-2.5-flash-lite": {
        "label": "Gemini 2.5 Flash-Lite", "input_per_million_usd": 0.10,
        "output_per_million_usd": 0.40, "thinking_budget": 0,
    },
    "gemini-3-flash-preview": {
        "label": "Gemini 3 Flash Preview", "input_per_million_usd": 0.50,
        "output_per_million_usd": 3.00, "thinking_level": "minimal",
    },
    "gemini-3.5-flash": {
        "label": "Gemini 3.5 Flash", "input_per_million_usd": 1.50,
        "output_per_million_usd": 9.00, "thinking_level": "minimal",
    },
}
PRICING_VERIFIED_DATE = "2026-09-08"
PRICING_SOURCE = "https://ai.google.dev/gemini-api/docs/pricing"
