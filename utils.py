import streamlit as st
import os
import google.generativeai as genai
from config import Config

def apply_css(dark_mode):
    css = Config.DARK_MODE_CSS if dark_mode else Config.LIGHT_MODE_CSS
    st.markdown(css, unsafe_allow_html=True)

def initialize_session():
    if 'dark_mode' not in st.session_state:
        st.session_state['dark_mode'] = False

def get_model_name(model_choice):
    if model_choice == "Gemini 1.5 Flash":
        return "gemini-1.5-flash-latest"
    elif model_choice == "Gemini 1.5 Pro":
        return "gemini-1.5-pro-latest"
    else:
        return "gemini-1.0-pro"

def create_chat_session(api_key, model_name, temperature, top_p, top_k, max_output_tokens):
    os.environ["GEMINI_API_KEY"] = api_key
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        safety_settings=Config.SAFETY_SETTINGS,
        generation_config=generation_config,
    )

    return model.start_chat(history=[])
