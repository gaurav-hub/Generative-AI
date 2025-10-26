# QuickBot AI

This folder contains a simple Streamlit-based chatbot application using Langchain and OpenAI.

## Files

- `app.py`: A Streamlit application that provides a chatbot interface. It uses Langchain's ChatOpenAI model with a prompt template to respond to user queries. The app is titled "Namaste, Welcome to LastMinute Help Bot."

## How to Run

1. Install dependencies: `pip install -r requirements.txt`.
2. Set up your OpenAI API key and Langchain API key in a `.env` file.
3. Enable Langchain tracing by setting `LANGCHAIN_TRACING_V2=true` in your environment.
4. Run the Streamlit app: `streamlit run app.py`.
5. Open the provided URL in your browser to interact with the chatbot.
