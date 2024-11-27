from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

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


# Initialize OpenAI model (or any other model you are using)
llm = OpenAI(api_key="your_openai_api_key")

# Combine the prompt with the model
chain = LLMChain(llm=llm, prompt=prompt)

# Example extracted text (replace with actual text from your PDF)
document_text = "Your extracted document content goes here."

# Get the results from LangChain
result = chain.run({"text": document_text})

# Print the extracted information
print(result)

