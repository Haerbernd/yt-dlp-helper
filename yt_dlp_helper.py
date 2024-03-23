from src import config_handler, logger as log, SystemFunctions
import sys
import os
import re
import urllib.request as url
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


# This function only validates whether a URL is technically a correct YouTube link not if it is a working URL
# TODO: clean this up by simplifying it
def validate_url(link):
    if str(link).startswith('http:'):
        link = re.sub('http:', 'https:', str(link))
    if str(link).startswith('https://www.youtube.com/watch?v=') | str(link).startswith('youtube.com/watch?v=') | \
            str(link).startswith('https://youtu.be/') | str(link).startswith('youtu.be/') | \
            str(link).startswith('https://youtube.com/watch?v=') | str(link).startswith('www.youtube.com/playlist') | \
            str(link).startswith('https://www.youtube.com/playlist') | str(link).startswith('youtube.com/shorts') | \
            str(link).startswith('https://youtube.com/shorts'):
        return True
    return False


def download_video(link, config_file, use_global_config):
    if not use_global_config:
        os.system(f'.\\yt-dlp --config-location "{config_file}" "{link}"')
    else:
        os.system(f'.\\yt-dlp) "{link}"')


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('yt-dlp-helper')
        self.resize(300, 50)

        instructionLabel = qtw.QLabel('Input video URL!', self)
        self.URLBox = qtw.QLineEdit(self)
        submitButton = qtw.QPushButton('Enter', self, shortcut=qtg.QKeySequence('return'), clicked=self.onPush)

        self.errorLabel = qtw.QLabel('<span style="color:red;">Invalid URL! Make sure to use a youtube video link!'
                                     '</span>', self)
        self.errorLabel.setVisible(False)

        layout = qtw.QVBoxLayout()
        sublayout = qtw.QHBoxLayout()

        #  Hint: The Order in which the labels are added is important -> Do not change!
        self.setLayout(layout)
        layout.addWidget(instructionLabel)
        layout.addLayout(sublayout)
        layout.addWidget(self.errorLabel)

        sublayout.addWidget(self.URLBox)
        sublayout.addWidget(submitButton)

        self.show()

    def onPush(self):
        link = self.URLBox.text()
        self.URLBox.setText('')
        if validate_url(link):
            self.errorLabel.setVisible(False)
            config = config_handler.get_config()
            download_video(link, config['localYt-dlpConfigName'], use_global_config=config['useGlobalYt-dlpConfig'])
        else:
            self.errorLabel.setVisible(True)


def get_os_specific_yt_dlp_binary_extension():
    current_os = SystemFunctions.validate_os()

    if current_os == 'windows':
        return '.exe'
    elif current_os == 'linux':
        return ''


if __name__ == '__main__':
    if not os.path.exists(f'./yt-dlp{get_os_specific_yt_dlp_binary_extension()}'):
        url.urlretrieve(f'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp'
                        f'{get_os_specific_yt_dlp_binary_extension()}', f'yt-dlp'
                                                                        f'{get_os_specific_yt_dlp_binary_extension()}')

    # TODO: Make the following block more versatile and responsive to the config -> later Update
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    if not os.path.exists('.meta/default.conf'):
        file = open('.meta/default.conf', 'w', encoding='utf-8')
        file.write(f'-P "{os.getcwd()}/videos"\n-o "%(title)s.%(ext)s"\n--windows-filenames')
        file.close()

    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
