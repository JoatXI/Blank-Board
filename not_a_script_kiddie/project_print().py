import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import selenium

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def taking_voice_commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "print" in command: # print() being the name of this AI (Note: should progamme AI with the abililty to change it's name through user command)
                command = command.replace("print", "")
                speak(command)
    except:
        pass
    return command
