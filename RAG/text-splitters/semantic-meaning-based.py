from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation", #meaning on the basis of standard deviation
    breakpoint_threshold_amount=3 #means if specific threshold is more than 3 sd
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)














#consider two paragraphs , first paragraph is tallking about two different things and second paragraph is talking about one thing
#so here normal text-structure based fails because you cznt divide text into jut two paragraphs, it requires three paragraphs.
#here semantic meaning text splitter comes into the game.
#it uses sliding window approach
#divide text into sentences -> generate embedding -> find consine similarity among embeddings-> wherever is most low that means there is topic shift
#new concept right now (it is in experimental stage rn)