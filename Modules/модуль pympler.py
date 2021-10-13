# не совсем понятный туториал: https://pympler.readthedocs.io/en/latest/tutorials/muppy_tutorial.html
from pympler import asizeof

obj = [1, 2, (1, 2), [1, 2], 'text']
print(asizeof.asizeof(obj))  # 344

print(asizeof.asized(obj, detail=1).format())
# [1, 2, (1, 2), [1, 2], 'text'] size=344 flat=96
#     [1, 2] size=72 flat=72
#     (1, 2) size=56 flat=56
#     'text' size=56 flat=56
#     1 size=32 flat=32
#     2 size=32 flat=32
