from src import logger as log
import os
import platform
import re
import sys
import json
import ast


class Cleaner:
    @staticmethod
    def list_to_string(list_that_will_be_converted, keep_comma=True, add_newlines=False):
        list_that_will_be_converted = str(list_that_will_be_converted)
        list_that_will_be_converted = re.sub('\[', '', list_that_will_be_converted)
        list_that_will_be_converted = re.sub(']', '', list_that_will_be_converted)
        list_that_will_be_converted = re.sub("'", '', list_that_will_be_converted)
        if add_newlines:
            list_that_will_be_converted = re.sub(', ', ',\n', list_that_will_be_converted)
        if not keep_comma:
            list_that_will_be_converted = re.sub(',', '', list_that_will_be_converted)
        return list_that_will_be_converted


class System:
    @staticmethod
    def clear():
        if platform.system().lower() == 'windows':
            os.system('cls')
        elif platform.system().lower() == 'linux' or 'linux2':
            os.system('clear')

    @staticmethod
    def terminate(termination_source, exit_code=0, termination_reason=None):
        if termination_reason is None:
            log.main.warning(f"The program or program subscript {termination_source} will now be shut down...")
        else:
            log.main.warning(f"The program or program subscript {termination_source} will now be shut down because "
                             f"of {termination_reason}...")
        sys.exit(exit_code)


class Color:
    reset = '\u001b[0m'
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'


class BgColor:
    black = '\u001b[40m'
    red = '\u001b[41m'
    green = '\u001b[42m'
    yellow = '\u001b[43m'
    blue = '\u001b[44m'
    magenta = '\u001b[45m'
    cyan = '\u001b[46m'
    white = '\u001b[47m'


class TextStyle:
    none = ''
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reverse = '\u001b[7m'
