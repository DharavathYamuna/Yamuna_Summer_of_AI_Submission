
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Yamuna's Chatbot", layout="centered")

st.title("🤖 Hugging Face Chatbot")
st.markdown("This chatbot is powered by GPT-2 from Hugging Face Transformers!")

# Load model
chatbot = pipeline("text-generation", model="gpt2")

# Input
user_input = st.text_input("You:", "")

# Response
if user_input:
    with st.spinner("Chatbot is typing..."):
        result = chatbot(user_input, max_length=100, num_return_sequences=1)
        response = result[0]['generated_text']
        st.success(response)
