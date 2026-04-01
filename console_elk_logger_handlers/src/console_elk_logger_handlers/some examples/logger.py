import logging
from handlers.elk_handler import ELKHandler
from  handlers.colorized_console import ColorizedConsole
from logging import getLogger, Handler, DEBUG, ERROR, LogRecord

logger = getLogger('sandbox')
logger.setLevel(DEBUG)
logger.addHandler(ELKHandler(index='sandbox'))
logger.addHandler(ColorizedConsole(name='sandbox'))

logger.debug('Debug info')
logger.critical('Critical info')
