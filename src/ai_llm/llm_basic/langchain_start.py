from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(
    model_name="deepseek-v4-flash",
    # thinking={
    #     "type": "disabled",
    # }
)


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="你是一个强大的AI助手，请用中文回答我的。",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "深圳今天的天气是什么"}]}
)

print(type(result), result)
print("-" * 50)
print(result["messages"][-1].content_blocks)
