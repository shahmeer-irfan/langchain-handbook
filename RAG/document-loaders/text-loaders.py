from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI() #use any model

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('RAG\\notes.txt',encoding='utf-8')

docs= loader.load() #it loads .txt file as a document object.

print(docs) 

# print(type(docs)) list of document objects

#print(len(docs)) length 1 means 1 document

#print(docs[0]) prints content of document

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))