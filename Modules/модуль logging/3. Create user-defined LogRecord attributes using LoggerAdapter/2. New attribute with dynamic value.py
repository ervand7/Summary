import logging


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('id', self.extra['id'])
        return '[%s] %s' % (my_context, msg), kwargs


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger = CustomAdapter(logger, {"id": None})

logger.info('ID is provided', id='1234')
logger.info('ID is provided', id='5678')
logger.info('Missing ID information')

# 2022-08-30 08:40:16,581 - [INFO] - __main__ - (2. New attribute with dynamic value.py).<module>(18) - [1234] ID is provided
# 2022-08-30 08:40:16,581 - [INFO] - __main__ - (2. New attribute with dynamic value.py).<module>(19) - [5678] ID is provided
# 2022-08-30 08:40:16,581 - [INFO] - __main__ - (2. New attribute with dynamic value.py).<module>(20) - [None] Missing ID information
