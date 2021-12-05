from itertools import zip_longest
from typing import Iterator

print(list(zip_longest('ABCD', 'xy', fillvalue='-')))


# [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]


# _________________________________________________________________


def group(iterable, n, fillvalue=None) -> Iterator:
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


print(list(group('ABCDEFG', 3, 'x')))
# [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]
