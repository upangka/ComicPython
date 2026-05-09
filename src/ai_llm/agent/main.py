import os
from pprint import pprint

from langchain.chat_models import init_chat_model

# from dotenv import load_dotenv
# load_dotenv()

keys = {key: os.getenv(key) for key in ["OPENAI_API_KEY", "GOOGLE_API_KEY", "ANTHROPIC_API_KEY"]}
pprint(keys)

model_names = ['gpt-5-nano', 'openai:gpt-5.4', 'claude-sonnet-4-6', 'google_genai:gemini-2.5-flash-lite']
for model_name in model_names:
    model = init_chat_model(model_name)
    print(f"{type(model).__name__}")
