import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
logging.config.dictConfig(LOGGING_CONFIG)

if __name__ == "__main__":
    log = logging.getLogger(__name__)
    log.info("hello world")

# 2022-08-30 22:05:26,275 [INFO] __main__: hello world
