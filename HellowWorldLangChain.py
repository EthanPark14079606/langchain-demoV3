import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

deepseek_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_base = os.getenv("DEEPSEEK_API_BASE")
deepseek_model = os.getenv("DEEPSEEK_MODEL")

llm = ChatOpenAI(
model=deepseek_model,
openai_api_key=deepseek_key,
openai_api_base=deepseek_base
)

result = llm.invoke([
HumanMessage(content="你好，你能介绍一下 DeepSeek 是什么吗？")
])

print(result.content)