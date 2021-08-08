import pyttsx3
import speech_recognition as sr
from multiprocessing import Process

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecmd():
    r = sr.Recognizer()
    r.energy_threshold = 1000
    with sr.Microphone(sample_rate = 48000, chunk_size = 2048) as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recongnizing...')
        data = r.recognize_google(audio, language='en-in')
        print(data)
    except Exception:
        print('I Didn\'t Got YOU')
        return None
    return data.lower()

if __name__ == '__main__':
    from Accounts.accounts import Account
    login_to = Account('account', 'thisispssword')
    login_to.instagram()