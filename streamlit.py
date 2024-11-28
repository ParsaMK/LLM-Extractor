import streamlit as st
from PyPDF2 import PdfReader
import pdfplumber
from parser import preprocess_text
from extractor import extract_kid_info

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain

import pprint
import os
import openai


import sys
print(sys.executable)



# Page title
st.title("PDF Text Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Display uploaded file details
    st.write("**File Uploaded:**", uploaded_file.name)
    
    # Extract text from the PDF
    try:
        pdf_reader = PdfReader(uploaded_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()
        
        # with pdfplumber.open(pdf_path) as pdf:
        #     for page in pdf.pages:
        #         extracted_text.append(page.extract_text())
        #     extracted_text = "\n".join(extracted_text)
        # Display extracted text
        st.subheader("Extracted Text:")
        if extracted_text.strip():
            extracted_text = preprocess_text(extracted_text)
            extracted_kid = extract_kid_info(extracted_text)
            st.text_area("Text", str(extracted_kid), height=400)
        else:
            st.warning("No text could be extracted. The PDF might contain images instead of text.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")