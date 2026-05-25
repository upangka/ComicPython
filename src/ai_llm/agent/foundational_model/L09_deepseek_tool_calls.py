"""
L09_deepseek_tool_calls.py

This module demonstrates DeepSeek's tool calling capabilities with thinking mode disabled.
It covers how to configure DeepSeek models to use external tools and functions while keeping
the reasoning/thinking mode turned off for faster response times in production applications.
"""
import json
import os
from dataclasses import dataclass

from openai import OpenAI


@dataclass
class WeatherParams:
    city: str


def get_weather(params: WeatherParams):
    print('*' * 25, "tool call start", '*' * 25)
    print(f"Getting weather for {params.city}")
    print('*' * 25, "tool call  end", '*' * 25)
    return f"{params.city} 29℃ 大部分晴"


tools_dict = {tool.__name__: tool for tool in [get_weather]}


def send_message(messages):
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        tools=tools
    )
    return response.choices[0].message


client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# manually define tools schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name only, without country or state, e.g. San Francisco",
                    }
                },
                "required": ["city"]
            },
        }
    },
]

messages = [{"role": "user", "content": "What's the weather in ShenZhen, China"}]
# messages = [{"role": "user", "content": "I'm recharging and studying right now in the ShenZhen Library."}]

message = send_message(messages)
print(message.model_dump_json(indent=4))
messages.append(message)
if message.tool_calls:
    tool_call = message.tool_calls[0]
    func_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    observation = tools_dict.get(func_name)(WeatherParams(**args))

    messages.append({"role": "tool", "content": observation, "tool_call_id": tool_call.id})
    message = send_message(messages)
    print(message.content)
    print(getattr(message, "reasoning_content"))


"""
{
    "content": "",
    "refusal": null,
    "role": "assistant",
    "annotations": null,
    "audio": null,
    "function_call": null,
    "tool_calls": [
        {
            "id": "call_00_2khQSjI08eZSazBQfs2T8575",
            "function": {
                "arguments": "{\"city\": \"ShenZhen\"}",
                "name": "get_weather"
            },
            "type": "function",
            "index": 0
        }
    ],
    "reasoning_content": "The user is asking for the weather in ShenZhen, China. I should use the get_weather function with the city name \"ShenZhen\" (just the city name, without country or state as per the description)."
}
************************* tool call start *************************
Getting weather for ShenZhen
************************* tool call  end *************************
深圳目前的天气是 **29°C**，大部分晴朗 ☀️。
The weather in ShenZhen is 29°C and mostly clear (大部分晴 means "mostly clear/fair"). Let me present this to the user.
"""