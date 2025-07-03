<h1>📦 Structured Output Examples with LangChain using Pydantic, TypeDdict, JSON schema</h1>

<p>This repository contains examples demonstrating how to use <strong>LangChain</strong> and <strong>Pydantic</strong> for structured output parsing. It includes real-world scenarios for extracting data from unstructured text using well-defined schemas.</p>

<hr>

<h2>🚀 What This Project Demonstrates</h2>
<ul>
  <li>Using <code>LangChain</code>’s <code>with_structured_output()</code> for type-safe JSON outputs</li>
  <li>Defining data schemas using <code>Pydantic</code> and <code>TypedDict</code></li>
  <li>Explaining and comparing <code>Annotated</code> vs <code>Field()</code> in schema definitions</li>
  <li>Handling optional fields and default values</li>
  <li>Parsing sentiment, pros & cons, and key themes from reviews</li>
  <li>Generating and using JSON Schema for validation and LLM prompting</li>
</ul>

<hr>

<h2>🧠 What I Learned / Implemented</h2>
<ul>
  <li>How to extract structured JSON from natural language using LangChain</li>
  <li>The difference between <code>TypedDict</code> and <code>Pydantic</code> models</li>
  <li>When and how to use <code>Annotated</code> and <code>Field()</code> with descriptions</li>
  <li>How to use <code>Optional</code> fields and <code>Literal</code> types in schemas</li>
  <li>How LangChain uses schema to guide LLMs internally (via system prompts)</li>
  <li>Basics of JSON Schema and how it integrates with FastAPI or OpenAI Function Calling</li>
</ul>

<hr>

<h2>📦 Technologies Used</h2>
<ul>
  <li><strong>Python</strong></li>
  <li><strong>LangChain</strong></li>
  <li><strong>Pydantic</strong></li>
  <li><strong>OpenAI / Mistral LLMs</strong></li>
</ul>

<hr>

<h2>📑 Example Use Case</h2>
<p>Given a natural language product review, extract the following in JSON format:</p>
<ul>
  <li><code>summary</code>: A brief summary</li>
  <li><code>sentiment</code>: Either <code>pos</code> or <code>neg</code></li>
  <li><code>key_themes</code>: List of key ideas mentioned</li>
  <li><code>pros</code> and <code>cons</code>: Optional lists</li>
  <li><code>name</code>: Optional reviewer name</li>
</ul>

<hr>

<h2>🛠️ How to Run</h2>
<ol>
  <li>Install dependencies:
    <pre><code>pip install langchain-openai pydantic python-dotenv</code></pre>
  </li>
  <li>Create a <code>.env</code> file with your OpenAI or Mistral API key</li>
  <li>Run any example script:
    <pre><code>python example_script.py</code></pre>
  </li>
</ol>

<hr>

<h2>🧾 License</h2>
<p>This project is for learning purposes only. You are free to fork, learn, and build on top of it.</p>
