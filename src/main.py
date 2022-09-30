import sys
import logger as log
import os

queue = []


def start(config):
    log.main.info('Main program started...')
    os.system(str(config['drive']))
    log.debug.debug('Changed drive to ' + str(config['drive']) + '...')
    os.system('cd ' + str(config['yt-dlp-path']))
    log.debug.debug('Changed dictionary to ' + str(config['yt-dlp-path']) + '...')
    os.system('cls')
    log.debug.debug('Cleaned screen...')
    video = input('Input video/playlist to download!')
    queue.append(video)
    os.system('cls')
    log.debug.debug('Cleaned screen...')
    while True:
        video = input('Input video/playlist to download!\n'
                      'Input !done when all videos/playlists that you wish to download are inputted!')
        if video == '!quit':
            break
        queue.append(video)
        os.system('cls')
        log.debug.debug('Cleaned screen...')
    os.system('cls')
    log.debug.debug('Cleaned screen...')
    for i in queue:
        log.main.info('Started downloading a video...')
        log.debug.debug('Started downloading ' + str(i))
        os.system('.\yt-dlp ' + str(queue[i]))
        log.main.info('Finished downloading a video/playlist')
        log.debug.debug('Finished downloading ' + str(i))
        os.system('cls')
        log.debug.debug('Cleaned screen...')
    log.main.info('Finished downloading all videos/playlists...')
    log.main.info('Program will now be shutted down as it finished all operations...')
    sys.exit(0)
