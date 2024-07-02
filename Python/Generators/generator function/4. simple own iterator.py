from pprint import pprint


def my_range(start, end):
    while start < end:
        yield start
        start += 1


result = my_range(1, 10)
pprint(result.__dir__())
# here we can see, that there are methods __iter__ and __next__
# if we did not claim the generator inside the my_range it wouldn't have them

for i in result:
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9

