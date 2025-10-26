# ObjectBox RAG

This folder contains a Streamlit application for PDF summarization using ObjectBox as the vector store.

## Files

- `app.py`: A Streamlit app that loads PDFs from the `us_census` directory, creates vector embeddings using OpenAI, stores them in ObjectBox, and provides a RAG interface for querying the documents using Groq's Llama model.
- `us_census/`: A subdirectory containing PDF files related to US Census data, used for summarization.

## How to Run

1. Ensure PDFs are present in the `us_census` subdirectory.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up your Groq API key and OpenAI API key in a `.env` file.
4. Run the Streamlit app: `streamlit run app.py`.
5. Click "Document Embedding" to process the PDFs and create the vector store.
6. Enter questions about the documents in the input field to get summarized answers.
