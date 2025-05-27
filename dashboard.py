# dashboard.py
import streamlit as st
from main import process_query

st.title("🎓 Academic Advisor Voice Bot")

user_input = st.text_input("Ask a question about your schedule, exams, or meetings:")

language = st.selectbox("Language", ["en", "ar", "hi"])

if st.button("Submit"):
    response = process_query(user_input, language=language)
    st.write("🤖 Response:", response)
