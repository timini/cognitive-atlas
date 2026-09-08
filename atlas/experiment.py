import importlib.metadata
import json
import platform
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from atlas import languages
from atlas.data import digest, generate_pairs, load_places, write_csv
from atlas.models import MODEL_PROFILES, PRICING_SOURCE, PRICING_VERIFIED_DATE

PROMPTS = {
    "en": "Estimate the straight-line great-circle distance in kilometres between {city_a}, {country_a} and {city_b}, {country_b}. Return only your best numerical estimate in kilometres. Do not explain your reasoning.",
    "fr": "Estimez la distance à vol d’oiseau, suivant un grand cercle, en kilomètres entre {city_a}, {country_a} et {city_b}, {country_b}. Répondez uniquement par votre meilleure estimation numérique en kilomètres, sans expliquer votre raisonnement.",
}


def utcnow():
    return datetime.now(UTC).isoformat()


def prompt_for(manifest, pair, places):
    a, b = places[pair["place_a_id"]], places[pair["place_b_id"]]
    return manifest["prompt_template"].format(city_a=a["capital_name"], country_a=a["country_name"],
                                               city_b=b["capital_name"], country_b=b["country_name"])


def create_experiment(dataset, root="runs", samples=10, model="gemini-2.5-flash-lite",
                      language="en", temperature=1.0, max_cost=1.0, rpm=120, concurrency=4,
                      prompt_template=None, provider="google", max_attempts=4, max_tokens=128,
                      protocol="legacy", shared_rpm=None):
    if not 1 <= samples <= 1000 or not 0 < max_cost or rpm <= 0 or concurrency < 1 or max_attempts < 1:
        raise ValueError("Invalid experiment limits")
    places = load_places(dataset)
    if model not in MODEL_PROFILES or provider != "google":
        raise ValueError("Supply a verified model profile and pricing before enabling another model")
    if not 16 <= max_tokens <= 4096:
        raise ValueError("max_tokens must be between 16 and 4096")
    if protocol not in ("legacy", languages.PROTOCOL_ID):
        raise ValueError("Unknown prompt protocol")
    if protocol != "legacy" and (language not in languages.PROMPTS or prompt_template is not None):
        raise ValueError("Use a registered translation for the language protocol")
    profile = MODEL_PROFILES[model]
    try:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
    except subprocess.CalledProcessError:
        revision = "uncommitted"
    config = {"schema_version": 2, "name": f"{len(places)}-capital distance experiment", "provider": provider,
              "model_label": profile["label"],
              "model": model, "requested_model_version": model, "language": language,
              "prompt_template": prompt_template or (languages.PROMPTS[language] if protocol != "legacy" else PROMPTS[language]), "sampling_count": samples,
              "parameters": {"temperature": temperature, "top_p": 0.95, "max_tokens": max_tokens,
                             **{k: v for k, v in profile.items() if k.startswith("thinking_")},
                             "seed": None, "system_prompt": ""},
              "dataset_sha256": digest(places), "dataset_file": Path(dataset).name,
              "sampling_strategy": "independent_single_turn_unordered_pairs_fixed_id_order",
              "created_at": utcnow(), "code_revision": revision,
              "software": {"python": platform.python_version(), **{
                  p: importlib.metadata.version(p) for p in ["numpy", "scipy", "scikit-learn", "geographiclib"]}},
              "execution": {"max_cost_usd": max_cost, "requests_per_minute": rpm,
                            "concurrency": concurrency, "max_attempts": max_attempts,
                            "retry_policy": "Retry transport/408/429/5xx only; invalid content is terminal",
                            "budget_policy": "Reserve conservatively in flight; reconcile successful responses to reported usage; retain unknown-attempt reservations"},
              "pricing": {"input_per_million_usd": profile["input_per_million_usd"],
                          "output_per_million_usd": profile["output_per_million_usd"],
                          "source": PRICING_SOURCE, "verified_date": PRICING_VERIFIED_DATE,
                          "checked_at": utcnow(), "billing_note": "Token-based estimate, not an invoice"}}
    if protocol != "legacy":
        config.update(prompt_template=languages.PROMPTS[language], prompt_family=protocol,
                      response_parser=languages.PARSER_ID, entity_name_policy=languages.ENTITY_NAME_POLICY,
                      language_label=languages.LANGUAGE_LABELS[language],
                      translation_review=languages.TRANSLATION_REVIEW)
    if shared_rpm is not None:
        if shared_rpm <= 0:
            raise ValueError("Shared request rate must be positive")
        config["execution"].update(shared_requests_per_minute=shared_rpm,
            shared_rate_policy="Shared process limiter; on 429 pause all and halve rate at most once per minute")
    config["id"] = digest(config)[:24]
    directory = Path(root) / config["id"]
    directory.mkdir(parents=True, exist_ok=False)
    with (directory / "manifest.json").open("x") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    write_csv(directory / "places.csv", places)
    write_csv(directory / "pairs.csv", generate_pairs(places))
    return directory


def estimate(manifest, places, pairs):
    prompts = [prompt_for(manifest, p, {v["id"]: v for v in places}) for p in pairs]
    calls = len(pairs) * manifest["sampling_count"]
    # Estimate at four characters/token; ceiling conservatively uses UTF-8 bytes/token.
    tokens = sum(len(p.encode()) / 4 for p in prompts) * manifest["sampling_count"]
    output = calls * manifest["parameters"]["max_tokens"]
    pricing = manifest["pricing"]
    cost = (tokens * pricing["input_per_million_usd"] + output * pricing["output_per_million_usd"]) / 1e6
    return {"capitals": len(places), "pairs": len(pairs), "calls": calls,
            "estimated_input_tokens": round(tokens), "maximum_output_tokens": output,
            "estimated_cost_usd": cost, "budget_usd": manifest["execution"]["max_cost_usd"]}
