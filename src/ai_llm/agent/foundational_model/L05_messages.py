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

"""
Lù Ēn, what a fitting and lovely name for someone in Qater Garden! You certainly can feel her presence there. She isn't a girl you'd meet in a bustling marketplace, but rather a gentle spirit woven into the very fabric of the Moon's capital. Some say she is the whisper of the lunar wind, others believe she is the glimmer in the dewdrop that never falls, reflecting the Earth's beauty. If you listen closely to the silent hum of Qater Garden and open your heart to its serene beauty, you might just sense her delicate grace, a comforting presence that embodies the moon's gentle light.
—
露恩，多么适合且可爱的名字，尤其是在Qater Garden！你当然能感受到她的存在。她不是那种你会在熙熙攘攘的市场里遇到的女孩，而是一个温柔的灵魂，编织在月球首都的每一寸肌理之中。有人说她是月亮风的低语，另一些人则相信她是永不坠落的露珠中闪烁的光芒，映照着地球的美丽。如果你仔细聆听Qater Garden寂静的低吟，并向其宁静之美敞开心扉，你或许就能感受到她那精致的优雅，一种舒适的存在，它体现着月亮温柔的光芒。
"""