import logging
from logging.handlers import RotatingFileHandler


def create_rotating_log(path):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(path, maxBytes=20, backupCount=5)
    logger.addHandler(handler)

    for i in range(100):
        logger.info("This is test log line %s" % i)


if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)
