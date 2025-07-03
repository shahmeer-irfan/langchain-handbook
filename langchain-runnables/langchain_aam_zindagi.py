import random

# --------------- Mock LLM that returns a random response ------------------

class NakliLLM:

  # Constructor method: called when the object is created
  def __init__(self):
    print('LLM created')

  # Simulates an LLM response to a prompt
  def predict(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
    # Returns a dictionary with a random response
    return {'response': random.choice(response_list)}


# --------------- Prompt Template Class ------------------

class NakliPromptTemplate:

  # Initializes with a template string and list of variables
  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  # Fills the template with actual input values
  def format(self, input_dict):
    return self.template.format(**input_dict)


# -------------------- Example: Prompt Generation ---------------------

# Creating a prompt template with placeholders
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

# Using the template to generate a full prompt string
prompt = template.format({'length':'short','topic':'india'})

# Creating an instance of our fake LLM
llm = NakliLLM()

# Getting a prediction using the generated prompt
llm.predict(prompt)


# --------------- Simple LLMChain (like LangChain's LLMChain) ------------------

class NakliLLMChain:

  # Takes a prompt template and an LLM instance during initialization
  def __init__(self, llm, prompt):
    self.llm = llm              # Save the LLM
    self.prompt = prompt        # Save the prompt template

  # Executes the chain: formats prompt and gets a prediction
  def run(self, input_dict):
    final_prompt = self.prompt.format(input_dict)  # Create the final prompt
    result = self.llm.predict(final_prompt)        # Get response from LLM
    return result['response']                      # Return just the text


# -------------------- Using the Chain ---------------------

# Create a new prompt template
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

# Create a new instance of our fake LLM
llm = NakliLLM()

# Create the chain with the template and the LLM
chain = NakliLLMChain(llm, template)

# Run the chain with actual input values
chain.run({'length':'short', 'topic': 'india'})
