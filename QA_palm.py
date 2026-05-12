from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


os.environ["GOOGLE_API_KEY"] = "google_api_key"
genai.configure(api_key='google_api_key')

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="CHATBOT DEMO")  
st.header("LLLM APPLICATION")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question") 
if submit and input:
    response=get_gemini_response(input)
    st.session_state["chat_history"].append(("you", input))
    st.subheader("THe Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("bot", chunk.text))
    
st.subheader("the chat history is")
for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")

