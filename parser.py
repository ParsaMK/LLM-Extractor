import re
import pdfplumber
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def extract_text_and_tables(pdf_path):
    """
    Extracts text and tabular data from a PDF file using pdfplumber.

    Parameters:
    pdf_path (str): The path to the PDF file.

    Returns:
    dict: A dictionary containing extracted text and tables.
    """
    extracted_data = {"text": [], "tables": []}

    try:
        # Open the PDF file with pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                # Extract text
                text = page.extract_text()
                if text:
                    extracted_data["text"].append({"page": page_number, "content": text})

                # Extract tables
                tables = page.extract_tables()
                for table in tables:
                    extracted_data["tables"].append({"page": page_number, "content": table})

        return extracted_data

    except Exception as e:
        print(f"Error occurred while processing the PDF: {e}")
        return extracted_data

# Preprocessing function for text
def preprocess_text(text):
    """
    Preprocess the extracted text by cleaning and tokenizing it.

    Args:
        text (str): The raw text to be preprocessed.

    Returns:
        str: The cleaned and tokenized text.
    """
    # # # Convert to lowercase
    # text = text.lower()

    # # Remove non-alphabetic characters (optional)
    # text = re.sub(r'[^a-z\s]', '', text)

    # # Tokenize the text
    # tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization (optional)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into a string
    cleaned_text = ' '.join(tokens)
    return cleaned_text

# Preprocessing function for tables
def preprocess_table(table):
    """
    Preprocess the extracted table into a readable text format.

    Args:
        table (list): The raw table data, as a list of lists (rows).

    Returns:
        str: The table data in a structured, readable format.
    """
    # Convert each row into a string and join the columns with '|'
    #table_str = "\n".join([" | ".join(row) for row in table])
    # Replace None with an empty string and join columns with '|'
    table_str = "\n".join([" | ".join(cell if cell is not None else "" for cell in row) for row in table])
    return table_str

# Extract text and tables from the PDF file
def extract_text_and_tables(pdf_path):
    """
    Extracts text and tables from the PDF file using pdfplumber.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: A dictionary containing extracted text and tables.
    """
    extracted_data = {"text": [], "tables": []}
    #try:
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            # Extract text
            text = page.extract_text()
            if text:
                # Preprocess and append the text
                #cleaned_text = preprocess_text(text)
                cleaned_text = text
                extracted_data["text"].append({"page": page_number, "content": cleaned_text})
            # Extract tables
            tables = page.extract_tables()
            for table in tables:
                # Preprocess and append the table
                cleaned_table = preprocess_table(table)
                extracted_data["tables"].append({"page": page_number, "content": cleaned_table})

    return extracted_data

    # except Exception as e:
    #     print(f"Error occurred while processing the PDF: {e}")
    #     return extracted_data

# Format the extracted data for ChatGPT input
def format_for_chatgpt(data):
    """
    Formats the extracted text and tables into a prompt suitable for ChatGPT.

    Args:
        data (dict): Extracted data containing text and tables.

    Returns:
        str: The formatted input prompt for ChatGPT.
    """
    prompt = "Ecco il testo estratto e i dati della tabella:\n\n"

    # Add the text content to the prompt
    for text_item in data["text"]:
        prompt += f"--- Page {text_item['page']} Text ---\n"
        prompt += text_item["content"] + "\n\n"

    # Add the table content to the prompt
    for table_item in data["tables"]:
        prompt += f"--- Page {table_item['page']} Table ---\n"
        prompt += table_item["content"] + "\n\n"

    return prompt
