import os
from pprint import pprint

import requests

"""
Упрощеный вариант example_2.
"""


def download_url(url: str):
    response = requests.get(url, stream=True)
    for my_line in response.iter_lines():
        yield my_line


file_path = os.path.join(os.getcwd(), 'hebr.html')
with open(file_path, 'wb') as file:
    for line in download_url('http://habr.com'):
        file.write(line)
