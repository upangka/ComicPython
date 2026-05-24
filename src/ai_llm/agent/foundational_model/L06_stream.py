"""
L06_stream.py

This module demonstrates streaming capabilities in chat models, enabling real-time response generation.
It covers how to receive and process token-by-token output from language models, providing immediate
feedback and improved user experience in interactive applications.
"""
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

agent = create_agent(
    model=init_chat_model("deepseek:deepseek-v4-pro",
                          temperature=0.9,
                          extra_body={"thinking": {"type": "disabled"}}),
    system_prompt=SystemMessage("You are an excellent fiction writer")
)

input = {
    "messages": [
        HumanMessage("What's the capital of Moon?"),
        AIMessage("The capital of moon is 'Qater Garden'"),
        HumanMessage(
            "Oh,what a beautiful capital name! Can I meet a  gentle girl whose Chinese name is Lù Ēn(露恩) there? Answer me in English,then use a long dash to separate it,then translate it into Chinese.")
    ]
}

# event stream introduced in LangChain V1.3
for message in agent.stream_events(input, version="v3").messages:
    print(f"[{message.node}] ")
    for delta in message.text:
        print(delta, end="", flush=True)

print("\n", '━' * 100)
"""
https://docs.langchain.com/oss/python/langchain/streaming#llm-tokens
{'type': 'messages', 'ns': (), 'data': (AIMessageChunk(content='着歌谣，你确实很有可能遇到一个拥有如此美丽名字的温柔灵魂。月球的首都居住着许多奇迹，而那样的相遇定会是一次令人愉快的经历。', additional_kwargs={}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-2.5-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--019e5a24-9668-7e71-962a-1ec60c4f1963', tool_calls=[], invalid_tool_calls=[], usage_metadata={'output_tokens': 42, 'output_token_details': {'reasoning': 0}, 'input_tokens': 0, 'total_tokens': 42, 'input_token_details': {'cache_read': 0}}, tool_call_chunks=[]), {'ls_integration': 'langchain_chat_model', 'langgraph_step': 1, 'langgraph_node': 'model', 'langgraph_triggers': ('branch:to:model',), 'langgraph_path': ('__pregel_pull', 'model'), 'langgraph_checkpoint_ns': 'model:5f9371a8-ef28-097b-db7f-3771c5f55416', 'checkpoint_ns': 'model:5f9371a8-ef28-097b-db7f-3771c5f55416', 'ls_provider': 'google_genai', 'ls_model_name': 'gemini-2.5-flash', 'ls_model_type': 'chat', 'ls_temperature': 0.7})}
"""
count = 0
for chunk in agent.stream(input,
                          stream_mode="messages",
                          version="v2"):
    # type(chunk) is dict
    if chunk["type"] == "messages":
        # type(chunk['data']) is tuple(AIMessageChunk, dict)
        token, _ = chunk["data"]
        print(token.text, end="", flush=True)
    # print(f"{'━' * 20}【{(count := count + 1)}】{'━' * 20}")