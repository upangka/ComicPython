

from typing import Optional

from google import genai
client = genai.Client()

# MODEL_NAME = "gemini-3.5-flash"
# MODEL_NAME = "gemini-2.5-flash"


def ask_for_model_name(retries=3, model_version: Optional[int] = None):
    """Ask for model name."""

    if model_version:
        return f"gemini-{model_version}.5-flash"

    print("请选择模型：")
    print("2. gemini-2.5-flash")
    print("3. gemini-3.5-flash")

    while True:
        reply = input("请输入数字选择模型：")
        if reply in ['2', '3']:
            model_name = f"gemini-{reply}.5-flash"
            print(f"你选择了模型：{model_name}")
            return model_name

        retries -= 1
        if retries < 0:
            raise ValueError("多次无效输入，程序终止。")

        print("无效的选择，请输入数字2或3。")


model_name = ask_for_model_name(model_version=3)
response = client.models.generate_content(
    model=model_name,
    contents="你叫什么名字"
)

print(response.text)
