
import streamlit as st
import os
import openai
from langchain.llms import OpenAI

from dotenv import load_dotenv, find_dotenv

# Load environment variables from a .env file
_ = load_dotenv(find_dotenv())

# Set the OpenAI API key from the environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

#Function to return the response
def load_answer(question):
    llm = OpenAI(model_name="text-davinci-003",temperature=0)
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

