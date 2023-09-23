from pprint import pprint


def my_range(start, end):
    while start < end:
        yield start
        start += 1


rng = my_range(1, 10)
pprint(rng.__dir__())  # here we can see, that there are methods __iter__ and __next__
for i in rng:
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9

