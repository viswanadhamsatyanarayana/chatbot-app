import streamlit as st
from transformers import pipeline

# Load chatbot model
generator = pipeline("text-generation", model="distilgpt2")

st.set_page_config(page_title="Simple Chatbot", layout="centered")
st.title("🤖 Chatbot App")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = generator(user_input, max_length=50, do_sample=True)[0]['generated_text']
        st.text_area("Bot:", value=response, height=200)
    else:
        st.warning("Please type something to chat.")
