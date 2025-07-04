from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf', #specify file types
    loader_cls=PyPDFLoader #directory of PDFs
)

docs = loader.lazy_load() #it loads on demand (best when dealing with large documents or lots of files ) - returns generator of document objects
#.load() loads everything at once
for document in docs:
    print(document.metadata)