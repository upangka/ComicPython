"""Initialize Chat Model

This module demonstrates how to initialize and use chat models with LangChain.
"""

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
chat_model = init_chat_model("deepseek:deepseek-v4-pro")
response = chat_model.invoke("what's the capital of Moon?")


agent= create_agent(model=chat_model)
agent.invoke({
    "messages":[{"role": "user", "content": "what's the capital of Moon?"}]
})
