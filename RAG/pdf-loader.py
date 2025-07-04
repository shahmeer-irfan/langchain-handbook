from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf') #only works on textual pdf files

docs = loader.load() #if pdf has 25 pages that means it will make 25 document objects

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)

#more pdf loaders 
#pdf with columns/tables -> PDFplubeLoader
#Scanned/images PDFs -> UnstructuredPDFLoader or AmazonTextractPDFLoader
#Need layout and image data -> PyMuPDF Loader
#Want best structure extraction -> UnstructuredPDF Loader
