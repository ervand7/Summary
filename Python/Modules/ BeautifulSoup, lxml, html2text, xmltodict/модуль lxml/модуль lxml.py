# основная статья: https://lecturesnet.readthedocs.io/net/web.scraping/lxml.html
import requests
from lxml import html
import sys
from pathlib import Path
from urllib.parse import urljoin

response = requests.get('http://ya.ru')

# Преобразование тела документа в дерево элементов (DOM)
parsed_body = html.fromstring(response.text)

# Выполнение xpath в дереве элементов
print(parsed_body.xpath('//title/text()')[0])  # Получить title страницы
print(parsed_body.xpath('//a/@href'))  # Получить аттрибут href для всех ссылок

response = requests.get('http://imgur.com/')
parsed_body = html.fromstring(response.text)

# Парсим ссылки с картинками при помощи XPath
images = parsed_body.xpath('//img/@src')
if not images:
    sys.exit("images Not Found")

# Конвертирование всех относительных ссылок в абсолютные
images = [
    urljoin(response.url, url)
    for url in images
]
print('Found {} images'.format(len(images)))
# Скачиваем только первые 10
for url in images[0:10]:
    r = requests.get(url)
    target = Path(
        '/Users/USER/Desktop/Ерванд. мусор/суперская/{}'.format(
            url.split('/')[-1]  # file name from URL
        )
    )
    target.write_bytes(r.content)