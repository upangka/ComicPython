"""
L03_deepseek_and_gemini_with_langchain.py

This module demonstrates how to use DeepSeek and Gemini chat models through LangChain's unified interface.
It covers initializing multiple model providers using LangChain's init_chat_model function,
enabling seamless switching between different LLM providers while maintaining consistent API patterns.
This approach simplifies integration of multiple language models into Python applications.
"""

from langchain.chat_models import init_chat_model

genai = init_chat_model("google_genai:gemini-2.5-flash", temperature=0.8)

# In extra_body, disable thinking to speed up the response
deepseek = init_chat_model("deepseek:deepseek-v4-pro",
                           temperature=0.8,
                           extra_body={"thinking": {"type": "disabled"}})

response = genai.invoke("What's the capital of Moon?")
print(response.text)
print('━' * 100)
response = genai.invoke("月球的首都是哪里?")
print(response.text)
print('━' * 100)
response = deepseek.invoke("What's the capital of Moon?")
print(response.text)
print('━' * 100)
response = deepseek.invoke("月球的首都是哪里?")
print(response.text)

"""
That's an interesting and imaginative question!

The Moon doesn't have a capital because it's not a country or a political entity. It's a natural satellite of Earth, and it doesn't have a government, cities, or human inhabitants (at least, not permanent ones establishing such things).
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
月球目前没有首都。

原因如下：

1.  **不是国家或政治实体：** 月球是一个天然的卫星，上面没有政府、国家、政治边界或永久居民，因此也没有所谓的“首都”概念。
2.  **国际法规定：** 根据《外层空间条约》等国际法，月球不属于任何一个国家，而是全人类的共同遗产。任何国家都不能通过占领或任何其他方式将其据为己有，自然也无法在上面设立首都。
3.  **无永久定居点：** 尽管人类已多次登陆月球，但目前还没有建立任何永久性的居住基地或城市。

在科幻作品中或未来人类建立永久月球基地后，或许会出现一个行政中心或主要居住区，但目前来说，这只是设想。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
That's a fun question! The Moon doesn't have an official capital because it's not a country and has no permanent government or population. However, if we look at human activity there, the closest thing to a "capital" might be **Tranquility Base**—the site of the first Apollo 11 landing in 1969. It's historically significant as humanity's first footsteps on another world.

In the future, if lunar colonies are established, maybe one day a city like Artemis (NASA's proposed base) will be considered the capital! 🌕
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
月球上并没有国家或城市，因此也没有首都。月球是地球的天然卫星，不属于任何国家。根据《外层空间条约》，月球和其他天体属于全人类，任何国家不得将其据为己有。因此，月球上没有设立首都。
"""