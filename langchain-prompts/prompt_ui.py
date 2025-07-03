from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize the model (you must have OpenAI key set in your .env)
model = ChatOpenAI(model='meta-llama/llama-3.3-70b-instruct')

# Streamlit UI
st.set_page_config(page_title="AI Chat App")
st.header("AI Chat App")

paper_input = st.selectbox(
    "Select Research Paper Name", 
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


template = load_prompt('template.json') #laods template from json file


# Button trigger
if st.button("Search"):
    with st.spinner("Thinking..."):
        chain = template | model #making chain, first it will invoke template then it will invoke model
        result = chain.invoke({
            'paper_input':paper_input,
            'style_input':style_input,
            'length_input':length_input
        })
        st.write(result.content)
