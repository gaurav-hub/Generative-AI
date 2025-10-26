# GroqRAG Studio

This folder contains Streamlit applications for Retrieval-Augmented Generation (RAG) using Groq models and OpenAI embeddings.

## Files

- `app.py`: A Streamlit app that allows users to input a website URL, loads and processes the content, creates vector embeddings, and provides a RAG interface for querying the website content using Groq's Llama model.
- `llama3.py`: A Streamlit app for PDF summarization. It loads PDFs from the `us_census` directory, creates embeddings, and allows users to ask questions about the documents using Groq's Llama-3.3-70b-versatile model.
- `us_census/`: A subdirectory containing PDF files related to US Census data, used in the PDF summarizer app.

## How to Run

### Website RAG App (app.py)
1. Install dependencies: `pip install -r requirements.txt`.
2. Set up your Groq API key in a `.env` file.
3. Run the Streamlit app: `streamlit run app.py`.
4. Enter a website URL in the input field and wait for processing.
5. Ask questions about the website content in the prompt input.

### PDF Summarizer App (llama3.py)
1. Ensure PDFs are present in the `us_census` subdirectory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up your Groq API key and OpenAI API key in a `.env` file.
4. Run the Streamlit app: `streamlit run llama3.py`.
5. Click "Document Embedding" to process the PDFs.
6. Enter questions about the documents in the input field.
