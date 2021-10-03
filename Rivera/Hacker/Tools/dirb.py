import subprocess

def exec_():
    target = input("Target URL: ")
    subprocess.run(['dirb', target, '-f'])

# target = "http://testphp.vulnweb.com/"

exec_()