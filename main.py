import speech_recognition as sr
import pyttsx3
import json
from googletrans import Translator

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""

def load_qa_data(filepath="qa_data.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def translate_to_english(text):
    return Translator().translate(text, dest='en').text

def process_query(query, qa_data):
    for keyword in qa_data:
        if keyword in query:
            return qa_data[keyword]
    return "Sorry, I didn’t understand that. Let me forward you to a human advisor."

def main():
    qa_data = load_qa_data()
    speak("Hello! How can I help you today?")
    while True:
        query = listen()
        if not query:
            continue
        query = translate_to_english(query)
        response = process_query(query, qa_data)
        speak(response)
        if "goodbye" in response.lower():
            break

if __name__ == "__main__":
    main()
