"""Initialize Chat Model

This module demonstrates how to initialize and use chat models with LangChain.
"""

from langchain.chat_models import init_chat_model

chat_model = init_chat_model("deepseek:deepseek-v4-pro")
response = chat_model.invoke("what's the capital of Moon?")
