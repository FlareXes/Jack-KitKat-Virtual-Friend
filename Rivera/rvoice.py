import pyttsx3
import speech_recognition as sr
from multiprocessing import Process

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)       # Best voices 3, 6, 2  MArkm
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak('Hey What\'s Up Everybody, Rivera in the house... Oh WOW!!! Now We Don\'t Need You Jack')