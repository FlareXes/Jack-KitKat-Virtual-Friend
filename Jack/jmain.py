from Essentials.DataFilters import takecmd, wakeandsleep
from Jack.Accounts.PassMag.passmag import account_selecter_and_opener
from Jack.Tasks.commands import Task


def category(UserInput: str) -> str:
    try:
        UserInputList = UserInput.strip().split(' ')

        # 1. Filter
        categories = {
            'wikipedia': ['related', 'know', 'anything', 'about', 'wikipedia', 'tell'],
            'search': ['google', 'search', 'related'],
            'youtube': ['youtube', 'open', 'related', 'search'],
            'shutdown': ['shutdown', 'system'],
            'account': ['login', 'log', 'in', 'sign', 'up', 'instagram', 'facebook', 'account', 'discord']}
        matchlengthdict = {}
        for category in categories.items():
            length = len(set(category[1]).intersection(UserInputList))
            # Special case for {on category}
            if f"{category} for" in UserInput:
                length += 1

            # if UserInputList[-2:] and category[0] == ['on', str(category[0])]:
            #     length += 1
            newdict = {category[0]: length}
            matchlengthdict.update(newdict)
        print(matchlengthdict)
        if len(list(set(list(matchlengthdict.values())))) != 1:
            return max(matchlengthdict, key=matchlengthdict.get)
    except Exception:
        return 'NoCat'


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
