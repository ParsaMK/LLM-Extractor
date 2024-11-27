import os
import re
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using pdfplumber.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    extracted_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text.append(page.extract_text())
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return "\n".join(extracted_text)

def preprocess_text(raw_text):
    """
    Cleans and preprocesses the extracted text.

    Args:
        raw_text (str): Raw text extracted from the PDF.

    Returns:
        str: Preprocessed text.
    """
    # Remove excessive whitespace
    cleaned_text = re.sub(r'\s+', ' ', raw_text)
    
    # Remove special characters (keep only printable ASCII and essential symbols)
    cleaned_text = re.sub(r'[^\x20-\x7E]', '', cleaned_text)
    
    # Optional: Normalize punctuation
    cleaned_text = cleaned_text.replace('–', '-').replace('•', '-')

    # Optional: Convert to lowercase
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def process_pdf_directory(pdf_dir, output_dir):
    """
    Processes all PDFs in a directory and saves preprocessed text files.

    Args:
        pdf_dir (str): Directory containing PDF files.
        output_dir (str): Directory to save the preprocessed text files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(pdf_dir):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file_name)
            print(f"Processing: {file_name}")

            # Extract and preprocess text
            raw_text = extract_text_from_pdf(pdf_path)
            preprocessed_text = preprocess_text(raw_text)

            # Save to a text file
            output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.txt")
            with open(output_path, "w", encoding="utf-8") as text_file:
                text_file.write(preprocessed_text)
            print(f"Saved processed text to {output_path}")

# Example usage:
if __name__ == "__main__":
    # Define paths
    pdf_directory = "./PDFs"  # Replace with your PDF directory
    output_directory = "./processed_texts"  # Replace with your desired output directory

    # Process all PDFs in the directory
    process_pdf_directory(pdf_directory, output_directory)
