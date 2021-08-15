from Essentials.DataFilters import takecmd
from Jack.Accounts.PassMag.passmag import account_selecter_and_opener
from Jack.jmain import category
from Jack.Tasks.commands import Task

if __name__ == '__main__':
    while True:
        voiceInput = takecmd(vid='j')
        cat = category(voiceInput)

        if voiceInput != '!@#$%^&*()' or cat != 'NoCat':
            print(voiceInput+"\n")
            ask = Task()
            if cat == 'youtube':
                ask.youtube(voiceInput)
            elif cat == 'wikipedia':
                ask.wikipedia(voiceInput)
            elif cat == 'search':
                ask.search(voiceInput)
            elif cat == 'shutdown':
                ask.shutdown()
            elif cat == 'account':
                account_selecter_and_opener(voiceInput)
