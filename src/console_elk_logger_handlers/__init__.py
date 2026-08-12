from logging import getLogger, DEBUG
from .colorized_console import ColorizedConsole
from .elk_handler import ELKHandler


def get_common_loggers(
    name,
    elk_index='probe',
    elk_host='host.docker.internal',
    elk_port=9200,
    password='changeme',
    default_level=DEBUG
):
    LOGGER = getLogger(name=name)
    LOGGER.addHandler(ColorizedConsole(name=name))
    LOGGER.setLevel(default_level)
    LOGGER.addHandler(
        ELKHandler(
            index=elk_index,
            host=elk_host,
            port=elk_port,
            password=password
        )
    )
    return LOGGER

__all__ = ['ELKHandler', 'ColorizedConsole', 'get_common_loggers']
