import logging
import coloredlogs

logger = logging.getLogger('my_app')
coloredlogs.install(level='DEBUG', logger=logger)

logger.debug("Отладка")
logger.info("Инфо")
logger.warning("Внимание")
logger.error("Ошибка")
