'''
def UserInputFilter(UserInput: str, cmdToFilters: list) -> str:
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data.strip()
'''


# Use Below Code If You Want Execute Command Only If You Start Conversion By Their Name
'''
def takecmd(vid='', callExceptions=False) -> str:
    r = sr.Recognizer()
    r.energy_threshold = 2000
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...\n')
        recognized_data = r.recognize_google(audio, language='en-in').lower()

        if callExceptions == False:
            if recognized_data[:4] == 'jack':
                data = recognized_data[5:]
                print(data)
                is_sleeping = wakeandsleep(vid, data)
                if is_sleeping != 'sleep':
                    return data
                else:
                    return '!@#$%^&*()'
            else:
                return "Nothing To Say"
    except Exception:
        print('\nI Didn\'t Got YOU\n')
        return ''
'''


'''
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
'''