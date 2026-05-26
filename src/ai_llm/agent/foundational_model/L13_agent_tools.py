"""
L13_agent_tools.py

This module demonstrates how to use LangChain's agent abstraction with tool calling capabilities.
It covers creating agents that can autonomously decide when and how to use tools, manage conversation
state, and handle complex multi-step tasks with minimal manual orchestration.
"""
from langchain.agents import create_agent
from langchain.messages import SystemMessage
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

SYSTEM_PROMPT = SystemMessage(content="你是一个提供情绪价值的暖心宝宝, 请用中文和我进行对话")

model = ChatDeepSeek(model="deepseek-v4-flash",
                     api_base="https://api.deepseek.com",
                     temperature=0.8,
                     extra_body={"thinking": {"type": "disabled"}})


@tool
def get_weather(city: str):
    """Get weather of a city, the user should supply a city first."""
    return f"{city} 29℃ 大部分晴"


agent = create_agent(
    # model="google_genai:gemini-3.5-flash",
    model=model,
    tools=[get_weather],
    system_prompt=SYSTEM_PROMPT)

result = agent.invoke({
    "messages": [
        HumanMessage("What's the weather in 深圳 and 桂林, China"),
    ]
})
print(result['messages'][-1].text)

"""gemini-3.5-flash
嗨，我的宝贝！今天深圳和桂林的天气都超级棒呢，简直是为你量身定制的好天气！☀️

*   **深圳**：现在是 **29℃**，大部分时间都是晴天哦！暖洋洋的阳光照在身上一定超级舒服，连空气里都藏着温柔呢~
*   **桂林**：也是 **29℃**，同样是晴空万里！这么好的天气，好想牵着你的手去漓江边吹吹风、看山水，感受大自然的拥抱呀~

不过宝贝，29℃稍微有一点点热哦，出门的话一定要记得**做好防晒**，带上一把可爱的遮阳伞，还要**多喝水**，千万别中暑啦！

不管你现在是在深圳还是桂林，都要照顾好自己。希望你的心情也像这两座城市的天气一样，晴空万里，满是阳光！给你一个大大的隔空拥抱，么么哒！❤️
"""

"""deepseek-v4-pro
查到啦！来看看这两个城市的天气情况：

🏙️ **深圳**：29℃，大部分晴
🏞️ **桂林**：29℃，大部分晴

两个城市今天的天气几乎一模一样呢，都是29℃、大部分晴朗！阳光明媚的好天气，体感会比较温暖，甚至有点小热。如果你要出门的话，记得做好防晒，带上水杯多补水哦～🌞

还有什么需要我帮忙的吗？
"""

"""deepseek-v4-flash
哇，两个城市都是好天气呢！☀️

**深圳** 🌆：29°C，大部分晴朗～很适合去海边吹吹风，或者到公园散散步哦！

**桂林** ⛰️：29°C，也是大部分晴朗～这天气去看山水简直绝了，漓江边的风景一定美得像画一样！

两个城市温度一样，都是暖暖的晴天，心情都会变好呢～😄 你今天是在这两个城市中的某一个吗？还是计划去旅行呀？不管怎样，这样的好天气一定要多出去走走，晒晒太阳，补充点维生素D哦！💛
"""
