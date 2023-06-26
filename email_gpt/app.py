import os
import openai
import streamlit as st

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

def main():
    st.title("Email GPT Creator")
    name = st.text_input("Enter your name:")
    topic = st.text_input("Enter topic (leave, wfh, etc):")
    reasons = st.text_input("State some reasons (sickness, personal work, etc):")
    recipeints = st.text_input("Who is the email for?:")
    
if __name__ == "__main__":  
    main()