# Dicts are compared by length and elements independent of they order

dct1 = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "a5": 5}
dct2 = {"a2": 2, "a1": 1, "a3": 3, "a4": 4, "a5": 5}
print(dct1 == dct2)  # True
