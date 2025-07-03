# Importing the abstract base class (ABC) tools
from abc import ABC, abstractmethod
import random

# -------------- ABSTRACT BASE CLASS (INTERFACE) ------------------

# A base interface for anything that can "run" or "invoke"
class Runnable(ABC):

  # All child classes must implement this method
  @abstractmethod
  def invoke(input_data):
    pass

# -------------- FAKE LLM THAT GENERATES RANDOM RESPONSES ------------------

# A mock Large Language Model (LLM)
class NakliLLM(Runnable):

  def __init__(self):
    print('LLM created')

  # The main method that takes a prompt and returns a fake response
  def invoke(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
    return {'response': random.choice(response_list)}

  # An extra method to show another way of returning a response
  def predict(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
    return {'response': random.choice(response_list)}

# -------------- PROMPT TEMPLATE CLASS ------------------

# This formats input variables into a prompt string
class NakliPromptTemplate(Runnable):

  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  # Converts input data into a formatted prompt using the template
  def invoke(self, input_dict):
    return self.template.format(**input_dict)

  # A helper method (same as invoke) that formats the prompt
  def format(self, input_dict):
    return self.template.format(**input_dict)

# -------------- OUTPUT PARSER CLASS ------------------

# This extracts the string response from the LLM's output dictionary
class NakliStrOutputParser(Runnable):

  def __init__(self):
    pass

  def invoke(self, input_data):
    return input_data['response']

# -------------- CONNECTOR THAT CHAINS RUNNABLES TOGETHER ------------------

# This class chains multiple Runnable objects together like a pipeline
class RunnableConnector(Runnable):

  def __init__(self, runnable_list):
    self.runnable_list = runnable_list

  def invoke(self, input_data):
    # Pass input through each runnable in sequence
    for runnable in self.runnable_list:
      input_data = runnable.invoke(input_data)
    return input_data

# ------------------- CHAIN EXAMPLE 1 -----------------------

# Create a prompt template
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

# Create the fake LLM
llm = NakliLLM()

# Create the parser to get the final string output
parser = NakliStrOutputParser()

# Chain: Template → LLM → Output Parser
chain = RunnableConnector([template, llm, parser])

# Run the chain with input variables
chain.invoke({'length':'long', 'topic':'india'})


# ------------------- CHAIN EXAMPLE 2: Nested Chains -----------------------

# First prompt template for generating a joke
template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# Second prompt template for explaining the joke using previous response
template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

# New instance of the fake LLM
llm = NakliLLM()

# Create the parser again
parser = NakliStrOutputParser()

# First chain: Template → LLM
chain1 = RunnableConnector([template1, llm])

# Second chain: Template → LLM → Parser
chain2 = RunnableConnector([template2, llm, parser])

# Final chain: Output from chain1 flows into chain2
final_chain = RunnableConnector([chain1, chain2])

# Run the full nested chain
final_chain.invoke({'topic':'cricket'})
