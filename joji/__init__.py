import openai
from dotenv import find_dotenv, load_dotenv
import os
import streamlit as st

load_dotenv(find_dotenv())


@st.cache_resource
def initialize_openai():
    openai.api_key = os.environ["OPENAI_API_KEY"]
