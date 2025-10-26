"""
QuickBot AI Application

This module provides a simple Streamlit-based chatbot using Langchain and OpenAI for responding to user queries.

Functions:
    None (main script)

Usage:
    Run this script with Streamlit to launch the chatbot interface.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to queries."),
        ("user","Question:{question}")
    ]
)

st.title("Namaste, Welcome to LastMinute Help Bot.")
input_text = st.text_input("Search the topic you want!")

#openAI LLM
llm = ChatOpenAI(model = "gpt-4o")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))