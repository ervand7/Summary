import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('hello world')

# 2022-08-30 22:07:44,643 root         DEBUG    hello world
