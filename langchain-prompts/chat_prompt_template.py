from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'), #sending tuple, drawback of langchain
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

#here we are using dynamic template
#.3 latest langchain version template.
#we use ChatPrompttemplate for multiturn conversations.