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
        'DEBUG': ('green', ['dark', 'bold']),
        'INFO': ('white', ['dark', 'bold']),
        'WARNING': ('red', ['dark', 'bold']),
        'ERROR': ('yellow', 'on_black', ['dark', 'bold']),
        'CRITICAL': ('yellow', 'on_black', ['dark', 'bold']),
    }

    def __init__(self, level: int=DEBUG, name: str='', line_divider='*') -> None:
        super().__init__(level=level)
        self.setLevel(level)
        self.__name_field = name
        self.__line_divider = line_divider
        self.__max_levelname_len = max([len(levelname) for levelname in self.LEVEL_COLORS])

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
        sys.stdout.write(colored(f'{t}', 'green', attrs=['bold',]))
        sys.stdout.write(colored(f' |', 'white'))
        sys.stdout.write(colored(f'{record.levelname}' + " " * (self.__max_levelname_len - len(record.levelname)), *color))
        sys.stdout.write(colored(f'| ', 'white'))
        sys.stdout.write(colored(f'[{self.__name_field}]', 'black', "on_yellow", attrs=["bold",]))

        if os.environ.get('TERM_PROGRAM') != 'vscode':
            sys.stdout.write(colored(f' - ', 'white'))
            sys.stdout.write(colored(f'{record.lineno}', 'red'))

        sys.stdout.write(colored(f' | ', 'white'))
        sys.stdout.write(colored(f'{record.msg}', 'white'))
        sys.stdout.write('\n')

        if os.environ.get('TERM_PROGRAM') == 'vscode':
            sys.stdout.write('\n')
            sys.stdout.write(colored(f'{record.pathname}:{record.lineno}', 'red'))
            sys.stdout.write('\n')

        if self.__line_divider:
            sys.stdout.write(
                colored(
                    self.__line_divider * shutil.get_terminal_size().columns,
                    "blue"
                )
            )

        sys.stdout.write('\n')
        sys.stdout.flush()


def test_handler():
    logger = getLogger(__name__)
    logger.addHandler(ColorizedConsole(name='Agent', line_divider='*'))
    logger.setLevel(DEBUG)

    logger.debug('debug info')
    logger.info('Just info')
    logger.warning('Be careful!')
    logger.error('Hey! It\'s error')
    logger.critical('No SPACE LEFT!')
    logger.exception('No network!')
    print('\n\n')

if __name__ == '__main__':
    test_handler()
    pass
