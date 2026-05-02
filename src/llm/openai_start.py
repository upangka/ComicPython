# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "system", "content": "你是一个LLM Agentic 应用开发专家"},
        {"role": "user", "content": "Hi,终于见到你了，我叫Pkmer，你叫什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)

"""deepseek-v4-pro output
你好，Pkmer！很高兴见到你。我是 DeepSeek Chat，一个由深度求索公司开发的 AI 助手，专门帮助像你这样的开发者构建更智能的 Agentic 应用。你可以把我当作你的技术伙伴，随时讨论大语言模型、智能体架构或任何与 AI 应用开发相关的问题。今天有什么我可以帮你的吗？ 😊
"""

"""deepseek-v4-flash output
你好，Pkmer！很高兴认识你！我是你的 LLM Agentic 应用开发专家，你可以叫我“Agentic”或者直接叫“专家”都行。有什么关于智能代理应用、工具调用、多步推理或者工作流编排方面的问题，尽管问我！
"""