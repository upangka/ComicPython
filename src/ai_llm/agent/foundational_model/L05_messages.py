"""
L05_messages.py

This module covers message handling in chat models, including user messages,
assistant responses, and system messages. It demonstrates the structure and processing
of different message types in LangChain chat interactions.
"""

from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# model = init_chat_model("deepseek:deepseek-v4-pro",
#                           temperature=0.9,
#                           extra_body={"thinking": {"type": "disabled"}})
agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=SystemMessage("You are an excellent fiction writer")
)

result = agent.invoke({
    "messages": [
        HumanMessage("What's the capital of Moon?"),
        AIMessage("The capital of moon is 'Qater Garden'"),
        HumanMessage(
            "Oh,what a beautiful capital name! Can I meet a  gentle girl whose Chinese name is Lù Ēn(露恩) there? Answer me in English,then use a long dash to separate it,then translate it into Chinese.")
    ]
})

print(type(result))  # type dict
print(type(result["messages"]))  # type list
print(result["messages"][-1].text)
