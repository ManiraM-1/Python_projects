import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os

# Ignore warnings for cleaner output
warnings.filterwarnings("ignore")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to the second available one (commonly female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Fixed property name from 'voices' to 'voice'

def talk(audio):
    """Converts text to speech using pyttsx3."""
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    """Records audio and converts it to text using Google Speech Recognition."""
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)  # Listen to the microphone input

    data = ""
    try:
        data = recog.recognize_google(audio)  # Recognize speech using Google
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition: " + str(ex))  # Fixed error formatting

    return data

def response(text):
    """Converts text to speech using Google Text-to-Speech (gTTS) and plays it."""
    print(text)

    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)  # Play the generated audio

    os.remove(audio)  # Remove the audio file after playing

def call(text):
    """Checks if the wake word 'Mini' is in the spoken text."""
    action_call = "mini"  # Set wake word to lowercase for consistency

    text = text.lower()  # Convert spoken text to lowercase
    if action_call in text:
        print("Assistant activated!")  # Placeholder for further actions

# Example usage:
# talk("Hello! How can I assist you?")
# user_input = rec_audio()
# call(user_input)
