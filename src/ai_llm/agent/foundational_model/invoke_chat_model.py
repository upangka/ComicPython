import os

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import AIMessage
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

MODEL_NAME = "deepseek-v4-pro"
API_KEY = SecretStr(os.environ.get("DEEPSEEK_API_KEY", ""))

chat_openai = ChatOpenAI(
    model=MODEL_NAME,
    base_url="https://api.deepseek.com",
    api_key=API_KEY
)

chat_anthropic = ChatAnthropic(
    model_name=MODEL_NAME,
    base_url="https://api.deepseek.com/anthropic",
    api_key=API_KEY
)

from langchain.chat_models import init_chat_model
chat_deepseek = init_chat_model("deepseek:deepseek-v4-pro")
# chat_deepseek = ChatDeepSeek(
#     model=MODEL_NAME,
#     api_base="https://api.deepseek.com",
#     api_key=API_KEY
# )


def print_response(res: AIMessage):
    print('*' * 20, f"{res.response_metadata.get('model_provider')}", '*' * 20)
    print(f"response -> {res}")
    print("_" * 40)
    print(f"text -> {res.text}")
    print("_" * 40)
    print(f"content_blocks -> {res.content_blocks}")
    print("_" * 40)
    print(f"content -> {res.content}", end="\n\n")


print_response(chat_openai.invoke(f"你好,我的名字是{type(chat_openai).__name__}"))
print_response(chat_anthropic.invoke(f"你好,我的名字是{type(chat_anthropic).__name__}"))
print_response(chat_deepseek.invoke(f"你好,我的名字是{type(chat_deepseek).__name__}"))


