import os
from typing import Iterator

import requests


# В этом примере мы через генератор response.iter_lines() построчно запишем html-файл


class Downloader:
    def __init__(self, url: str):
        self.response = requests.get(url, stream=True)
        self.response_lines: Iterator = self.response.iter_lines()
        # self.response_lines = self.response.iter_content(chunk_size=1024) # or you can set specific size

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response_lines)


file_path = os.path.join(os.getcwd(), 'habr.html')
with open(file_path, 'wb') as file:
    for line in Downloader('https://habr.com'):
        file.write(line)
