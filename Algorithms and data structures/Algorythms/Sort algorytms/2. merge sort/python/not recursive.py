# In this example, only sorted lists can merge with each other
list_1 = [2, 8, 8, 16, 19]
list_2 = [3, 4, 5, 5, 10, 11, 12]


def merge_lists(a: list, b: list):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    result_list = []
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            result_list.append(a[i])
            i += 1
        else:
            result_list.append(b[j])
            j += 1
    while i < len_a:
        result_list.append(a[i])
        i += 1
    while j < len_b:
        result_list.append(b[j])
    return result_list


print(merge_lists(list_1, list_2))  # [2, 3, 4, 5, 5, 8, 8, 10, 11, 12, 16, 19]
