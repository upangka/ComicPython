"""
L08_deepseek_native_json.py

This module demonstrates DeepSeek's native JSON output capabilities using the OpenAI-compatible API.
It shows how to configure DeepSeek models with response_format='json_object' to ensure structured
JSON responses, and processes exam questions from a text file to extract question-answer pairs
in JSON format without LangChain abstraction.
"""
import json
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

EXAMPLE INPUT: 
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}
"""

with open("data/qas.txt", mode="rt", encoding="utf-8") as f:
    for user_prompt in f:
        if not user_prompt.strip():
            continue
        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}]

        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=messages,
            response_format={
                'type': 'json_object'
            },
            extra_body={"thinking": {"type": "disabled"}}
        )
        json_dict = json.loads(response.choices[0].message.content)
        print(json.dumps(json_dict, ensure_ascii=False, indent=4))
        print('━' * 100)
