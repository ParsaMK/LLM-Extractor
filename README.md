# Project Overview

This project provides a streamlined workflow for extracting and processing text from PDF files and then using it to extract structured information with the help of OpenAI's API. The code is designed to run in a Dockerized environment for consistency and ease of use.

---

## How to Use

1. **Set Up the Docker Environment**
   - Build the Docker container by running:
     ```bash
     docker compose up --build
     ```
   - To access the container's bash, use:
     ```bash
     docker compose exec dev-env bash
     ```

2. **Prepare Your Files**
   - Place your PDF files in a folder named `PDFs` (create the folder in the project directory if it doesn't already exist).

3. **Run the Parser**
   - Execute `parser.py` to process the PDFs.
   - The extracted text will be saved as individual files inside a folder named `processed_texts`.

4. **Extract Information**
   - Open `extractor.py` to select one of the processed text files.
   - Run the script to extract the desired information.

---

## Important Notes

- **OpenAI API Key**
  - To use OpenAI's API, you'll need an API key.
  - It is recommended to create a `.env` file in the project directory and store your API key securely inside it as follows:
    ```env
    OPENAI_API_KEY=your_key_here
    ```

- Make sure you have proper access and permissions for the API key to ensure seamless integration.

---

This setup ensures a clean and efficient way to handle and process financial product documents. Happy coding!




To run the server, run the following code: 
```bash
   streamlit run streamlit.py --server.port=8080
```