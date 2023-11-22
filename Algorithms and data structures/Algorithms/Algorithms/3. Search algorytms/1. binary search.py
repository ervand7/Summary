# O(log n)

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))  # 4
