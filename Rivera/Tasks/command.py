import os
import random
import pyjokes
from Essentials.priv_esc import request_to_priv_esc_, danger_alert
from Rivera.rvoice import speak
from Essentials.DataFilters import takecmd


def UserInputFilter(UserInput, cmdToFilters):
    datalendict = {}
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            newdict = {data: len(data)}
            datalendict.update(newdict)
    try:
        data = min(datalendict, key=datalendict.get)
    except ValueError as e:
        data = UserInput

    if data == '':
        data = UserInput
    return data.strip()


class Task:
    def music(self, UserInput):
        music_dir = 'E:\\CONFIDANCIAL INFORMATION\\ABHI SONGS\\English Song'
        choreography_dir = 'E:\\CONFIDANCIAL INFORMATION\\ABHI SONGS\\Choreography'
        random_dir = random.choice([music_dir, choreography_dir])

        if 'no specification' in UserInput or 'without specification' in UserInput:
            songs = random.choice(os.listdir(random_dir))
            os.startfile(os.path.join(random_dir, songs))
            speak("Here we are!")
        else:
            empz1 = 'absolutely... but before we go further, any specifications!!!'
            empz2 = 'Okay would you like me to play anything special?'
            speakEmpz = random.choice([empz1, empz2])
            speak(speakEmpz)
            spec = takecmd()
            if 'choreography on' in spec or 'choreography of' in spec or 'choreography by' in spec:
                cmdToFilters = ['choreography on', 'choreography of', 'yeah']
                data = UserInputFilter(spec, cmdToFilters).strip()
                print(data)
                with os.scandir(choreography_dir) as dirs:
                    for entry in dirs:
                        if data in entry.name.lower():
                            os.startfile(os.path.join(choreography_dir, entry.name))
                            speak("Let's enjoy your choice")
                            break
            elif 'favourite choreography' in spec or 'one of my favourite' in spec:
                songs = 'Bailey Sok And Sean Lew UP  Bailey Sok Choreography.mp4'
                os.startfile(os.path.join(choreography_dir, songs))
                speak("here is your flavor")
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
            else:
                cmdToFilters = ['can we have', 'song by', 'any', 'cover by', 'listen', 'yeah']
                data = UserInputFilter(spec, cmdToFilters).strip()
                print(data)
                with os.scandir(music_dir) as dirs:
                    for entry in dirs:
                        if data in entry.name.lower():
                            os.startfile(os.path.join(music_dir, entry.name))
                            speak("Let's enjoy your choice")
                            break

    def joke(self):
        joke = pyjokes.get_joke(language='en', category='all')
        print(joke)
        speak(joke)

    def privesc(self):
        speak('privilege escalation initialed... Jack i need your authorization')
        answer_from_jack = request_to_priv_esc_()
        if not answer_from_jack:
            speak("Access Denied. Bye, I Can't Let Him Down Sir")
        else:
            speak("Access Granted. Preceding Further")
            if os.name == 'nt':
                speak("Just wait sir, i'm working on it")
                danger_alert('critical')
