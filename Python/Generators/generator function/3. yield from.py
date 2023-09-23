import os
import sys

import requests

# используем response.iter_lines() чтобы не забивать в память весть ответ


def download_url(url: str):
    response = requests.get(url, stream=True)
    print(sys.getsizeof(response.iter_lines()))  # 112
    yield from response.iter_lines()


file_path = os.path.join(os.getcwd(), 'habr.html')
with open(file_path, 'wb') as file:
    for line in download_url('https://habr.com'):
        file.write(line)
