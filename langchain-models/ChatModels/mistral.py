from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load variables from .env
load_dotenv()

# Create chat model using OpenRouter
model = ChatOpenAI(model="mistralai/mistral-7b-instruct" , temperature=0.5, max_completion_tokens=40) # or other open source OpenRouter model

result =  model.invoke("What is the capital of France?")
print(result.content)

#temperature is a parameter that controls the randomness of the model.
#0.0 is the most deterministic, 1.0 is the most random.

#max_completion_tokens is used for paid models to limit number of tokens per dollars.
