# O(n log n), в худшем случае O(n^2) в зависимости от выбора опорного элемента

def quick_sort(array):
    if len(array) <= 1:
        return array

    support_el = array[0]
    left = list(filter(lambda x: x < support_el, array))  # [5, 2, 3, 6]
    center = [i for i in array if i == support_el]  # [7]
    right = list(filter(lambda x: x > support_el, array))  # [9, 8]

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([7, 5, 2, 3, 9, 8, 6]))  # [2, 3, 5, 6, 7, 8, 9]
