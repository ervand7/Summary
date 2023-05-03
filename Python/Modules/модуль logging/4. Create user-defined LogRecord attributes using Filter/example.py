import logging


class CustomFilter(logging.Filter):
    COLOR = {
        "DEBUG": "GREEN",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "RED",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - [%(color)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger.addFilter(CustomFilter())

logger.debug("debug message, color is green")
logger.info("info message, color is green")
logger.warning("warning message, color is yellow")
logger.error("error message, color is red")
logger.critical("critical message, color is red")

# 2022-08-30 08:48:13,605 - [DEBUG] - [GREEN] - __main__ - (example.py).<module>(26) - debug message, color is green
# 2022-08-30 08:48:13,606 - [INFO] - [GREEN] - __main__ - (example.py).<module>(27) - info message, color is green
# 2022-08-30 08:48:13,606 - [WARNING] - [YELLOW] - __main__ - (example.py).<module>(28) - warning message, color is yellow
# 2022-08-30 08:48:13,606 - [ERROR] - [RED] - __main__ - (example.py).<module>(29) - error message, color is red
# 2022-08-30 08:48:13,606 - [CRITICAL] - [RED] - __main__ - (example.py).<module>(30) - critical message, color is red
