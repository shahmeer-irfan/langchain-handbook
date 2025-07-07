from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('example.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, #ovelapping region between two chunks.it helps retain abrupt text chunk(1o to 20 percent is a good number for RAG applications)
    separator=''
)

result = splitter.split_documents(docs) #chunk will also be document

print(result[1].page_content)







#method to divide text into chunks of similar size either on basis of characters or tokens (simplest method)
#it doesnt focus on semantic meaning or grammar or language 