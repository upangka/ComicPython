#


```python
from langchain.chat_models import init_chat_model

model = init_chat_model("deepseek-v4-pro",
                        api_base="https://api.deepseek.com",
                        extra_body={"thinking": {"type": "disabled"}})
```


```python
model
```




    ChatDeepSeek(output_version=None, client=<openai.resources.chat.completions.completions.Completions object at 0x000002B191B82C10>, async_client=<openai.resources.chat.completions.completions.AsyncCompletions object at 0x000002B191B83390>, root_client=<openai.OpenAI object at 0x000002B191B820D0>, root_async_client=<openai.AsyncOpenAI object at 0x000002B191B82D50>, model_name='deepseek-v4-pro', model_kwargs={}, openai_api_key=SecretStr('**********'), openai_proxy=None, stream_chunk_timeout=120.0, extra_body={'thinking': {'type': 'disabled'}}, api_key=SecretStr('**********'), api_base='https://api.deepseek.com')


