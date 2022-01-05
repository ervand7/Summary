import os
from pprint import pprint
from typing import Generator

import requests

"""
В этом примере мы через генератор построчно запишем html-файл.
"""


class Downloader:
    def __init__(self, url: str):
        self.response = requests.get(url, stream=True)
        self.response_lines: Generator = self.response.iter_lines()
        # self.response_lines = self.response.iter_content(chunk_size=1024) # or you can set specific size

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response_lines)


file_path = os.path.join(os.getcwd(), 'hebr.html')
with open(file_path, 'wb') as file:
    for line in Downloader('http://habr.com'):
        file.write(line)
