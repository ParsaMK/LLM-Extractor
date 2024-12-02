import streamlit as st
from parser import extract_text_and_tables, format_for_chatgpt
from extractor import extract_kid_info
import io
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Use ChatOpenAI for chat models like GPT-4
from langchain.chains import LLMChain

# Page title
st.title("PDF Text Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Display uploaded file details
    st.write("**File Uploaded:**", uploaded_file.name)

    # Convert the uploaded file to a byte stream
    pdf_bytes = uploaded_file.read()
    pdf_stream = io.BytesIO(pdf_bytes)  # Create an in-memory binary stream

    # Extract text from the PDF
    try:
        extracted_data = extract_text_and_tables(pdf_stream)
        extracted_text = extracted_data["text"]
        extracted_tables = extracted_data["tables"]
        input = format_for_chatgpt(extracted_data)
        output = extract_kid_info(input)

        st.subheader("Extracted Text:")
        #############################################
        # if extracted_text.strip():
        #############################################
        st.text_area("Text", output["text"], height=400)
        # else:
        #     st.warning("No text could be extracted. The PDF might contain images instead of text.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")