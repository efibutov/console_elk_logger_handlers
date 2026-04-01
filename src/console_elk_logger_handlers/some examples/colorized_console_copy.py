# import logging
# from termcolor import colored

# class ColoredFormatter(logging.Formatter):
#     COLORS = {
#         'DEBUG': 'cyan',
#         'INFO': 'green',
#         'WARNING': 'yellow',
#         'ERROR': 'red',
#         'CRITICAL': 'magenta',
#     }

#     def format(self, record):
#         levelname = record.levelname
#         if levelname in self.COLORS:
#             record.levelname = colored(levelname, self.COLORS[levelname])
#         return super().format(record)

# # Настройка логгера
# logger = logging.getLogger('my_app')
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler()
# handler.setFormatter(ColoredFormatter(
#     '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
#     datefmt='%H:%M:%S'
# ))
# logger.addHandler(handler)

# # Тесты
# logger.debug("Отладочная информация")
# logger.info("Всё работает")
# logger.warning("Что-то не так")
# logger.error("Ошибка!")
# logger.critical("Критическая ошибка!")


import logging
from termcolor import colored

class ColoredFormatter(logging.Formatter):
    # Цвета для уровней
    LEVEL_COLORS = {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'magenta',
    }

    # Цвета для полей
    FIELD_COLORS = {
        'asctime': 'grey',      # время
        'name': 'blue',         # имя логгера
        'message': 'white',     # сообщение
    }

    def format(self, record):
        # Сначала форматируем строку как обычно
        original_msg = super().format(record)

        # Разбиваем на части (время, уровень, имя, сообщение)
        # Формат: [время] [уровень] [имя] сообщение
        parts = original_msg.split('] ', 3)

        if len(parts) == 4:
            time_part = parts[0] + ']'
            level_part = parts[1] + ']'
            name_part = parts[2] + ']'
            message = parts[3]

            # Красим каждую часть
            time_part = colored(time_part, self.FIELD_COLORS.get('asctime', 'grey'))
            level_part = colored(level_part, self.LEVEL_COLORS.get(record.levelname, 'white'))
            name_part = colored(name_part, self.FIELD_COLORS.get('name', 'blue'))

            return f"{time_part} {level_part} {name_part} {message}"

        return original_msg


# Настройка
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter(
    '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt='%H:%M:%S'
))
logger.addHandler(handler)

# Тесты
logger.debug("Отладка")
logger.info("Инфо")
logger.warning("Внимание")
logger.error("Ошибка")