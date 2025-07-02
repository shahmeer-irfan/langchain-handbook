from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()


model = ChatOpenAI() #any model

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

#prompt = template.format() #fills in the variables inside the prompt template with actual values
chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)