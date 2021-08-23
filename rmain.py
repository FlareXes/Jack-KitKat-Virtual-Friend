from Essentials.DataFilters import takecmd, delsleepfiles
from Rivera.Rchatbot.rchatbot import importcoroutine

if __name__ == '__main__':
    delsleepfiles('rivera')
    search = importcoroutine()
    search.__next__()
    while True:
        UserInput = takecmd(vid='r')
        search.send(UserInput)