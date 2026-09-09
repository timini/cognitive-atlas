import os
import time
from dataclasses import dataclass
from typing import Protocol

import httpx


@dataclass
class Reply:
    text: str
    payload: dict
    input_tokens: int
    output_tokens: int
    model_version: str
    latency_ms: float
    finish_reason: str


class ProviderError(Exception):
    def __init__(self, code, retryable=False, retry_after=0):
        super().__init__(code)
        self.code, self.retryable, self.retry_after = code, retryable, retry_after


class Provider(Protocol):
    async def query(self, model: str, prompt: str, parameters: dict) -> Reply: ...


class Gemini:
    def __init__(self, key=None, transport=None):
        self.key = key or os.environ.get("GEMINI_API_KEY")
        if not self.key:
            raise ValueError("Set GEMINI_API_KEY in .env or the environment")
        self.client = httpx.AsyncClient(timeout=60, transport=transport)

    async def close(self):
        await self.client.aclose()

    async def query(self, model, prompt, parameters):
        config = {"temperature": parameters["temperature"], "topP": parameters["top_p"],
                  "maxOutputTokens": parameters["max_tokens"]}
        if 'response_json_schema' in parameters:
            if parameters.get('response_mime_type') != 'application/json':
                raise ValueError('A JSON response schema requires application/json')
            config['responseMimeType'] = 'application/json'
            config['responseJsonSchema'] = parameters['response_json_schema']
        if "thinking_level" in parameters:
            config["thinkingConfig"] = {"thinkingLevel": parameters["thinking_level"]}
        elif "thinking_budget" in parameters:
            config["thinkingConfig"] = {"thinkingBudget": parameters["thinking_budget"]}
        if parameters.get("seed") is not None:
            config["seed"] = parameters["seed"]
        body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
                "generationConfig": config}
        if parameters.get("system_prompt"):
            body["systemInstruction"] = {"parts": [{"text": parameters["system_prompt"]}]}
        started = time.monotonic()
        try:
            response = await self.client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                headers={"x-goog-api-key": self.key}, json=body)
        except httpx.TimeoutException:
            raise ProviderError("timeout", True) from None
        except httpx.TransportError:
            raise ProviderError("transport_error", True) from None
        if response.status_code != 200:
            # Never persist HTTP request headers or exceptions which might expose secrets.
            try:
                delay = float(response.headers.get("retry-after", 0))
            except ValueError:
                delay = 0
            raise ProviderError(f"http_{response.status_code}",
                                response.status_code in (408, 429, 500, 502, 503, 504), delay)
        payload = response.json()
        candidates = payload.get("candidates", [])
        candidate = candidates[0] if candidates else {}
        text = "".join(p.get("text", "") for p in candidate.get("content", {}).get("parts", [])
                       if not p.get("thought"))
        usage = payload.get("usageMetadata", {})
        return Reply(text, payload, usage.get("promptTokenCount", 0),
                     usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0),
                     payload.get("modelVersion", model), (time.monotonic() - started) * 1000,
                     candidate.get("finishReason", "BLOCKED"))


PROVIDERS = {"google": Gemini}
