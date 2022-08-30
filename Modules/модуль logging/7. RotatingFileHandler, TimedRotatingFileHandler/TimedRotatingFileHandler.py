import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    "timed_test.log", when="s", interval=1, backupCount=5
)
logger.addHandler(handler)
for i in range(6):
    logger.info(i)
    time.sleep(1)
