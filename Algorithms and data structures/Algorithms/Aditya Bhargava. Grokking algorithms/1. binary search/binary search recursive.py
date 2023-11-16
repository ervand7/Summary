# O(log n)
def binary_search_recursive(array, item, low=0, high=0):
    if high < low:
        return None

    if high == 0:
        high = len(array) - 1

    mid = (low + high) // 2
    guess = array[mid]
    if guess == item:
        return mid
    if item < guess:
        return binary_search_recursive(array, item, low=low, high=mid - 1)
    else:
        return binary_search_recursive(array, item, low=mid + 1, high=high)


my_list = [1, 2, 123, 234, 345, 456, 56777, 99999999, ]
print(binary_search_recursive(my_list, 56777))  # 4
