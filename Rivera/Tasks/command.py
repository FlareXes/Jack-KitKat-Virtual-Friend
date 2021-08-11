import os
import random
import pyjokes
from Rivera.rvoice import speak
from Rivera.Rchatbot.rchatbot import importcoroutine
from Essentials.DataFilters import takecmd

def joke():
    joke=pyjokes.get_joke(language='en', category= 'all')
    print(joke)
    speak(joke)
    return joke


def UserInputFilter(UserInput, cmdToFilters):
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data


def talk():
    search = importcoroutine()
    search.__next__()
    while True:
        data = takecmd()
        search.send(data)


class Task:
    def music(self, UserInput):
        music_dir = 'E:\CONFIDANCIAL INFORMATION\ABHI SONGS\English Song'
        choreography_dir = 'E:\CONFIDANCIAL INFORMATION\ABHI SONGS\Choreography'
        random_dir = random.choice([music_dir, choreography_dir])

        if 'no specifications' in UserInput:
            songs = random.choice(os.listdir(random_dir))
            os.startfile(os.path.join(random_dir, songs))
            speak("Here we are!")
        else:
            speak('absolutely... but before we go further, any specifications!!!')
            spec = takecmd()
            if 'choreography on' in spec or 'choreography of' in spec or 'choreography by' in spec:
                cmdToFilters = ['choreography on', 'choreography of']
                data = UserInputFilter(spec, cmdToFilters).strip()
                with os.scandir(choreography_dir) as dirs:
                    for entry in dirs:
                        if data in entry.name.lower():
                            os.startfile(os.path.join(choreography_dir, entry.name))
                            speak("Let's enjoy your choice")
                            break
            elif 'choreography' in spec:
                songs = random.choice(os.listdir(choreography_dir))
                os.startfile(os.path.join(choreography_dir, songs))
                speak("did you liked my flavor?")
            elif 'random' in spec:
                songs = random.choice(os.listdir(random_dir))
                os.startfile(os.path.join(random_dir, songs))
                speak("how is that, my specifier")
            elif 'no' in spec:
                songs = random.choice(os.listdir(music_dir))
                os.startfile(os.path.join(music_dir, songs))
                speak("Okay, then here we go!")