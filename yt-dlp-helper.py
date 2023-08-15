import platform
import sys
import os
import urllib.request as url
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

URLError = False


def validate_url(url):
    if str(url).startswith('https://www.youtube.com/watch?v=') | str(url).startswith('youtube.com/watch?v=') | \
            str(url).startswith('https://youtu.be/'):
        return True
    else:
        return False


def download_video(url):
    os.system(f'.\yt-dlp --config-location "./default.conf" {url}')


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('yt-dlp-helper')

        instructionLabel = qtw.QLabel('Input video URL!', self)
        self.URLBox = qtw.QLineEdit(self)
        submitButton = qtw.QPushButton('Enter', self, shortcut=qtg.QKeySequence('return'), clicked=self.onPush)
        self.errorLabel = qtw.QLabel('<span style="color:red;">Invalid URL! Make sure to use a youtube video link!'
                                     '</span>', self)
        self.errorLabel.setVisible(False)

        layout = qtw.QVBoxLayout()
        sublayout = qtw.QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(instructionLabel)
        layout.addLayout(sublayout)
        layout.addWidget(self.errorLabel)

        sublayout.addWidget(self.URLBox)
        sublayout.addWidget(submitButton)

        self.show()

    def onPush(self):
        url = self.URLBox.text()
        if validate_url(url):
            self.errorLabel.setVisible(False)
            download_video(url)
        else:
            self.errorLabel.setVisible(True)
        self.URLBox.setText('')


if __name__ == '__main__':
    if platform.system().lower() == 'windows':
        if not os.path.exists('./yt-dlp.exe'):
            url.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', './yt-dlp.exe')
    elif platform.system().lower() == 'linux' or 'linux2':
        if not os.path.exists('./yt-dlp'):
            url.urlretrieve('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp', 'yt-dlp')
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    if not os.path.exists('./default.conf'):
        file = open('./default.conf', 'w', encoding='utf-8')
        file.write(f'-P "{os.getcwd()}/videos"\n-o "%(title)s.%(ext)s"\n--windows-filenames')
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
