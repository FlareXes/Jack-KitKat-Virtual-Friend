import wolframalpha
from twilio.rest import Client
from Essentials.DataFilters import takecmd
from Jack.jvoice import speak


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
    def wolframalpha(self):
        app_id = 'WLK8U4-HVUVRJGAVV'
        # Instance of wolframalpha
        client = wolframalpha.Client(app_id)

        while True:
            try:
                UserInput = takecmd()
                if not 'stop wolfalpha' in UserInput:
                    cmdToFilters = ['what is the', 'who is']
                    data = UserInputFilter(UserInput, cmdToFilters)
                    print(data)
                    # Stores the response from wolframalpha
                    res = client.query(data)
                    answer = next(res.results).text
                    print(answer, '\n\n')
                    speak(answer)
                else:
                    break
            except Exception:
                print("🤔🤔🤔🤔💭💭💭💭")
                pass

    def twiliocall(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'ACe279fadef07678e69535cfde42fe1704'
        auth_token = '3081a8c9428fdf5ef4c7746e6b52ddfd'
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            # url='http://demo.twilio.com/docs/voice.xml',
            twiml='<Response><Say>I Think You Got My Point. Don\'t Worry About Rivera.\
             After This She Will Be My Priority. See You There Soon Ra-Dou-Woo. \
             And Yeah! She\'s Is Doing Pretty Dam Work</Say></Response>',
            to='+918955349252',
            from_='+15162724924'
        )


    def twiliosms(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'ACe279fadef07678e69535cfde42fe1704'
        auth_token = '3081a8c9428fdf5ef4c7746e6b52ddfd'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Hey Jack! Here, I Think You Got My Point",
            from_='+15162724924',
            to='+918955349252'
        )