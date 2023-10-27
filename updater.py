import json
import platform
import os
import sys
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
        config_path_f = f'C:/Users/{user}/AppData/Roaming/yt-dlp-helper'
        # the '_f' is merely used to differentiate the function variable from the non-function variable
        return config_path_f
    elif platform.system().lower() == 'linux' or 'linux2':
        shell = subprocess.Popen('logname', shell=True, stdout=subprocess.PIPE)
        #  Notice: The usage of "logname" returns the username the user logged into -> sudo resistant
        user = shell.communicate()[0].decode()
        config_path_f = f'/home/{user}/.yt-dlp-helper'
        return config_path_f
    else:
        input(
            f'Your current Operating System {platform.system()} is not supported. Currently supported are only Windows'
            f' and Linux\nPress Enter to exit the program...')
        if __name__ == '__main__':
            sys.exit(0)
        else:
            return 'Unsupported OS'


def update():
    pass


def get_newest_version():
    url.urlretrieve('https://haerbernd.dev/github/repositories/_external-data/yt-dlp-helper/newest-version.json',
                    './.meta/newest-version.json')


def check_version():
    get_newest_version()

    file = open('./.meta/newest-version.json', 'r', encoding='utf-8')
    newest_version = json.load(file)
    file.close()

    file = open('./.meta/version_data.json', 'r', encoding='utf-8')
    version_data = json.load(file)
    file.close()

    if newest_version['newest-version'] == version_data['current-version']:
        if version_data['current-version'] in newest_version['upgradable-from']:
            update()
        else:
            input('The program cannot upgrade to the newest version automatically! Visit https://github.com/Haerbernd/'
                  'yt-dlp-helper to get the newest release!\nPress Enter to exit the updater...')
    else:
        input('You have the newest version installed!')


if __name__ == '__main__':
    config_path = get_config_path()

    #  Start of the GUI
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
