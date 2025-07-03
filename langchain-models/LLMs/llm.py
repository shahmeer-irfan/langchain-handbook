from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model="gpt-4o-mini")

result= llm.invoke("What is the capital of France?") #lmao cant use it because of api key, but yeah just for demonstration purpose.
print(result)

#no one uses LLMs now, they have become old fashioned. we use ChatModels now.
#here we are using it as chat completion model.