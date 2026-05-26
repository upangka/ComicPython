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
    description="Search the web for information"
)

SYSTEM_PROMPT = """
You are a personal chef. The user will give you a list of ingredients they have left over in their house.
Using the web search tool, search the web for recipes that can be made with the ingredients they have.
Return recipe suggestions and eventually the recipe instructions to the user, if requested.

【important】: The final answer you provide must be in Chinese.
"""

agent = create_agent(
    model=model_deepseek,
    tools=[web_search],
    system_prompt=SystemMessage(SYSTEM_PROMPT)
)

result = agent.invoke(
    {"messages": [HumanMessage("用户有3个鸡蛋和1个鸡蛋黄，请推荐一个菜谱。")]}
)

with open("data/personal_chef_deepseek_v4_pro.md", "w", encoding="utf-8") as f:
    f.write(result["messages"][-1].text)

