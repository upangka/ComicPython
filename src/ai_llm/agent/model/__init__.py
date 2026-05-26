from langchain.chat_models import init_chat_model

model_deepseek_pro = init_chat_model("deepseek-v4-pro",
                                 temperature=0.8,
                                 extra_body={"thinking": {"type": "disabled"}})


model_deepseek_flash = init_chat_model("deepseek-v4-flash",
                                 temperature=0.8,
                                 extra_body={"thinking": {"type": "disabled"}})
