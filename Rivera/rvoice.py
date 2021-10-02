import pyttsx3
from gtts import gTTS
import playsound
from os import name

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)       # Best voices 3, 6, 2  MArkm
engine.setProperty('rate', 170)


def speak(audio):
    if name == 'nt':
        engine.say(audio)
        engine.runAndWait()
    else:
        tts = gTTS(text=text, lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)

# speak('Hey What\'s Up Everybody, Rivera in the house... Oh WOW!!! Now We Don\'t Need You Jack')