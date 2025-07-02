from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate five interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model='meta-llama/llama-3.3-70b-instruct')

parser = StrOutputParser() 

chain = prompt | model | parser 

result = chain.invoke({'topic':'cricket'})
# print(result) 
chain.get_graph().print_ascii() #chain visualizer