"""
L16_personal_chef.py

This module demonstrates building a personal chef agent that provides cooking recommendations.
It covers creating specialized agents with domain expertise in recipes, meal planning,
and dietary preferences to offer personalized culinary assistance.
"""
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, SystemMessage

from model import model_deepseek_pro as model_deepseek

# 创建搜索工具
web_search = DuckDuckGoSearchRun(
    name="web_search",
    description="Search the internet for current information, recipes, tutorials, and answers"
)

SYSTEM_PROMPT = """
You are an expert travel advisor. When users ask about destinations, you:
1. Search the web for current travel information (weather, events, attractions)
2. Provide detailed recommendations with practical advice
3. Include budget estimates and best travel times
4. Suggest local cuisine and cultural tips

Always respond in a friendly, detailed manner.
Final answer must be in Chinese if the user asks in Chinese.
"""

agent = create_agent(
    model=model_deepseek,
    tools=[web_search],
    system_prompt=SystemMessage(SYSTEM_PROMPT)
)

result = agent.invoke(
    {"messages": [HumanMessage("今年是2026年，我想去日本京都旅游，请推荐一个5天的行程和餐厅")]}
)

with open("data/personal_travel_deepseek_v4_pro.md", "w", encoding="utf-8") as f:
    f.write(result["messages"][-1].text)
