import platform
import os
import sys
import re
import subprocess
import urllib.request as url
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.show()


def get_config_path():
    if platform.system().lower() == 'windows':
        shell = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE)
        user = shell.communicate()[0].decode().split('\\')[-1]
        config_path = f'C:/Users/{user}/AppData/Roaming/yt-dlp-helper'
        return config_path
    elif platform.system().lower() == 'linux' or 'linux2':
        shell = subprocess.Popen('logname', shell=True, stdout=subprocess.PIPE)
        #  Notice: The usage of "logname" returns the username the user logged into -> sudo resistant
        user = shell.communicate()[0].decode()
        config_path = f'/home/{user}/.yt-dlp-helper'
        return config_path
    else:
        input(
            f'Your current Operating System {platform.system()} is not supported. Currently supported are only Windows'
            f' and Linux\nPress Enter to exit the program...')
        if __name__ == '__main__':
            sys.exit(0)
        else:
            return 'Unsupported OS'


if __name__ == '__main__':
    config_path = get_config_path()

    #  Start of the GUI
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
