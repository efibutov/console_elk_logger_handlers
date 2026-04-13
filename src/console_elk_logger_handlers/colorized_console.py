'''
Colorized console log handler
'''
import os
import sys
import shutil
from datetime import datetime as dt
from math import floor
from termcolor import colored
from logging import getLogger, Handler, DEBUG, WARNING, INFO, ERROR, LogRecord
SPACE_SYMBOL = ' '


class ColorizedConsole(Handler):
    '''
    Colorized console log handler
    '''
    MILLISECOND = 0.001
    LEVEL_COLORS = {
        'DEBUG': ('green', ['dark', 'on_blue']),
        'INFO': ('white', ['dark', 'blink']),
        'WARNING': ('blue', ['dark']),
        'ERROR': ('black', 'on_yellow', ['bold', 'underline']),
        'CRITICAL': ('yellow', ['bold', 'on_black']),
    }

    def __init__(self, level: int=DEBUG, name: str='') -> None:
        super().__init__(level=level)
        self.setLevel(level)
        self.__name_field = name

    def emit(self, record: LogRecord):
        time = dt.fromtimestamp(record.created).time()
        hr = time.hour
        minute = time.minute
        second = time.second
        ms = floor(time.microsecond * self.MILLISECOND)

        if ms < 10:
            ms *= 100
        elif ms < 100:
            ms *= 10


        t = f'{hr:02d}:{minute:02d}:{second:02d}.{ms:01.0f}'
        color = self.LEVEL_COLORS.get(record.levelname, ('blue',))
        rec = f'[{t}][{record.levelname[0]}][{self.__name_field}] {record.msg}'
        sys.stdout.write(colored(f'{t}', 'white', attrs=['bold',]))
        sys.stdout.write(colored(f' | ', 'white'))
        sys.stdout.write(colored(f'{record.levelname[0:3]}', *color))
        sys.stdout.write(colored(f' | ', 'white'))
        sys.stdout.write(colored(f'{self.__name_field}', 'blue'))

        if os.environ.get('TERM_PROGRAM') != 'vscode':
            sys.stdout.write(colored(f' - ', 'white'))
            sys.stdout.write(colored(f'{record.lineno}', 'red'))

        sys.stdout.write(colored(f' | ', 'white'))
        sys.stdout.write(colored(f'{record.msg}', 'white'))
        sys.stdout.write(colored(f'\n', 'white'))
        sys.stdout.write('\n')

        if os.environ.get('TERM_PROGRAM') == 'vscode':
            sys.stdout.write(colored(f'{record.pathname}:{record.lineno}', 'red'))
            sys.stdout.write('\n')

        sys.stdout.write(colored('-' * shutil.get_terminal_size().columns, "blue"))
        sys.stdout.write('\n')
        sys.stdout.flush()


def test_handler():
    logger = getLogger(__name__)
    logger.addHandler(ColorizedConsole(name='Agent'))
    logger.setLevel(DEBUG)

    logger.debug('debug info')
    logger.info('Just info')
    logger.warning('Be careful!')
    logger.error('Hey! It\'s error')
    logger.critical('No SPACE LEFT!')
    print('\n\n')

if __name__ == '__main__':
    test_handler()
    pass
