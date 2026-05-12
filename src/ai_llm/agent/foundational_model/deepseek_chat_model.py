from langchain.chat_models import init_chat_model

model = init_chat_model("deepseek-v4-pro",
                        api_base="https://api.deepseek.com",
                        extra_body={"thinking": {"type": "disabled"}})

from pprint import pprint
pprint(model)