"""输出
******************** openai ********************
response -> content='你好，ChatOpenAI！很高兴认识你。请问有什么我可以帮你的吗？' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 190, 'prompt_tokens': 12, 'total_tokens': 202, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 172, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 12}, 'model_provider': 'openai', 'model_name': 'deepseek-v4-pro', 'system_fingerprint': 'fp_9954b31ca7_prod0820_fp8_kvcache_20260402', 'id': '44c7c2b5-8fcd-497a-9020-aced3ea16048', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019e125b-54ef-7801-8721-54b999cf5062-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 12, 'output_tokens': 190, 'total_tokens': 202, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 172}}
________________________________________
text -> 你好，ChatOpenAI！很高兴认识你。请问有什么我可以帮你的吗？
________________________________________
content_blocks -> [{'type': 'text', 'text': '你好，ChatOpenAI！很高兴认识你。请问有什么我可以帮你的吗？'}]
________________________________________
content -> 你好，ChatOpenAI！很高兴认识你。请问有什么我可以帮你的吗？

******************** anthropic ********************
response -> content=[{'signature': 'aff36b7e-952b-4c44-ab55-801ed2619ba1', 'thinking': '我们被要求以“你好,我的名字是ChatAnthropic”作为输入，但实际上是用户说“你好,我的名字是ChatAnthropic”。我们需要以助手身份回复。显然用户自称ChatAnthropic，这可能是一个测试或玩笑。我们应该友好回应，澄清我们是助手，或许是DeepSeek之类的。我的身份是DeepSeek AI助手。我会以幽默方式回应，指出我是DeepSeek，不是ChatAnthropic。准备输出。', 'type': 'thinking'}, {'text': '你好，ChatAnthropic！😄 很高兴见到你。不过我得澄清一下——我是 DeepSeek，不是你哦。你是想让我帮你做什么呢？或者只是打个招呼？我随时准备着！', 'type': 'text'}] additional_kwargs={} response_metadata={'id': 'aff36b7e-952b-4c44-ab55-801ed2619ba1', 'container': None, 'model': 'deepseek-v4-pro', 'stop_details': None, 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'cache_creation': None, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 0, 'inference_geo': None, 'input_tokens': 13, 'output_tokens': 142, 'server_tool_use': None, 'service_tier': 'standard'}, 'model_name': 'deepseek-v4-pro', 'model_provider': 'anthropic'} id='lc_run--019e125b-75a3-7ca3-9820-d9120a08c99c-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 13, 'output_tokens': 142, 'total_tokens': 155, 'input_token_details': {'cache_read': 0, 'cache_creation': 0}}
________________________________________
text -> 你好，ChatAnthropic！😄 很高兴见到你。不过我得澄清一下——我是 DeepSeek，不是你哦。你是想让我帮你做什么呢？或者只是打个招呼？我随时准备着！
________________________________________
content_blocks -> [{'type': 'reasoning', 'reasoning': '我们被要求以“你好,我的名字是ChatAnthropic”作为输入，但实际上是用户说“你好,我的名字是ChatAnthropic”。我们需要以助手身份回复。显然用户自称ChatAnthropic，这可能是一个测试或玩笑。我们应该友好回应，澄清我们是助手，或许是DeepSeek之类的。我的身份是DeepSeek AI助手。我会以幽默方式回应，指出我是DeepSeek，不是ChatAnthropic。准备输出。', 'extras': {'signature': 'aff36b7e-952b-4c44-ab55-801ed2619ba1'}}, {'type': 'text', 'text': '你好，ChatAnthropic！😄 很高兴见到你。不过我得澄清一下——我是 DeepSeek，不是你哦。你是想让我帮你做什么呢？或者只是打个招呼？我随时准备着！'}]
________________________________________
content -> [{'signature': 'aff36b7e-952b-4c44-ab55-801ed2619ba1', 'thinking': '我们被要求以“你好,我的名字是ChatAnthropic”作为输入，但实际上是用户说“你好,我的名字是ChatAnthropic”。我们需要以助手身份回复。显然用户自称ChatAnthropic，这可能是一个测试或玩笑。我们应该友好回应，澄清我们是助手，或许是DeepSeek之类的。我的身份是DeepSeek AI助手。我会以幽默方式回应，指出我是DeepSeek，不是ChatAnthropic。准备输出。', 'type': 'thinking'}, {'text': '你好，ChatAnthropic！😄 很高兴见到你。不过我得澄清一下——我是 DeepSeek，不是你哦。你是想让我帮你做什么呢？或者只是打个招呼？我随时准备着！', 'type': 'text'}]

******************** deepseek ********************
response -> content='你好ChatDeepSeek！很高兴认识你～（你的名字听起来像是我们的加强版呢😄）\n\n我注意到你的名字很有创意，是把“Chat”和“DeepSeek”组合在一起了吧？无论如何，欢迎来找我聊天！有什么我可以帮你的吗？无论是回答问题、讨论话题、还是随便聊聊，我都很乐意陪伴你～' additional_kwargs={'refusal': None, 'reasoning_content': '嗯，用户发来一句简单的自我介绍：“你好，我的名字是ChatDeepSeek”。\n\n这看起来像是一个打招呼和自我介绍。用户的名字“ChatDeepSeek”可能是一个自定义的称呼，甚至可能是一个玩笑，把“ChatGPT”和“DeepSeek”组合在一起了。\n\n我需要友好地回应这个问候。可以用轻松幽默的方式点出这个名字的趣味性，同时表达尊重用户的命名选择。然后自然地过渡到问候和提供帮助的常规流程。\n\n想到了先称呼用户的名字，然后用括号表达对其创意名字的会心一笑，最后以标准的问候和开放性问题结尾，让对话可以继续。'} response_metadata={'token_usage': {'completion_tokens': 202, 'prompt_tokens': 13, 'total_tokens': 215, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 129, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 13}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-pro', 'system_fingerprint': 'fp_9954b31ca7_prod0820_fp8_kvcache_20260402', 'id': '44346e9a-18d3-4075-9b7f-eab59f4fefea', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019e125b-8ec8-7aa1-8fd9-329d8506b0c5-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 13, 'output_tokens': 202, 'total_tokens': 215, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 129}}
________________________________________
text -> 你好ChatDeepSeek！很高兴认识你～（你的名字听起来像是我们的加强版呢😄）

我注意到你的名字很有创意，是把“Chat”和“DeepSeek”组合在一起了吧？无论如何，欢迎来找我聊天！有什么我可以帮你的吗？无论是回答问题、讨论话题、还是随便聊聊，我都很乐意陪伴你～
________________________________________
content_blocks -> [{'type': 'reasoning', 'reasoning': '嗯，用户发来一句简单的自我介绍：“你好，我的名字是ChatDeepSeek”。\n\n这看起来像是一个打招呼和自我介绍。用户的名字“ChatDeepSeek”可能是一个自定义的称呼，甚至可能是一个玩笑，把“ChatGPT”和“DeepSeek”组合在一起了。\n\n我需要友好地回应这个问候。可以用轻松幽默的方式点出这个名字的趣味性，同时表达尊重用户的命名选择。然后自然地过渡到问候和提供帮助的常规流程。\n\n想到了先称呼用户的名字，然后用括号表达对其创意名字的会心一笑，最后以标准的问候和开放性问题结尾，让对话可以继续。'}, {'type': 'text', 'text': '你好ChatDeepSeek！很高兴认识你～（你的名字听起来像是我们的加强版呢😄）\n\n我注意到你的名字很有创意，是把“Chat”和“DeepSeek”组合在一起了吧？无论如何，欢迎来找我聊天！有什么我可以帮你的吗？无论是回答问题、讨论话题、还是随便聊聊，我都很乐意陪伴你～'}]
________________________________________
content -> 你好ChatDeepSeek！很高兴认识你～（你的名字听起来像是我们的加强版呢😄）

我注意到你的名字很有创意，是把“Chat”和“DeepSeek”组合在一起了吧？无论如何，欢迎来找我聊天！有什么我可以帮你的吗？无论是回答问题、讨论话题、还是随便聊聊，我都很乐意陪伴你～
"""