"""
LangServe Hub Application

This module provides a FastAPI server for Langchain-based applications, including direct OpenAI chat model interface and a templated essay generator.

Functions:
    None (main script)

Usage:
    Run this script to start the FastAPI server on localhost:8000.
"""

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

# Set the key (optional if you pass it directly to ChatOpenAI)
os.environ["OPENAI_API_KEY"] = openai_api_key

# Create FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple Server"
)

# Add /openai route - direct chat model interface
add_routes(
    app,
    ChatOpenAI(openai_api_key=openai_api_key),
    path="/openai"
)

# Define the model and prompt template
model = ChatOpenAI(openai_api_key=openai_api_key)
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

# Add /essay route - templated essay generator
add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
