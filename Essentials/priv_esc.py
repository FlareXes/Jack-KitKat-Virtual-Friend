import codecs
from Essentials.DataFilters import takecmd
from Jack.jvoice import speak
from Jack.Tasks.APICALLS import ApiTask
import shutil
import os

def request_to_priv_esc_() -> bool:
    speak("Attention Please Rivera! Has Been Requested For Privilege Escalation. Should I Authorize Her")
    while True:
        data = takecmd()
        if 'yes' in data:
            return True
        elif 'no' in data:
            return False
        else:
            speak("Okay, Rivera! Has Been Requested For Privilege Escalation. Should I Authorize Her")

def danger_alert(danger_level: str):
    print("This was the critical action")
    exit()
    '''
    project_loc = 'C:\\Users\\as808\\OneDrive\\Documents\\KitKat'
    if danger_level == 'critical':
        # First
        os.remove('C:\\Users\\as808\\OneDrive\\Documents\\KitKat\\Jack\\Accounts\\PassMag\\testing.json')

        # Second
        import smtplib
        to = "jackdaclin@gmail.com"
        content = "Warning Someone Is There!"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('jackdaclin@gmail.com', codecs.decode('tenff#bccre123', 'rot_13'))
        server.sendmail('jackdaclin@gmail.com', to, content)
        server.close()

        # Third
        twilio = ApiTask()
        twilio.twiliosms()
        twilio.twiliocall()
        
        # Forth
        # shutil.rmtree('loc')
    '''
