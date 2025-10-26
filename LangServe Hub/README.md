# LangServe Hub

This folder contains a FastAPI server and a Streamlit client for Langchain-based applications.

## Files

- `app.py`: A FastAPI application that serves Langchain routes, including direct OpenAI chat model interface and a templated essay generator. It uses Langserve to add routes and runs on localhost:8000.
- `client.py`: A Streamlit application that acts as a client to interact with the FastAPI server, allowing users to input topics and receive generated essays.

## How to Run

### Server (app.py)
1. Install dependencies: `pip install -r requirements.txt`.
2. Set up your OpenAI API key in a `.env` file.
3. Run the FastAPI server: `python app.py` or `uvicorn app:app --host localhost --port 8000`.
4. Access the API documentation at `http://localhost:8000/docs`.

### Client (client.py)
1. Ensure the server is running.
2. Run the Streamlit client: `streamlit run client.py`.
3. Open the provided URL in your browser to interact with the essay generator.
