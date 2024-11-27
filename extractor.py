from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain

import pprint
import os
import openai

# Get the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    Extract the following details from the document text:
    - ISIN (if present)
    - SRI (Synthetic Risk Indicator)
    - RHP (Recommended Holding Period)
    - PRODUCT NAME
    - ISSUER NAME
    - Target Market
    - Performance scenarios at maturity (Stress, Unfavorable, Moderate, Favorable, expressed as percentages).
    
    Document Text:
    {text}
    """
)

# Initialize the ChatOpenAI model (use ChatOpenAI for GPT-4)
llm = ChatOpenAI(api_key=openai.api_key, model="gpt-4")

# Combine the prompt with the model using LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Read document text from the file
with open("./processed_texts/KID2.txt", "r") as file:
    document_text = file.read()

# Get the results from LangChain using invoke instead of run
result = chain.invoke({"text": document_text})

# Print the extracted information
pprint.pprint(result)