# RetrievalChains Pro

This folder contains a Jupyter notebook on Langchain chains, particularly retrieval chains, along with sample data files.

## Files

- `retrievers.ipynb`: A notebook demonstrating data ingestion from text, web, and PDF sources; text splitting; vector embeddings using OpenAI; vector stores like Chroma and FAISS; and building retrieval chains for question-answering based on documents.
- `attention.pdf`: A PDF document, likely the "Attention is All You Need" paper, used in the notebook for demonstration.
- `speech.txt`: A text file containing a speech, used for data ingestion examples.

## How to Run

1. Ensure you have Jupyter Notebook installed: `pip install jupyter`.
2. Install required dependencies: `pip install langchain langchain-community beautifulsoup4 requests pypdf chromadb faiss-cpu`.
3. Set up your OpenAI API key in a `.env` file.
4. Navigate to the `RetrievalChains Pro` directory.
5. Run the notebook: `jupyter notebook retrievers.ipynb`.
6. Execute the cells in order to perform data ingestion, text splitting, vector embedding, and retrieval chain setup.
