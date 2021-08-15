import webbrowser
import wikipedia
from Essentials.DataFilters import takecmd, wakeandsleep
from Jack.jvoice import speak
import urllib
import time
from os import system



def UserInputFilter(UserInput, cmdToFilters):
    data = ''
    for i in cmdToFilters:
        if i in UserInput:
            data = UserInput.split(i)[1]
            break
    if data == '':
        data = UserInput
    return data

class Task:
    def jsleep(self, UserInput: str):
        speak("Ok, I'm Down")
        if 'between me and rivera' in UserInput or 'can you please' in UserInput or 'go to sleep' in UserInput:
            wakeandsleep('sleep')

    def wikipedia(self, UserInput: str):
        try:
            speak('Give Me A Second')
            cmdToFilters = ['about', 'related to', 'related']
            data = UserInputFilter(UserInput, cmdToFilters)
            print('\nFor more information check out this page   👇👇👇')
            print(f'https://en.wikipedia.org/wiki/' + urllib.parse.quote(data))
            results = wikipedia.summary(data, sentences=2)
            speak(results)
        except wikipedia.exceptions.PageError as e:
            print("\nPage Not Found!")


    def youtube(self, UserInput: str):
        if UserInput in "open youtube":
            webbrowser.open('https://www.youtube.com')
        elif 'youtube for' or 'youtube related' in UserInput:
            cmdToFilters = ['youtube for', 'youtube', 'related to', 'related']
            data = UserInputFilter(UserInput, cmdToFilters)
            speak('Searching For' + data)
            webbrowser.open('https://www.youtube.com/results?search_query=' + urllib.parse.quote(data))
            time.sleep(5)
            speak('Here Are The Results')

    def search(self, UserInput: str):
        speak('Okay, Just Wait A Second')
        cmdToFilters = ['search for', 'google about', 'google for', 'google', 'search']
        data = UserInputFilter(UserInput, cmdToFilters)
        webbrowser.open('https://duckduckgo.com/?q=' + urllib.parse.quote(data))

    def shutdown(self):
        speak("Alert! System is about to shutdown soon")
        system('shutdown /s /t 1')


    def changedns(self):
        # netsh interface ipv4 set dns name="Wi-Fi" static 8.8.4.4
        # netsh interface ipv4 set dns name=”Wi-Fi” static 8.8.8.8 index=2
        speak("This will gonna take few seconds")
        import win32com.shell.shell as shell
        commands = 'netsh interface ipv4 set dns name="Wi-Fi" static 208.67.222.222 & netsh interface ipv4 set dns ' \
                   'name=”Wi-Fi” static 208.67.220.220 index=2 '
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
        system("ipconfig /release & ipconfig /renew")
        speak("OpenDNS Server will ready to use in 10 seconds")


    def rivera(self):
        speak("Okayy, She Will Be Alive Under 30 Sec")
        system(r"python C:\Users\as808\OneDrive\Documents\KitKat\Rivera\rmain.py")