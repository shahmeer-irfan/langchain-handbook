from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="meta-llama/llama-3.3-70b-instruct")

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print("Exiting chat...")
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

# Optional: view chat history
# print(chat_history)
