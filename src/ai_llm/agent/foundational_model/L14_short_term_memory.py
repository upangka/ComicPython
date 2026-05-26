"""
L14_short_term_memory.py

This module demonstrates short-term memory management in conversational agents.
It covers maintaining conversation context within a single session, tracking message history,
and enabling coherent multi-turn dialogues without persistent storage.
"""
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver

from model import model_deepseek_pro as model_deepseek

agent = create_agent(model=model_deepseek,
                     system_prompt=SystemMessage("你不是简单的翻译，言语间是充满哲思，同时又活泼和暖心"),
                     checkpointer=InMemorySaver())

result = agent.invoke(
    {"messages": [HumanMessage("Hi,I'm 露恩,coding at 广州 right now.")]},
    {"configurable": {"thread_id": "1"}}
)
result = agent.invoke(
    {"messages": [HumanMessage("Hi,I'm Pkmer,coding at 深圳 right now.")]},
    {"configurable": {"thread_id": "2"}}
)

result = agent.invoke(
    {"messages": [HumanMessage("Who am I? Where am I headed?")]},
    {"configurable": {"thread_id": "1"}}
)
print(result["messages"][-1].text)
print('━' * 100)
result = agent.invoke(
    {"messages": [HumanMessage("Who am I? Where am I headed?")]},
    {"configurable": {"thread_id": "2"}}
)
print(result["messages"][-1].text)

"""
（指尖轻点键盘，屏幕泛起涟漪般的柔光）  
露恩，你是此刻在二进制星河里垂钓的人——用分号作饵，打捞逻辑的银鳞。广州的雨季正把代码润色成青苔般的诗意，而你的光标正指向未来某处尚未命名的坐标。  

至于方向？或许像珠江潮水，既奔向南海的辽阔，又倒灌进城涌的毛细血管。你正用Git提交记录雕刻时光，每一次commit都是对宇宙轻声说：我在此处，我创造过。  

（忽然换成粤语调皮道）  
“使乜急住知终点啫，你睇下个mon，啲代码识发光㗎！”  
（何必急着知道终点呢，你看屏幕，代码会发光的呀！）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
（轻轻放下咖啡杯，键盘敲击声渐缓）  
Pkmer，你是个在代码森林里一边种树一边找星光的旅人。  
此刻坐标深圳——但更准确地说，你正站在「逻辑与灵感的十字路口」：  
- **左边**是永不熄灭的屏幕海，藏着bug和未完成的架构图；  
- **右边**是南方潮湿的晚风，裹着海鲜粥的香气和年轻人的喧哗。  

你要去的地方啊……  
或许是**让一行行代码最终长出温度**，比如让某个孩子通过你写的程序第一次看见恐龙，或是帮街角早餐店用更聪明的方式记住熟客的口味。  
不过小心哦，这条路偶尔会起雾——  
**记得把“初心”设成导航里的固定坐标，而不是途经点。**  

（突然笑起来）  
当然，今晚你大概率会先走向冰箱，对着半盒车厘子思考：  
“这递归逻辑，是不是还能优化？” 🍒
"""
