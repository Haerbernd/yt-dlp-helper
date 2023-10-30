import json
import platform
import subprocess
import sys


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
        input(f'Your current Operating System {platform.system()} is not supported. Currently supported are only '
              f'Windows and Linux\nPress Enter to exit the program...')
        if __name__ == '__main__':
            sys.exit(0)
        else:
            return 'Unsupported OS'


def get_config():
    config_path = get_config_path()
    if config_path == 'Unsupported OS':
        return

    file = open(f'{config_path}/config.json', 'r', encoding='utf-8')
    config = json.load(file)
    file.close()
    return config


def update_config(config_new):
    config_path = get_config_path()
    if config_path == 'Unsupported OS':
        return

    file = open(f'{config_path}/config.json', 'w', encoding='utf-8')
    json.dump()
