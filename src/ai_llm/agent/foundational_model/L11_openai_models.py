"""
L11_openai_models.py

This module demonstrates how to list available models using the OpenAI SDK.
It covers retrieving model information from OpenAI-compatible APIs, including DeepSeek,
and managing model metadata for dynamic selection in applications.
"""

import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

print(client.models.list().to_json(indent=4))

"""
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
"""
