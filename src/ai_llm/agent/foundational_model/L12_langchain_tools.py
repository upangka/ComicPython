"""
L12_langchain_tools.py

This module demonstrates how to use LangChain models with tool calling capabilities.
It covers integrating external tools and functions with LangChain chat models, enabling
models to perform actions like API calls, data retrieval, and complex computations.
"""

import logging

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import ToolMessage

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@tool
def get_weather(city: str):
    """Get weather of a city, the user should supply a city first."""
    return f"{city} 29℃ 大部分晴"


tools_by_name = {t.name: t for t in [get_weather]}
# print(get_weather.invoke({"city": "北京"}))
# print(get_weather.invoke("北京"))

# LangChain drops reasoning_content when serializing AIMessage back to the API.
# Fix: disable  thinking mode
model = init_chat_model("deepseek:deepseek-v4-pro",
                        api_base="https://api.deepseek.com",
                        extra_body={"thinking": {"type": "disabled"}})

model_with_tools = model.bind_tools([get_weather])

messages = [{"role": "user", "content": "What's the weather in 深圳 and 桂林, China"}]

ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    logger.debug(tool_call)
    tool = tools_by_name[tool_call['name']]
    observation = tool.invoke(tool_call)
    logger.debug(f"is type of observation is ToolMessage: {isinstance(observation, ToolMessage)}")
    logger.debug(f"observation: {observation}")
    messages.append(observation)

final_ai_msg = model_with_tools.invoke(messages)
print(final_ai_msg.text)

"""
2026-05-26 12:06:02,573 - __main__ - DEBUG - {'name': 'get_weather', 'args': {'city': '深圳'}, 'id': 'call_00_t4gl52OrRyGzE4w11cKz5492', 'type': 'tool_call'}
2026-05-26 12:06:02,574 - __main__ - DEBUG - is type of observation is ToolMessage: True
2026-05-26 12:06:02,574 - __main__ - DEBUG - observation: content='深圳 29℃ 大部分晴' name='get_weather' tool_call_id='call_00_t4gl52OrRyGzE4w11cKz5492'
2026-05-26 12:06:02,574 - __main__ - DEBUG - {'name': 'get_weather', 'args': {'city': '桂林'}, 'id': 'call_01_dPWYyOWFrICLEs1o0M2h1118', 'type': 'tool_call'}
2026-05-26 12:06:02,574 - __main__ - DEBUG - is type of observation is ToolMessage: True
2026-05-26 12:06:02,575 - __main__ - DEBUG - observation: content='桂林 29℃ 大部分晴' name='get_weather' tool_call_id='call_01_dPWYyOWFrICLEs1o0M2h1118'
Here's the weather for both cities:

| 城市 | 温度 | 天气状况 |
|------|------|----------|
| **深圳** | 29℃ | 大部分晴 |
| **桂林** | 29℃ | 大部分晴 |

两地目前都是29℃，天气以晴为主，看来今天华南地区天气都不错！适合出行和户外活动。
"""
