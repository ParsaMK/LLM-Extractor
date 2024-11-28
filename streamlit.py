import streamlit as st
from PyPDF2 import PdfReader

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
        
        # Display extracted text
        st.subheader("Extracted Text:")
        if extracted_text.strip():
            st.text_area("Text", extracted_text, height=400)
        else:
            st.warning("No text could be extracted. The PDF might contain images instead of text.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")