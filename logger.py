import logging
from handlers.elk_handler import ELKHandler
from  handlers.colorized_console import ColorizedConsole
from logging import getLogger, Handler, DEBUG, ERROR, LogRecord


logger = logging.getLogger('agent_data')
logger.setLevel(DEBUG)
logger.addHandler(ELKHandler(index='agent_data'))
logger.info("WORKING ON LOGGER")
