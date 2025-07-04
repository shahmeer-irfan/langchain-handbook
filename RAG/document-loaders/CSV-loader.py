from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv') #creates Document object for every row

docs = loader.load()

print(len(docs))
print(docs[1])