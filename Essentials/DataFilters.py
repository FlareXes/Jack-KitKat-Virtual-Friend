import speech_recognition as sr
import os
import time


def takecmd(vid='', callExceptions=True) -> str:
    r = sr.Recognizer()
    r.energy_threshold = 2000
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...\n')
        recognized_data = r.recognize_google(audio, language='en-in').lower()
        if callExceptions == False:
            if recognized_data == 'sophie' or recognized_data == 'rivera':
                print("------------------------------------------------------")
                print('Rivera Listening...')

                with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
                    audio = r.listen(source)
                print('Recognizing...\n')
                data = r.recognize_google(audio, language='en-in').lower()
                print(data)
                return data
            else:
                return "Nothing To See Here"
        else:
            return recognized_data
    except Exception:
        print('\nI Didn\'t Got YOU\n')
        return ''


def UserInputFilter(UserInput: str, cmdToFilters: list) -> str:
    datalendict = {}
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            newdict = {data: len(data)}
            datalendict.update(newdict)
    try:
        dataWithMinLength = min(datalendict, key=datalendict.get)
        if len(datalendict) > 1 and dataWithMinLength == '':
            datalendict.pop(dataWithMinLength)
            data = min(datalendict, key=datalendict.get)
        else:
            data = dataWithMinLength
    except ValueError as e:
        data = UserInput
         # if data == '': data = UserInput  (Use Them If Needed)
    return data.strip()


# < --  Sleeping Functionalities  -- >

def wakeandsleep(vid: str, takecmddata='') -> str:
    sleep_loc = f'C:\\Users\\as808\\OneDrive\\Documents\\KitKat\\Essentials\\{vid}sleep.txt'
    try:
        if 'go to sleep' in takecmddata or 'sleep' in takecmddata or 'between me and rivera' in takecmddata \
                or 'between me and jack' in takecmddata:
            with open(sleep_loc, 'w') as file:
                file.write('hi')
                file.close()
        if 'jack are you there' in takecmddata or 'wake up jack' in takecmddata or 'hey jack' in takecmddata:
            print("removing jack sleeping functionality...........\n")
            sleep_loc = f'C:\\Users\\as808\\OneDrive\\Documents\\KitKat\\Essentials\\jsleep.txt'
            os.remove(sleep_loc)
        elif 'sophie are you there' in takecmddata or 'wake up sophie' in takecmddata or 'hey sophie' in takecmddata:
            print("removing rivera sleeping functionality...........\n")
            sleep_loc = f'C:\\Users\\as808\\OneDrive\\Documents\\KitKat\\Essentials\\rsleep.txt'
            os.remove(sleep_loc)

        if os.path.exists(sleep_loc):
            return 'sleep'
        else:
            return 'wake'
    except FileNotFoundError:
        pass


def delsleepfiles(UserFileDelete: str):
    jack_sleep_loc = '../KitKat/Essentials/jsleep.txt'
    rivera_sleep_loc = '../KitKat/Essentials/rsleep.txt'

    if UserFileDelete == 'jack' and os.path.exists(jack_sleep_loc):
        os.remove(jack_sleep_loc)
    elif UserFileDelete == 'rivera' and os.path.exists(rivera_sleep_loc):
        os.remove(rivera_sleep_loc)