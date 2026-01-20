from langchain_openai import ChatOpenAI

client = ChatOpenAI(
    model = "gpt-4o-mini",
    base_url = "https://openrouter.ai/api/v1",
    temperature=0
)