import logging
from datetime import datetime
import os
from os.path import exists

if exists('log.log'):
    os.remove('log.log')

logging.basicConfig(filename='log.log',
                    format='%(asctime)s:\t[%(name)s]:\t\t%(module)s\t%(levelname)s\t%(lineno)d:\t%(message)s',
                    level=logging.DEBUG)
logging.info('BasicConfiguration of logging done...')
form = logging.Formatter('%(asctime)s:\t[%(name)s]:\t\t%(module)s\t%(levelname)s\t%(lineno)d:\t%(message)s')
logging.info('Formatter form was created...')
form_debug = logging.Formatter('%(asctime)s:\t[%(name)s]:\t%(module)s\t%(levelname)s\t%(lineno)d:\t%(message)s')
logging.info('Formatter form_debug was created...')

main = logging.getLogger('main')
logging.info('Created Logger main...')
main.setLevel(logging.INFO)
logging.info('Set logging-level of Logger main to INFO...')
try:
    logging.info('Try assigning fileh_main as FileHandler...')
    fileh_main = logging.FileHandler('logs/main/' + str(datetime.utcnow().strftime('%Y-%m-%d_%I-%M-%S')) + '.log')
except FileNotFoundError:
    logging.warning('Failed to assign folder logs/main to FileHandler fileh_main...')
    try:
        logging.info('Try creating folder logs...')
        os.mkdir('logs')
    except FileExistsError:
        logging.warning('Folder logs already exists...')
    logging.info('Try creating folder logs/main...')
    os.mkdir('logs/main')
    logging.info('Try assigning fileh_main as FileHandler...')
    fileh_main = logging.FileHandler('logs/main/' + str(datetime.utcnow().strftime('%Y-%m-%d_%I-%M-%S')) + '.log')
logging.info('Succeeded...')
fileh_main.setFormatter(form)
logging.info('Formatter form was assigned to fileh_main...')
main.addHandler(fileh_main)
logging.info('FileHandler fileh_main was assigned to main...')

debug = logging.getLogger('debug')
logging.info('Created Logger debug...')
debug.setLevel(logging.DEBUG)
logging.info('Set logging-level of Logger debug to DEBUG...')
try:
    logging.info('Try assigning fileh_debug as FileHandler...')
    fileh_debug = logging.FileHandler('logs/debug/' + str(datetime.utcnow().strftime('%Y-%m-%d_%I-%M-%S')) + '.log')
except FileNotFoundError:
    logging.warning('Failed to assign folder logs/debug to FileHandler fileh_debug...')
    logging.info('Try creating folder logs/debug...')
    os.mkdir('logs/debug')
    logging.info('Try assigning fileh_debug as FileHandler...')
    fileh_debug = logging.FileHandler('logs/debug/' + str(datetime.utcnow().strftime('%Y-%m-%d_%I-%M-%S')) + '.log')
logging.info('Succeeded...')
fileh_debug.setFormatter(form_debug)
logging.info('Formatter form_debug was assigned to fileh_debug...')
debug.addHandler(fileh_debug)
logging.info('FileHandler fileh_debug was assigned to debug...')

logging.info('Initialization of logging done...\n\n')
