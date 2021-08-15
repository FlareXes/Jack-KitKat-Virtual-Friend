import shutil

import pyttsx3
import time
import os
import shutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)  # Best voices 3, 5
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

time.sleep(60)
speak("hey welcome welcome Do you know what i mean")