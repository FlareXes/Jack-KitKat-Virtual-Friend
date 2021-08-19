import time
import webbrowser
from Jack.jvoice import speak
import os

class StartApp:
    def __init__(self):
        self.funcDict = {
                    "spotify": self.spotify, "vs code": self.vscode, 'visual studio code': self.vscode,
                    "vs 2019": self.vs2019, "canva": self.canva, "o b s studio": self.obstudio,
                    "screen recoder": self.obstudio, 'jupyter lab': self.jupyterlab, "parrot": self.parrotos,
                    'server': self.ubuntuserver, "vmware player": self.vmwareplayer, 'vmware': self.vmware,
                    'virtual box': self.virtualbox, 'onenote': self.onenote, 'settings': self.settings,
                    'control panel': self.controlpanel
                    }


    def spotify(self):
        spotify_loc = 'C:\\Users\\as808\\Spotify - Shortcut'
        os.startfile(os.path.join(spotify_loc))

    def vscode(self):
        vscode_dir = 'C:\\Users\\as808\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(vscode_dir)

    def vs2019(self):
        vs2019_dir = '"D:\\Program Files\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"'
        os.startfile(vs2019_dir)

    def canva(self):
        canva_loc = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\canva'
        os.startfile(canva_loc)

    def obstudio(self):
        obs_studio = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit)'
        os.startfile(obs_studio)

    def jupyterlab(self):
        anaconda_prompt = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook (anaconda3)'
        os.startfile(anaconda_prompt)
        time.sleep(8)
        webbrowser.open('http://localhost:8888/lab')

    def parrotos(self):
        parrot_os = 'D:\\Documents\\VirtualBox VMs\\Parrot Security\\Parrot Security.vbox'
        os.startfile(parrot_os)

    def ubuntuserver(self):
        ubuntu_server = 'D:\\Virtual Box\\CodeServer\\CodeServer.vbox'
        os.startfile(ubuntu_server)

    def vmware(self):
        vmware_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VMware\\VMware Workstation Pro'
        os.startfile(vmware_loc)

    def vmwareplayer(self):
        vmware_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VMware\\VMware Workstation 16 Player'
        os.startfile(vmware_loc)

    def virtualbox(self):
        virtualbox_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle VM VirtualBox\\Oracle VM VirtualBox'
        os.startfile(virtualbox_loc)

    def onenote(self):
        onenote_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote'
        os.startfile(onenote_loc)

    def settings(self):
        settings_loc = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings'
        os.startfile(settings_loc)

    def controlpanel(self):
        controlpanel_loc = 'C:\\Users\\as808\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel'
        os.startfile(controlpanel_loc)
