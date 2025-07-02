# Types of messages in langchain
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="meta-llama/llama-3.3-70b-instruct")

messages = [
    SystemMessage(content="You are a helpful AI assistant who delivers concise answer"),
    HumanMessage(content='what is langchain')
]  # message history

result = model.invoke(messages)

# appending AI message to message history
messages.append(AIMessage(content=result.content))

print(messages)

#multi-turn conversation