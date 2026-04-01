'''
Colorized console log handler
'''
import sys
from datetime import datetime as dt
from math import floor
from termcolor import colored
from logging import getLogger, Handler, DEBUG, ERROR, LogRecord
SPACE_SYMBOL = ' '


class ColorizedConsole(Handler):
    '''
    Colorized console log handler
    '''
    MILLISECOND = 0.001
    LEVEL_COLORS = {
        'DEBUG': ('yellow', ['dark', 'blink']),
        'INFO': ('green', ['dark']),
        'WARNING': ('blue', ['dark']),
        'ERROR': ('red', ['bold', 'underline']),
        'CRITICAL': ('yellow', 'on_black', ['bold', 'underline']),
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
        t = f'{hr:02d}:{minute:02d}:{second:02d}.{ms:01.0f}'
        color = self.LEVEL_COLORS.get(record.levelname, ('white',))
        rec = f'[{t}][{record.levelname}][{self.__name_field}] {record.msg}'
        sys.stdout.write(colored(rec, *color))
        sys.stdout.write('\n')
        sys.stdout.flush()


def test_handler():
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    logger.addHandler(ColorizedConsole(name='Agent'))

    logger.debug('debug info')
    logger.info('Just info')
    logger.warning('Be careful!')
    logger.error('Hey! It\'s error')
    logger.critical('No SPACE LEFT!')

if __name__ == '__main__':
    test_handler()
