# Querying Available LLM Models: REST API vs OpenAI SDK

> A practical guide to listing models from DeepSeek (and other OpenAI-compatible providers) using two complementary approaches.

---

## Overview

When building LLM-powered applications, you often need to **dynamically discover which models are available** from a given provider. This post covers two techniques demonstrated in `L10_model_list.py` and `L11_openai_models.py`:

| Approach | Tool | File |
|---|---|---|
| Raw HTTP request | `requests` library | `L10_model_list.py` |
| SDK abstraction | `openai` Python SDK | `L11_openai_models.py` |

Both examples target the **DeepSeek API**, which exposes an OpenAI-compatible interface.

---

## Approach 1 — Raw HTTP Request (`requests`)

`L10_model_list.py`

```python
import os
import requests

token = os.getenv("DEEPSEEK_API_KEY")

response = requests.get(
    "https://api.deepseek.com/models",
    headers={"Authorization": f"Bearer {token}"}
)

if response.status_code == 200:
    models = response.json()
    for model in models['data']:
        print(model['id'])
else:
    raise Exception(f"Error: {response.status_code}")
```

### How It Works

1. **Authentication** — The API key is read from the `DEEPSEEK_API_KEY` environment variable and passed as a `Bearer` token in the `Authorization` header.
   2. **HTTP GET** — A `GET` request is sent to the `/models` endpoint.
   3. **Response parsing** — On HTTP 200, the JSON payload is deserialized. The `data` array contains model objects, each with an `id`, `object`, and `owned_by` field.
   4. **Error handling** — Any non-200 status code raises an exception immediately.

### Sample Output

```
deepseek-v4-flash
deepseek-v4-pro
```

### When to Use This Approach

- You want **zero SDK dependency** and full control over the HTTP layer.
  - You need to target endpoints that no official SDK supports yet.
  - You prefer working directly with raw JSON for further processing or logging.

---

## Approach 2 — OpenAI SDK Abstraction

`L11_openai_models.py`
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

print(client.models.list().to_json(indent=4))
```

### How It Works

1. **Client instantiation** — An `OpenAI` client is created with two key parameters:
   - `api_key`: your DeepSeek API key.
   - `base_url`: overrides the default OpenAI endpoint to point at DeepSeek's API.
   2. **Model listing** — `client.models.list()` returns a typed response object.
   3. **Serialization** — `.to_json(indent=4)` converts the response to a pretty-printed JSON string for inspection.

### Sample Output

```json
{
    "data": [
        {
            "id": "deepseek-v4-flash",
            "object": "model",
            "owned_by": "deepseek"
        },
        {
            "id": "deepseek-v4-pro",
            "object": "model",
            "owned_by": "deepseek"
        }
    ],
    "object": "list"
}
```

### When to Use This Approach

- You are already using the `openai` SDK elsewhere in your project.
  - You want **type-safe** response objects with IDE auto-completion.
  - You need to switch between OpenAI and OpenAI-compatible providers (DeepSeek, Azure OpenAI, etc.) by simply changing `base_url`.

---

## Comparing the Two Approaches

| Dimension | `requests` (L10) | `openai` SDK (L11) |
|---|---|---|
| Dependencies | `requests` | `openai` |
| Response type | Raw `dict` | Typed SDK object |
| Serialization | Manual (`response.json()`) | Built-in (`.to_json()`) |
| Provider switching | Change URL string | Change `base_url` parameter |
| Error handling | Manual status-code check | SDK raises typed exceptions |
| Boilerplate | Slightly more | Minimal |

---

## Key Takeaways

- **DeepSeek's API is OpenAI-compatible**, meaning the standard `openai` Python SDK works out-of-the-box by simply pointing `base_url` at DeepSeek's endpoint.
  - **Environment variables** (`DEEPSEEK_API_KEY`) are the recommended way to manage API keys — never hard-code credentials.
  - **Dynamic model discovery** is useful for building provider-agnostic applications that adapt to newly released models without code changes.
  - Both approaches return the same underlying data: a list of models, each identified by an `id` string (e.g., `deepseek-v4-flash`, `deepseek-v4-pro`).

---

## Environment Setup

Both scripts require the `DEEPSEEK_API_KEY` environment variable. Store it in a `.env` file at the project root:

```
DEEPSEEK_API_KEY=your_api_key_here
```

Then load it with `python-dotenv` or let your shell/IDE inject it automatically.

---

*Part of the **Foundational LLM Models** series — exploring core patterns for building LLM-powered applications with Python, LangChain, DeepSeek, and OpenAI-compatible APIs.*
