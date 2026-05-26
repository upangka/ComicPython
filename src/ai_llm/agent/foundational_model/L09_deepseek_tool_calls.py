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

messages = [{"role": "user", "content": "What's the weather in 桂林 and 深圳, China"}]
# messages = [{"role": "user", "content": "I'm recharging and studying right now in the ShenZhen Library."}]

message = send_message(messages)
print(message.model_dump_json(indent=4))
messages.append(message)
if message.tool_calls:
    # Execute ALL tool calls and collect every result before sending the next request.
    # The API requires one tool message per tool_call_id in the assistant message.
    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        observation = tools_dict.get(func_name)(WeatherParams(**args))
        messages.append({"role": "tool", "content": observation, "tool_call_id": tool_call.id})

    # Send a single follow-up request only after all tool results are appended.
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
            "id": "call_00_CcFstJQuBwR1gWqAVFhO0203",
            "function": {
                "arguments": "{\"city\": \"桂林\"}",
                "name": "get_weather"
            },
            "type": "function",
            "index": 0
        },
        {
            "id": "call_01_frwSN5l8QR7SblOAXh4p6825",
            "function": {
                "arguments": "{\"city\": \"深圳\"}",
                "name": "get_weather"
            },
            "type": "function",
            "index": 1
        }
    ],
    "reasoning_content": "The user is asking for weather in two cities in China: 桂林 (Guilin) and 深圳 (Shenzhen). I need to make two separate weather API calls for these cities."
}
************************* tool call start *************************
Getting weather for 桂林
************************* tool call  end *************************
************************* tool call start *************************
Getting weather for 深圳
************************* tool call  end *************************
以下是桂林和深圳的天气情况：

| 城市 | 温度 | 天气状况 |
|------|------|----------|
| **桂林** | 29℃ | 🌤️ 大部分晴 |
| **深圳** | 29℃ | 🌤️ 大部分晴 |

两个城市的天气非常相似，都是29°C，大部分晴朗。天气不错，适合外出活动！有什么其他需要了解的吗？
Both weather results are in. Let me summarize:

- 桂林 (Guilin): 29°C, 大部分晴 (mostly sunny)
- 深圳 (Shenzhen): 29°C, 大部分晴 (mostly sunny)
"""