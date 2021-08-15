from Essentials.DataFilters import takecmd
from Rivera.Rchatbot.rchatbot import importcoroutine


search = importcoroutine()
search.__next__()

while True:
    UserInput = takecmd(vid='r')
    search.send(UserInput)