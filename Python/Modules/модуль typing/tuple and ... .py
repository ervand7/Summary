from typing import Tuple

# this construction says that we will have only values with type int in this tuple
elems: Tuple[int, ...]
elems = (1, "2")  # Expected type 'tuple[int, ...]', got 'tuple[int, str]' instead

a: Tuple[int]
a = (1, 1, 1, 1, 1)  # Expected type 'tuple[int]', got 'tuple[int, int, int, int, int]' instead
