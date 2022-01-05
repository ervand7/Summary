import os
from pprint import pprint

import requests


class MyRange:

    def __init__(self, start: int, end: int):
        self.start = start - 1
        self.end = end

    def __iter__(self):  # without this __iter__(self) it will be TypeError: 'MyRange' object is not iterable
        return self

    def __next__(self):
        """
        Эмулируем то, как под капотом работает цикл for
        Благодаря raise StopIteration у нас итерация остановится
        на элементе end - 1.
        """
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start


for i in MyRange(1, 10):
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
