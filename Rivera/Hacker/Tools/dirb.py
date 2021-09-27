import subprocess

target = input("Target URL: ")

subprocess.run(['dirb', target, 'wordlist/common.txt'])