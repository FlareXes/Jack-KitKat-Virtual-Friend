import time
import webbrowser
from Jack.jvoice import speak
import os


def spotify():
    spotify_loc = 'C:\\Users\\as808\\Spotify - Shortcut'
    os.startfile(os.path.join(spotify_loc))

def vscode():
    vscode_dir = 'C:\\Users\\as808\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    os.startfile(vscode_dir)

def vs2019():
    vs2019_dir = '"D:\\Program Files\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"'
    os.startfile(vs2019_dir)

def canva():
    canva = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\canva'
    os.startfile(canva)

def obstudio():
    obs_studio = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit)'
    os.startfile(obs_studio)


def jupyterlab():
    anaconda_prompt = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook (anaconda3)'
    os.startfile(anaconda_prompt)
    time.sleep(8)
    webbrowser.open('http://localhost:8888/lab')

def parrotos():
    parrot_os = 'D:\\Documents\\VirtualBox VMs\\Parrot Security\\Parrot Security.vbox'
    os.startfile(parrot_os)

def ubuntuserver():
    ubuntu_server = 'D:\\Virtual Box\\CodeServer\\CodeServer.vbox'
    os.startfile(ubuntu_server)

def vmware():
    vmware_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VMware\\VMware Workstation Pro'
    os.startfile(vmware_loc)

def vmwareplayer():
    vmware_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VMware\\VMware Workstation 16 Player'
    os.startfile(vmware_loc)

def virtualbox():
    virtualbox_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle VM VirtualBox\\Oracle VM VirtualBox'
    os.startfile(virtualbox_loc)

def onenote():
    onenote_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote'
    os.startfile(onenote_loc)

def settings():
    settings_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings'
    os.startfile(settings_loc)

def controlpanel():
    controlpanel_loc = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel'
    os.startfile(controlpanel_loc)
