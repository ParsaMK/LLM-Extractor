from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain
import os
import openai

def extract_kid_info(text: str):
    # Get the OpenAI API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    with open('./KID1_text_and_tables/KID1.txt', 'r', encoding='utf-8') as file:
        example = file.read()

    # Define your prompt template
    prompt = PromptTemplate(
        input_variables=["text", "example"],
        template="""
    Informazioni oggetto dell'estrazione:
        1.	Campi puntuali:
        o	ISIN (se e dove presente)
        o	SRI - indicatore sintetico di riscbìhio (va da 1 a 7)
        o	RHP - orizzonte di detenzione raccomandato
        o	NOME DEL PRODOTTO
        o	NOME DELL'EMITTENTE
        2.	Campi testuali:
        o	Target market
        3.	Campi tabellari (Hint: sarebbe opportuno, prima di interrogare un LLM, estrarre la tabella in maniera strutturata):\n
        {example}
        Document Text:
        {text}
        """
    )

    # Initialize the ChatOpenAI model (use ChatOpenAI for GPT-4)
    llm = ChatOpenAI(api_key=openai.api_key, model="gpt-4")

    # Combine the prompt with the model using LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Get the results from LangChain using invoke instead of run
    result = chain.invoke({"text": text, "example": example})

    # Print the extracted information
    return result