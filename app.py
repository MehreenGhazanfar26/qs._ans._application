from dotenv import load_dotenv  # Corrected spelling of 'load_dotevn'
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure the API key using environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initializing our Streamlit app
st.set_page_config(page_title="Question Answering App", page_icon="🧠")

st.header("Gemini LLM Application by Mehreen")

# Text input for the questions
input = st.text_input("Input your question:", key="input")

# Button to submit the question
submit = st.button("Ask the Question")

# When submit is called
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
