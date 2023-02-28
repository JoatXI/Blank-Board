import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()