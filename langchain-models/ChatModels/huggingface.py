from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
chat = ChatHuggingFace(llm=llm)
result = chat.invoke('what is game')
print(result.content)

#can also run model locally, but hardware heavy