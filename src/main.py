import sys
from src import logger as log, utils
import os

queue = []


def start(config):
    log.main.info('Main program started...')

    video = input('Input video/playlist to download!\n')
    queue.append(video)
    os.system('cls')
    log.debug.debug('Cleaned screen...')

    while True:
        video = input('Input video/playlist to download!\n\n'
                      'Input ' + utils.Color.red + '!done' + utils.Color.reset +
                      ' when all videos/playlists that you wish to download are inputted!\n')
        if video == '!done':
            break
        queue.append(video)
        os.system('cls')
        log.debug.debug('Cleaned screen...')
    os.system('cls')
    log.debug.debug('Cleaned screen...')

    for i in queue:
        log.main.info('Started downloading a video...')
        log.debug.debug('Started downloading ' + str(i))
        print(config['drive'] + ':&cd ' + config['yt-dlp-path'] + '&.\yt-dlp ' + i)
        os.system(config['drive'] + ':&cd ' + config['yt-dlp-path'] + '&.\yt-dlp ' + i)
        log.main.info('Finished downloading a video/playlist')
        log.debug.debug('Finished downloading ' + str(i))
        os.system('cls')
        log.debug.debug('Cleaned screen...')
    log.main.info('Finished downloading all videos/playlists...')
    log.main.info('Program will now be shutted down as it finished all operations...')
    input()
    sys.exit(0)
