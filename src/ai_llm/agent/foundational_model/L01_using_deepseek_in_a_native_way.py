"""
L01_using_deepseek_in_a_native_way.py

This module demonstrates how to use DeepSeek chat models in a native way through LangChain.
It covers the initialization of DeepSeek models using the init_chat_model function,
configuring API endpoints, and setting model-specific parameters such as disabling
the thinking mode. This serves as a foundational example for integrating DeepSeek's
advanced language models into Python applications.
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages = [
        {"role": "user", "content": "Explain how AI works in a few words"}
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(type(response))
print('━'*100)
print(response)
print('━'*100)
print(response.choices[0].message.content)


"""
<class 'openai.types.chat.chat_completion.ChatCompletion'>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ChatCompletion(id='0da62eec-bbdd-478a-a9e0-8c82941c1321', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='AI learns patterns from data to make predictions or decisions.', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning_content='We need to explain how AI works in a few words. The user asked: "Explain how AI works in a few words". I need to provide a concise, understandable explanation.\n\nI should consider what "AI" refers to here—likely modern AI like machine learning, neural networks. I\'ll craft a very short, memorable explanation.\n\nOptions: "AI learns patterns from data to make predictions or decisions." That\'s short. Could also say: "AI uses algorithms to find patterns in data and then applies those patterns to new situations." But "in a few words" might mean a single sentence or a phrase. I\'ll aim for a one-sentence explanation that captures the essence.\n\nI\'ll answer: "AI learns from examples to recognize patterns and make predictions." That\'s simple. Or: "AI is pattern recognition at scale, trained on data." I\'ll provide a clear, concise definition.'))], created=1779612108, model='deepseek-v4-pro', object='chat.completion', service_tier=None, system_fingerprint='fp_9954b31ca7_prod0820_fp8_kvcache_20260402', usage=CompletionUsage(completion_tokens=192, prompt_tokens=12, total_tokens=204, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=180, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0), prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=12))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI learns patterns from data to make predictions or decisions.
"""

print(response.model_dump_json(indent=2))
"""
{
  "id": "4ce86d0b-38e3-482c-a137-085c659e420b",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "AI learns patterns from data, then uses those patterns to make predictions or decisions.",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "reasoning_content": "We need to explain how AI works in a few words. \"In a few words\" implies a very concise explanation. I need to capture the essence of AI, likely modern machine learning, in a very short, pithy phrase or a few sentences. The user might be expecting something like: \"AI learns patterns from data to make predictions or decisions.\" That's a common one-liner. Alternatively, \"Algorithms trained on data to recognize patterns and make decisions.\" I'll craft a very short, clear explanation. It says \"in a few words,\" so I'll keep it to a single sentence or a phrase. I'll respond with something like: \"AI learns from examples to spot patterns and make decisions.\" I can also mention neural networks as a common method. But I'll keep it ultra-simple."
      }
    }
  ],
  "created": 1779612243,
  "model": "deepseek-v4-pro",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_9954b31ca7_prod0820_fp8_kvcache_20260402",
  "usage": {
    "completion_tokens": 182,
    "prompt_tokens": 12,
    "total_tokens": 194,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 165,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0
    },
    "prompt_cache_hit_tokens": 0,
    "prompt_cache_miss_tokens": 12
  }
}
"""