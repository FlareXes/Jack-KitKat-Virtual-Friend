#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from hashID import writeResult
from hashID import HashID

def getHashMode(hashString):
    modeList = writeResult(HashID().identifyHash(hashString), outfile=None, hashcatMode=True)
    return modeList

def crackHash(hashString):
    # hashString = 'd033e22ae348aeb5660fc2140aec35850c4da997'
    mode = getHashMode(hashString)
    wordlist = '/home/hacker/Desktop/KitKat/Rivera/Hacker/wordlist/common.txt'
    subprocess.run(['hashcat', '-m', str(mode[0]), hashString, '--wordlist', wordlist])
    print()
    subprocess.run(['hashcat', '-m', str(mode[0]), hashString, '--wordlist', wordlist, '--show'])

# crackHash()

# Hacker - 4baf5897963fc12d1cd8fe1a02eb48fb
# hacker - d6a6bc0db10694a2d90e3a69648f3a03
# hackme - 23b4222d2613a2765d4d432d2d65e88e
# admin  - 21232f297a57a5a743894a0e4a801fc3
# admin  - d033e22ae348aeb5660fc2140aec35850c4da997