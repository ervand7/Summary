# одна из статей https://webdevblog.ru/logging-v-python/
# https://stackoverflow.com/questions/16337511/log-all-requests-from-the-python-requests-module
# https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module

# помимо всего прочего библиотека logging может вести себя как хук, перхватывающий http-запросы
import requests
import logging

logging.basicConfig(
    filename='/Users/USER/Desktop/Ерванд. мусор/Новая папка3/log.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)

for i in range(10):
    requests.get('http://httpbin.org/get?foo=bar&baz=python')
