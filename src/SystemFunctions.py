import os
import platform
import sys
from src import custom_errors as err, logger as log


def get_os(support_mac=False):
    user_os = platform.system().lower()
    if user_os == "windows":
        return 'windows'
    elif user_os == 'linux' or 'linux2':
        return 'linux'
    elif user_os == 'darwin':
        if support_mac:
            return 'mac'
        raise err.UnsupportedOSError(f'MacOS is not supported right now')
    raise err.UnsupportedOSError(os)


def validate_os(terminate_on_error=True, support_mac=False):
    try:
        user_os = get_os(support_mac)
        return user_os
    except err.UnsupportedOSError:
        if terminate_on_error and user_os is not None:  # TODO: Might be problematic -> check and improve if necessary
            terminate(termination_source=f'unsupported OS "{user_os}" was used!')
        elif terminate_on_error:
            terminate(termination_source=f'unsupported OS was used!')


def clear():
    current_os = validate_os()
    if current_os == 'windows':
        os.system('cls')
    elif current_os == 'linux' or 'linux2':
        os.system('clear')


def terminate(termination_source=__name__, exit_code=0, termination_reason=None):
    if termination_reason is None:
        log.main.warning(f"The program or program subscript {termination_source} will now be shut down...")
    else:
        log.main.warning(f"The program or program subscript {termination_source} will now be shut down because "
                         f"of {termination_reason}...")
    sys.exit(exit_code)