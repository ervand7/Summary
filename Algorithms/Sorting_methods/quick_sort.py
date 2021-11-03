from datetime import datetime


def quick_sort(array):
    if len(array) <= 1:  # let's write a condition of exit from recursion
        return array

    support_el = array[0]  # as support element you can choose any element
    left = list(filter(lambda x: x < support_el, array))
    center = [i for i in array if i == support_el]  # we use list comprehension as alternative written above
    right = list(filter(lambda x: x > support_el, array))

    return quick_sort(left) + center + quick_sort(right)


if __name__ == '__main__':
    start = datetime.now()
    print(*quick_sort([7, 5, 2, 3, 9, 8, 6]))
    end = datetime.now() - start
    print(f'the duration is {end}')
