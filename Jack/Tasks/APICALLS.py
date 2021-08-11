import wolframalpha
from main import speak, takecmd

def UserInputFilter(UserInput, cmdToFilters):
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data

class ApiTask():
    def wolframalpha(self, UserInput):
        cmdToFilters = ['what is the', 'who is']
        data = UserInputFilter(UserInput, cmdToFilters)
        print(data)

        app_id = 'WLK8U4-HVUVRJGAVV'
        # Instance of wolframalpha
        client = wolframalpha.Client(app_id)
        # Stores the response from wolframalpha
        res = client.query(data)
        answer = next(res.results).text
        print(answer, '\n\n')
        speak(answer)