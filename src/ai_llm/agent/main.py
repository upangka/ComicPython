import os
from pprint import pprint

from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
def mask_key(key):
    key = os.getenv(key)
    if len(key) < 5:
        return key
    else:
        return key[:2] + "*" * 4 + key[-2:]

# from dotenv import load_dotenv
# load_dotenv()

def print_current_model():
    keys = {key: mask_key(key) for key in ["OPENAI_API_KEY", "GOOGLE_API_KEY", "ANTHROPIC_API_KEY"]}
    pprint(keys)

    model_names = ['gpt-5-nano', 'openai:gpt-5.4', 'claude-sonnet-4-6', 'google_genai:gemini-2.5-flash-lite']
    for model_name in model_names:
        model = init_chat_model(model_name)
        print(f"{type(model).__name__}")





def call_gemini_model():
    from langchain.chat_models import init_chat_model
    chat_model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    response = chat_model.invoke("你是什么模型?请介绍一下你自己")
    print(response.content)
    print('━'*100)
    print(response.model_dump_json(indent=2))

if __name__ == '__main__':
    # print_current_model()
    call_gemini_model()
