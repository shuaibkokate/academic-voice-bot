# Placeholder for Streamlit dashboard showing query analytics
import streamlit as st
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

st.title("🎓 Academic Advisor Voice Bot")

if st.button("🎤 Start Voice Chat"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            st.success(f"You said: {query}")
            # Placeholder: you can call your advisor function here
            response = f"You asked about: {query}"
            st.write("Bot:", response)
            speak(response)
        except:
            st.error("Sorry, I could not understand.")
