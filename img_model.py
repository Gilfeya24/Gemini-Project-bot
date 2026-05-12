
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


os.environ["GOOGLE_API_KEY"] = "AIzaSyDmXE1t0ezu9cR6cMxUEeQC3wLEX5__KdE'"
genai.configure(api_key='AIzaSyDmXE1t0ezu9cR6cMxUEeQC3wLEX5__KdE')

#function
def get_gemini_response(input,image):
    model=genai.GenerativeModel("gemini-2.5-flash")
    if input !="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="GEMINI VISION BOT")
st.header("Gemini application")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("choose an image: ",type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    #main action

submit=st.button("Tell ME About This Image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)  


#AIzaSyD0Z4wq9whkyTeD-mIKAYeiXrRvWZJBh_0