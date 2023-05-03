import os
from pprint import pprint

import requests

"""
Упрощеный вариант example_1.
"""


# Now to simplify above shown example we can use generator expression:
def my_range(start, end):
    while start < end:
        yield start
        start += 1


rng = my_range(1, 10)
pprint(rng.__dir__())  # here we can see, that there are methods __iter__ and __next__
for i in rng:
    print(i)
