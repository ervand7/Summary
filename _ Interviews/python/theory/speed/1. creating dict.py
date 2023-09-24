from time import time

COUNT = 20_000_000

start = time()
for i in range(COUNT):
    dct = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "a5": 5, "a6": 6, "a7": 7, "a8": 8, "a9": 9, "a10": 10}
end = time()
print(end - start)  # 6.086091995239258

start = time()
for i in range(COUNT):
    dct = dict(a1=1, a2=2, a3=3, a4=4, a5=5, a6=6, a7=7, a8=8, a9=9, a10=10)
end = time()
print(end - start)  # 7.996924877166748
