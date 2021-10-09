import subprocess

def exec_():
    target = input("Target: ")
    subprocess.run(['sudo', 'nmap', '-oN', 'nmap-results.txt', '-sS', '-sV', '-A', '-T4', target])