import os
from langchain import HuggingFaceHub
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load the environmental variables
load_dotenv()

# Hugging Face API token
hf_apitoken = os.getenv("HUGGINGFACEAPI")

# Initialize the HuggingFaceHub model
hub_llm = HuggingFaceHub(
    repo_id ='facebook/blenderbot-400M-distill', 
    huggingfacehub_api_token = hf_apitoken,
    model_kwargs = {'temperature': 0.7, 'max_length': 100}
)

# Define a prompt template (customize it as needed)
prompt_template = PromptTemplate(
    input_variables = ["input_text"],
    template = "{input_text}"
)

# Example input text
input_text = "Are you a human ?"

# Generate the prompt
prompt = prompt_template.format(input_text=input_text)

# Get the model's response
response = hub_llm(prompt)

# Main Function to Generate Version 
def chatbot(input_text):
    try:
        prompt = prompt_template.format(input_text=input_text)
        response = hub_llm(prompt)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, something went wrong. Please try again."

