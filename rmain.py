from Essentials.DataFilters import takecmd, delsleepfiles
from Rivera.Rchatbot.rchatbot import importcoroutine

if __name__ == '__main__':
    delsleepfiles('rivera')             # Delete Sleeping Files If Exists After New Start
    search = importcoroutine()
    search.__next__()
    while True:
        UserInput = takecmd(True)
        search.send(UserInput)