import speech_recognition as sr
import os


def takecmd(vid='') -> str:
    r = sr.Recognizer()
    r.energy_threshold = 2000
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...\n')
        data = r.recognize_google(audio, language='en-in').lower()
        print(data)
        is_sleeping = wakeandsleep(vid, data)
        if is_sleeping != 'sleep':
            return data
        else:
            return '!@#$%^&*()'
    except Exception:
        print('\nI Didn\'t Got YOU\n')
        return ''


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


def UserInputFilter(UserInput: str, cmdToFilters: list) -> str:
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data.strip()
