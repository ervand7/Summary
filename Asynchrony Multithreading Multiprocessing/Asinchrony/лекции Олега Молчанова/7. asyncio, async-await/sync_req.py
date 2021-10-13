"""Здесь скачиваем картинки синхронным скриптом"""
from time import time

import requests


def get_file(url_address):
    response = requests.get(url_address, allow_redirects=True)
    return response


def write_file(response):
    # https://loremflickr.com/cache/resized/65535_51007696125_08cf597744_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(f'pictures/{filename}', mode='wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'
    for i in range(10):
        write_file(get_file(url))
    print(time() - t0)


if __name__ == '__main__':
    main()
