import sys
import json
import time
import os
from src import main, utils, logger as log

if os.path.exists('C:\\Users\\' + str(os.getlogin()) + '\\AppData\\Roaming\\yt-dlp-help'):
    file = 'C:\\Users\\' + str(os.getlogin()) + '\\AppData\\Roaming\\yt-dlp-help\\alternate-config-path'
    file = open(file, 'r+', encoding='utf-8')
    tmp = file.read()
    file.close()
    file = tmp
else:
    file = 'config.json'

try:
    file = open(file, 'r+', encoding='utf-8')
    config = json.load(file)
    file.close()
except FileNotFoundError:
    log.main.error('Standart config file not found...')
    print('Config file not found!\nPlease input path to config!')
    try:
        file_path = input()
        file = file_path
        log.main.info('User inputted alternate conifg file path...')
        log.debug.debug('Alternate config path = ' + file)
        file = open(file, 'r+', encoding='utf-8')
        config = json.load(file)
        file.close()
    except FileNotFoundError:
        log.main.error('Alternate config file did not work...')
        log.main.warning('Proceeding to terminate program...')
        print('Path contained no config file!')
        time_until_termination = 5
        while time_until_termination > 0:
            print('The program will be terminated in ' + str(utils.Color.red) +
                  str(time_until_termination) + str(utils.Color.reset) + ' seconds...\r')
            log.main.error('The program will be terminated in ' + str(time_until_termination) + ' seconds...')
            time_until_termination = time_until_termination - 1
            time.sleep(1)
        log.main.debug('Program terminated...')
        sys.exit(0)
    file = open('C:\\Users\\' + str(os.getlogin()) + '\\AppData\\Roaming\\yt-dlp-help\\alternate-config-path',
                'w', encoding='utf-8')
    file.write(file_path)
    file.close()

log.main.info('Successfully loaded config file...')

log.main.info('Starting main program...')
main.start(config)
