"""
L07_structured_output.py

This module demonstrates structured output capabilities in chat models, enabling type-safe responses.
It covers how to define Pydantic models and JSON schemas to ensure language models return data
in predictable, validated formats suitable for programmatic processing and integration.
"""
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

from pydantic import BaseModel, Field


class CapitalInfo(BaseModel):
    name: str = Field(description="Name of the capital city")
    location: str = Field(description="Geographic location of the capital city")
    vibe: str = Field(description="General atmosphere or cultural feeling of the capital city")
    economy: str = Field(description="Economic profile or key industries of the capital city")


agent = create_agent(
    model=init_chat_model("deepseek:deepseek-v4-flash",
                          temperature=0.9,
                          extra_body={"thinking": {"type": "disabled"}}),
    system_prompt=SystemMessage("You are a excellent science fiction writer, create a capital city at user request."),
    response_format=CapitalInfo
)

result = agent.invoke({
    "messages": [HumanMessage("What is the capital city of the moon? Answer in Chinese")]
})

# print(result["structured_response"])

capital_info: CapitalInfo = result["structured_response"]
print(capital_info.model_dump_json(indent=2))

"""
{
  "name": "月华城 (Yuèhuá Chéng)",
  "location": "月球正面，风暴洋与雨海交界处的熔岩管网络内，坐标北纬18°、西经23°",
  "vibe": "一座被穹顶笼罩的银色不夜城，街道由发光苔藓铺就，空气里飘浮着淡淡的全息桂花香。居民穿着自适应织物制成的长袍，表面流转着如月光般的液态光泽。这里融合了东方古典美学与未来科技，茶馆里的机器人用宋代建盏奉茶，而窗外便是裸露的月球荒原。",
  "economy": "以氦-3聚变能源出口为核心支柱，辅以月面真空环境下的精密芯片制造、零重力生物制药，以及面向地球富人的\"月球度假村\"旅游业。月华证券交易所（MSE）交易着太阳系最前沿的量子加密资产。"
}
"""