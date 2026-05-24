"""
L01_using_deepseek_in_a_native_way.py

This module demonstrates how to use DeepSeek chat models in a native way
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
print('━'*100)
print(response.choices[0].message.reasoning_content)


"""
<class 'openai.types.chat.chat_completion.ChatCompletion'>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ChatCompletion(id='c33b3c75-70a7-49cc-a0e7-81d83f5a5de2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='AI learns patterns from data, then uses them to make decisions or predictions—without being explicitly programmed for every step.', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning_content="We need to explain how AI works in a few words. The user wants a concise explanation. I'll craft a short, simple explanation covering the core concept: AI learns patterns from data to make predictions or decisions without explicit programming. Keep it brief."))], created=1779615221, model='deepseek-v4-pro', object='chat.completion', service_tier=None, system_fingerprint='fp_9954b31ca7_prod0820_fp8_kvcache_20260402', usage=CompletionUsage(completion_tokens=74, prompt_tokens=12, total_tokens=86, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=None, reasoning_tokens=50, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0), prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=12))
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI learns patterns from data, then uses them to make decisions or predictions—without being explicitly programmed for every step.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
We need to explain how AI works in a few words. The user wants a concise explanation. I'll craft a short, simple explanation covering the core concept: AI learns patterns from data to make predictions or decisions without explicit programming. Keep it brief.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print('━'*100)
print(response.model_dump_json(indent=2))
"""
{
  "id": "c33b3c75-70a7-49cc-a0e7-81d83f5a5de2",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "AI learns patterns from data, then uses them to make decisions or predictions—without being explicitly programmed for every step.",
        "refusal": null,
        "role": "assistant",
        "annotations": null,
        "audio": null,
        "function_call": null,
        "tool_calls": null,
        "reasoning_content": "We need to explain how AI works in a few words. The user wants a concise explanation. I'll craft a short, simple explanation covering the core concept: AI learns patterns from data to make predictions or decisions without explicit programming. Keep it brief."
      }
    }
  ],
  "created": 1779615221,
  "model": "deepseek-v4-pro",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": "fp_9954b31ca7_prod0820_fp8_kvcache_20260402",
  "usage": {
    "completion_tokens": 74,
    "prompt_tokens": 12,
    "total_tokens": 86,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 50,
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