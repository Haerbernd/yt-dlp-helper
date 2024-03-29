from src import custom_errors as err, FileIO, SystemFunctions, Cleaner
import platform
import subprocess
import os.path
import shutil


def get_config_path():
    current_os = SystemFunctions.validate_os(terminate_on_error=False)

    if current_os == 'windows':
        shell = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE)
        user = shell.communicate()[0].decode().split('\\')[-1]
        config_path_f = f'C:/Users/{user}/AppData/Roaming/yt-dlp-helper'
        config_path_f = Cleaner.remove_newlines(config_path_f)
    elif current_os == 'linux':
        shell = subprocess.Popen('logname', shell=True, stdout=subprocess.PIPE)
        #  Notice: The usage of "logname" returns the username the user logged into -> sudo resistant
        user = shell.communicate()[0].decode()
        config_path_f = f'/home/{user}/.yt-dlp-helper'
        config_path_f = Cleaner.remove_newlines(config_path_f)
    else:
        input(f'Your current Operating System {platform.system()} is not supported. Currently supported are only '
              f'Windows and Linux\nPress Enter to exit the program...')
        if __name__ == '__main__':
            SystemFunctions.terminate(termination_reason='using an unsupported OS')
        else:
            raise err.UnsupportedOSError(current_os)  # TODO: current_os might be empty

    if not os.path.exists(config_path_f):
        os.mkdir(config_path_f)

    if os.path.exists(f'{config_path_f}/config.json'):
        return f'{config_path_f}/config.json'

    shutil.copyfile('.meta/default_config.json', f'{config_path_f}/config.json')
    return f'{config_path_f}/config.json'


def get_config():
    try:
        config_path = get_config_path()
    except err.UnsupportedOSError:
        SystemFunctions.terminate(termination_reason='using an unsupported OS')

    config = FileIO.load_dict_from_json_file(f'{config_path}', open_mode='r')
    return config


def update_config(config_new):
    try:
        config_path = get_config_path()
    except err.UnsupportedOSError:
        SystemFunctions.terminate(termination_reason='using an unsupported OS')

    FileIO.write_dict_to_json_file(f'{config_path}', config_new)
