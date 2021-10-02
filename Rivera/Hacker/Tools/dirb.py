import subprocess

def exec_():
    target = input("Target URL: ")
    subprocess.run(['dirb', target, 'wordlist/common.txt'])