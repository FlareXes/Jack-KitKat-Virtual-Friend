import subprocess

def exec_():
    target = input("Target: ")
    subprocess.run(['sudo', 'nmap', '-sS', '-A', '-T4', target])