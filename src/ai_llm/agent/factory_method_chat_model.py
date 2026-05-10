from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

def print_current_model():
    model_names = ['gpt-5-nano',
                   'openai:gpt-5.4',
                   'claude-sonnet-4-6',
                   'google_genai:gemini-2.5-flash-lite']
    for model_name in model_names:
        model = init_chat_model(model_name)
        print(f"'{model_name}' -> {type(model).__name__}(实例) {model._llm_type}")

if __name__ == '__main__':
    print_current_model()