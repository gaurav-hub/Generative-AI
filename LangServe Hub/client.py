"""
LangServe Hub Client

This module provides a Streamlit client to interact with the LangServe Hub FastAPI server for generating essays.

Functions:
    get_openai_response(input_text: str) -> str: Sends a request to the server to generate an essay on the given topic and returns the response.

Usage:
    Run this script with Streamlit to launch the client interface.
"""

import requests
import streamlit as st


def get_openai_response(input_text):
    """
    Sends a POST request to the LangServe Hub server to generate an essay on the specified topic.

    Args:
        input_text (str): The topic for the essay.

    Returns:
        str: The generated essay content or an error message.
    """
    # Properly send the JSON payload
    payload = {'input': {'topic': input_text}}

    response = requests.post("http://localhost:8000/essay/invoke", json=payload)
    print(response)

    if response.status_code == 200:
        return response.json()['output']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"



st.title("Demo")
input_text = st.text_input("Write an essay on")

if input_text:
    st.write(get_openai_response(input_text))
