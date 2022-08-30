import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger = logging.LoggerAdapter(logger, {"app": "test application"})
logger.info("Program starts")
logger.info("Program is over")

# 2022-08-30 08:36:47,822 - [INFO] - test application - __main__ - (example.py).<module>(10) - Program starts
# 2022-08-30 08:36:47,822 - [INFO] - test application - __main__ - (example.py).<module>(11) - Program is over
