# O(n^2)
from datetime import datetime


def bubble_sort(array):
    my_list = array
    counter = 0
    for run in range(len(my_list) - 1):
        for i in range(len(my_list) - 1 - run):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                counter += 1
    return print(f'sorted list: {my_list}\namount of replacements is {counter}.')


if __name__ == '__main__':
    start = datetime.now()
    bubble_sort([5, 7, 4, 3, 8, 2])  # [5, 4, 3, 7, 2, 8] the first bubble floated
    end = datetime.now() - start
    print(f'the duration is {end}')
