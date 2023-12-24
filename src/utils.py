from src import logger as log, custom_errors as err
import os
import platform
import re
import sys
import json
import ast


class Cleaner:
    @staticmethod
    def list_to_pretty_string(list_that_will_be_converted, keep_comma=True, replace_comma_with_newline=False,
                              add_newline_after_comma=False):
        list_that_will_be_converted = str(list_that_will_be_converted)
        list_that_will_be_converted = re.sub('\\[', '', list_that_will_be_converted)
        list_that_will_be_converted = re.sub(']', '', list_that_will_be_converted)
        list_that_will_be_converted = re.sub("'", '', list_that_will_be_converted)
        if replace_comma_with_newline:
            list_that_will_be_converted = re.sub(', ', ',\n', list_that_will_be_converted)
        if add_newline_after_comma:
            list_that_will_be_converted = re.sub(', ', ',\n', list_that_will_be_converted)
        if not keep_comma:
            list_that_will_be_converted = re.sub(',', '', list_that_will_be_converted)
        return list_that_will_be_converted


class System:
    @staticmethod
    def get_os(support_mac=False):
        os = platform.system().lower()
        if os == "windows":
            return 'windows'
        elif os == 'linux' or 'linux2':
            return 'linux'
        elif os == 'darwin':
            if support_mac:
                return 'mac'
            raise err.UnsupportedOSError(f'MacOS is not supported right now')
        raise err.UnsupportedOSError(os)

    @staticmethod
    def validate_os(terminate_on_error=True):
        try:
            os = System.get_os()
        except err.UnsupportedOSError:
            if terminate_on_error:
                System.terminate()

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
