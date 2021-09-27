import subprocess

target = input("Target: ")
subprocess.run(['sudo', 'nmap', '-sS', '-A', '-T4', target])
