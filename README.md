# Generative-AI

This repository contains a collection of projects and implementations related to Generative AI, focusing on Retrieval-Augmented Generation (RAG), Langchain agents, and various AI-powered applications. The projects demonstrate the integration of large language models (LLMs) with vector databases, embeddings, and interactive interfaces.

## Technologies Used

The projects in this repository leverage a variety of modern AI and software technologies:

- **Langchain**: Framework for building applications with LLMs
- **Streamlit**: Web app framework for creating interactive interfaces
- **FastAPI**: Modern web framework for building APIs
- **Groq**: High-performance inference platform for LLMs (using LPU for accelerated inference)
- **OpenAI**: Embeddings and GPT models
- **ChromaDB**: Vector database for embeddings
- **FAISS**: Efficient similarity search and clustering
- **ObjectBox**: Lightweight vector database
- **Hugging Face**: Transformers and models
- **LangServe**: Serving Langchain applications
- **LangSmith**: Debugging and monitoring for LLM applications
- **MCP (Model Context Protocol)**: Protocol for connecting AI models to tools

## Projects Overview

| Project | Description | Key Technologies | Purpose |
|---------|-------------|------------------|---------|
| **AgentForge** | Jupyter notebook demonstrating Langchain agents with tools like Wikipedia, Arxiv, and custom retrievers | Langchain, OpenAI, Wikipedia, Arxiv | Showcase agent capabilities for information retrieval and processing |
| **GroqRAG Studio** | Streamlit apps for RAG using Groq models - website content processing and PDF summarization | Groq (LPU), Streamlit, OpenAI embeddings, ChromaDB | Demonstrate RAG with Groq's accelerated inference for real-time applications |
| **LangServe Hub** | FastAPI server and Streamlit client for Langchain-based applications | FastAPI, LangServe, Streamlit, OpenAI | Provide a hub for serving and interacting with Langchain applications |
| **MCP** | Model Context Protocol server for mathematical operations | MCP, FastMCP | Enable AI models to perform mathematical computations via protocol |
| **ObjectBox RAG** | PDF summarization using ObjectBox as vector store | ObjectBox, Streamlit, Groq, OpenAI | Showcase lightweight vector database integration with RAG |
| **QuickBot AI** | AI-powered chatbot application | Streamlit, Langchain, OpenAI | Build interactive conversational AI |
| **RAG Essentials** | Basic RAG implementation with document processing | Langchain, FAISS, Streamlit | Fundamentals of retrieval-augmented generation |
| **RetrievalChains Pro** | Advanced retrieval chains and techniques | Langchain, ChromaDB, FAISS | Explore sophisticated retrieval methods |
| **HugAI Connect** | Hugging Face integrations and models | Hugging Face Transformers, Langchain | Connect and utilize open-source AI models |

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/gaurav-hub/Generative-AI.git
   cd Generative-AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys (OpenAI, Groq, etc.)

4. Navigate to any project folder and follow the README instructions for that specific project.

## Key Features

- **Accelerated Inference**: Utilizes Groq's LPU (Language Processing Unit) for high-speed LLM inference
- **Multiple Vector Stores**: Demonstrates ChromaDB, FAISS, and ObjectBox for different use cases
- **Interactive Interfaces**: Streamlit apps for user-friendly interaction with AI models
- **Modular Architecture**: Each project is self-contained with its own README and setup instructions
- **Production-Ready**: Includes FastAPI servers and proper error handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source. Please check individual project folders for specific licensing information.
