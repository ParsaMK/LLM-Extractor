from parser import extract_text_and_tables, format_for_chatgpt

extracted_data = extract_text_and_tables('./PDFs/KID2.pdf')
text = format_for_chatgpt(extracted_data)

###########################################################################
###########################################################################
###########################################################################
import openai
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI model (use ChatOpenAI for GPT-4)
llm = ChatOpenAI(api_key=openai.api_key, model="gpt-4")

# Define the summarization prompt template
summarization_prompt = PromptTemplate(
    input_variables=["text"],
    template="Please summarize the following text:\n\n{text}"
)

# Define the main processing prompt template
main_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Informazioni oggetto dell'estrazione:
    1. Campi puntuali:
    o ISIN (se e dove presente)
    o SRI - indicatore sintetico di rischio (va da 1 a 7)
    o RHP - orizzonte di detenzione raccomandato
    o NOME DEL PRODOTTO
    o NOME DELL'EMITTENTE
    2. Campi testuali:
    o Target market
    3. Campi tabellari (Hint: sarebbe opportuno, prima di interrogare un LLM, estrarre la tabella in maniera strutturata):\n
scrivere un riassunto completo del testo che includa le informazioni richieste (voglio misurazioni e fattori di rischio):
{text}
"""
)

# Create the chain for summarizing text
summarization_chain = LLMChain(llm=llm, prompt=summarization_prompt)

# Create the chain for processing the summarized text
main_chain = LLMChain(llm=llm, prompt=main_prompt)

# Function to summarize text and then process it
def process_text(text):
    # Step 1: Summarize the long text
    summary = summarization_chain.invoke({"text": text})

    # Step 2: Use the summarized text in the main prompt
    result = main_chain.invoke({"text": summary})

    return result

result = process_text(text)

###########################################################################
###########################################################################
###########################################################################

text = f"""
esempio di input e output atteso:
input:
{result["text"]}
output:
-	ISIN: LU0690021539
-	SRI: 2
-	RHP: 5
-	NOME DEL PRODOTTO: Unit Personal Private
-	NOME DELL'EMITTENTE: Fineco Asset Management
-	TARGET MARKET: il Fondo Esterno è rivolto ai clienti aventi una buona conoscenza e/o esperienza dei mercati finanziari e assicurativi e una bassa tolleranza al rischio finanziario, i quali intendono investire il proprio capitale nel medio periodo accettando i possibili rischi di perdita connessi all'investimento finanziario.
-	SCENARI DI PERFORMANCE A RHP:
o	stress -5.82%, 
o	sfavorevole -2.73%, 
o	moderato 0.13%. 
o	favorevole 0.99%
"""

with open('./KID1_text_and_tables/KID1.txt', "w") as file:
    file.write(text)