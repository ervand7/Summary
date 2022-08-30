# An example of logger-hook
import logging
import os

import requests

log_format = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"

logging.basicConfig(
    format=log_format,
    filemode='a',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    # filename=os.getcwd() + '/log.log',  # if uncomment, output will be sent to file
)

for i in range(10):
    requests.get('http://httpbin.org/get?foo=bar&baz=python')
