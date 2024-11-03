
# Simple LLM using Gemini; just in one line (line #10), we have created a LLM model.

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-pro")

st.title("Simple LLM using Gemini Pro")
user_input = st.text_input("Enter your question")

if st.button("Submit"):
    st.write(llm.invoke(user_input))