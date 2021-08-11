from Jack.jvoice import speak
from Jack.Accounts.PassMag.encryption import decryptPassword
from Essentials.DataFilters import UserInputFilter, takecmd
from Jack.Accounts.accountsHandler import Account


def logincred(acctologin: str):
    speak(f"{acctologin} Password Please")
    # pwd = takecmd()
    pwd = "actully jack i really don't care about my passwords"
    scrt = decryptPassword(pwd)

    for accDetails in scrt.split():
        a = accDetails.split('--')
        if a[0] == acctologin:
            return a


def account_selecter_and_opener(UserInput: str):
    cmdToFilters = ['to', 'can you please', 'could', 'login', 'log on', 'log in', 'sigh in', 'on']
    data = UserInputFilter(UserInput, cmdToFilters)
    cred = logincred(data)
    if data == 'instagram':
        Account(cred[1], cred[2]).instagram()
    elif data == 'facebook':
        Account(cred[1], cred[2]).facebook()
