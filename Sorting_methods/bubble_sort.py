from datetime import datetime


def bubble_sort(array):
    my_list = array
    counter = 0  # lat's count the amount of replacements, which we made to the first bubble floats
    for run in range(len(my_list) - 1):  # we will make amount of rounds one less then len(my_list)
        for i in range(len(my_list) - 1 - run):  # since we are comparing adjacent elements, we write - 1 because
            # we can not compare the last element of my_list with next element. And after -1 we write - run
            # because we don't want to make extra work and compare already sorted last
            # elements which increase with every iteration. - run is number, which increase with every iteration.
            # At first iteration we make  - 1 - 0, at second - 1 - 1, at third - 1 - 2 etc.
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                counter += 1
    return print(f'sorted list: {my_list}\namount of replacements is {counter}.')


if __name__ == '__main__':
    start = datetime.now()
    bubble_sort([5, 7, 4, 3, 8, 2])  # [5, 4, 3, 7, 2, 8] the first bubble floated
    end = datetime.now() - start
    print(f'the duration is {end}')



