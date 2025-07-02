from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional

load_dotenv()

# Load mistral model from OpenRouter (free tier)
model = ChatOpenAI(model='mistralai/mistral-small-3.2-24b-instruct:free')

# schema 
class Review(TypedDict):  # it does not give runtime validation; it is just a type hint
    # We use Annotated to provide field-level instructions for the model to follow
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]  # this is more complex way of extracting information from given prompt
    name: Annotated[Optional[str], "Write the name of the reviewer"]

# behind the scenes, it generates a system prompt that tells model to output the response in JSON format according to given schema
structured_model = model.with_structured_output(Review)  # for structured output according to given schema

# invoking structured model with a product review — model will extract info based on schema above
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
""")  # invoking structured model

# print the parsed structured result from the model
print(result)
