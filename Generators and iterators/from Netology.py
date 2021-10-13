import requests
import os
from pprint import pprint


class MyRange:

    def __init__(self, start: int, end: int):
        self.start = start - 1
        self.end = end

    def __iter__(self):  # without this __iter__(self) it will be TypeError: 'MyRange' object is not iterable
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start


# if __name__ == '__main__':
#     for i in MyRange(1, 10):
#         print(i)


# _________________________________________________________
class Downloader:
    def __init__(self, url: str):
        self.response = requests.get(url, stream=True)
        self.response_lines = self.response.iter_lines()
        # self.response_lines = self.response.iter_content(chunk_size=1024) # or you can set specific size

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response_lines)


# if __name__ == '__main__':
#     file_path = os.path.join(os.getcwd(), 'hebr.html')
#     with open(file_path, 'wb') as file:
#
#         for line in Downloader('http://habr.com'):
#             file.write(line)

# _________________________________________________________

# Now to simplify above shown example we can use generator expression:

def my_range(start, end):
    while start < end:
        yield start
        start += 1


s = my_range(1, 10)


# pprint(s.__dir__())  # here we can see, that there are methods __iter__ and __next__


# if __name__ == '__main__':
#     for i in my_range(1, 10):
#         print(i)

# _________________________________________________________
def download_url(url: str):
    response = requests.get(url, stream=True)
    for my_line in response.iter_lines():
        yield my_line

# if __name__ == '__main__':
#     file_path = os.path.join(os.getcwd(), 'habr.html')
#     with open(file_path, 'wb') as file:
#         for line in download_url('http://yandex.ru'):
#             file.write(line)
# _________________________________________________________
