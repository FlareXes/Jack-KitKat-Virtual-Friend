from Essentials.DataFilters import takecmd
from Jack.Accounts.PassMag.passmag import account_selecter_and_opener
from Jack.Tasks.commands import Task


def category(UserInput: str) -> str:
    UserInputList = UserInput.strip().split(' ')

    # 1. Filter
    categories = {
        'wikipedia': ['related', 'to', 'do', 'you', 'know', 'anything', 'about', 'wikipedia', 'for', 'tell', 'me'],
        'search': ['google', 'for', 'search', 'related', 'to'],
        'youtube': ['youtube', 'for', 'open', 'related', 'to', 'search'],
        'shutdown': ['shutdown', 'system'],
        'account': ['login', 'log', 'in', 'sign', 'up', 'instagram', 'facebook', 'account', 'discord']}
    matchlengthdict = {}
    for category in categories.items():
        length = len(set(category[1]).intersection(UserInputList))
        # Special case for {on category}
        if UserInputList[-2:] and category[0] == ['on', str(category[0])]:
            length += 1
        newdict = {category[0]: length}
        matchlengthdict.update(newdict)
    print(matchlengthdict)
    return max(matchlengthdict, key=matchlengthdict.get)


if __name__ == '__main__':
    voiceInput = takecmd()
    category = category(voiceInput)
    ask = Task()
    if category == 'youtube':
        ask.youtube(voiceInput)
    elif category == 'wikipedia':
        ask.wikipedia(voiceInput)
    elif category == 'search':
        ask.search(voiceInput)
    elif category == 'shutdown':
        ask.shutdown()
    elif category == 'account':
        # account_selecter_and_opener(voiceInput)

        account_selecter_and_opener('login to facebook')