"""
L15_duckduckgo_search.py

This module demonstrates how to integrate DuckDuckGo search tool into LangChain agents.
It covers using web search capabilities to retrieve real-time information, enabling agents
to access current data and provide up-to-date responses in conversations.
"""
from langchain_community.tools import DuckDuckGoSearchRun
# 创建搜索工具
search = DuckDuckGoSearchRun()
print(type(search))

# 执行一次搜索
result = search.invoke("LangChain Python 教程")
# 打印结果
print("搜索成功！返回内容如下：\n")
print(result)