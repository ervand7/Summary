from datetime import datetime


def merge_two_lists(first_list, second_list):
    final_list = []
    i = j = 0
    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            final_list.append(first_list[i])
            i += 1
        else:
            final_list.append(second_list[j])
            j += 1
    # after this loop one list can reach end, but other one can remain with elements.
    # Which specifically of them - we don't know. So we ask: if i didn't reach the end of first_list, we append in
    # final_list all elements from first_list since index, which value equally i. And the same with j.
    if i < len(first_list):
        final_list += first_list[i:]
    if j < len(second_list):
        final_list += second_list[j:]
    return final_list


def merge_sort(array):
    if len(array) == 1:  # if there is only 1 element in our array, the array is default sorted. Also this in a
        # condition of exit from recursion
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])  # Thanks this there is recursion decay of lists and gather back to sort list
        right = merge_sort(array[middle:])
        return merge_two_lists(left, right)  # only remains to merge initially fragmented lists


if __name__ == '__main__':
    start = datetime.now()
    print(*merge_sort([7, 5, 2, 3, 9, 8, 6]))
    end = datetime.now() - start
    print(f'the duration is {end}')
