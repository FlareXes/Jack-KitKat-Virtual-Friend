import speech_recognition as sr


def takecmd() -> str:
    r = sr.Recognizer()
    r.energy_threshold = 1000
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        data = r.recognize_google(audio, language='en-in')
        print(data)
    except Exception:
        print('I Didn\'t Got YOU')
        return 'None'
    return data.lower()


def UserInputFilter(UserInput: str, cmdToFilters: list) -> str:
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data.strip()
