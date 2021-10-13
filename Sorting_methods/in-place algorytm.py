# Main article: https://www.geeksforgeeks.org/in-place-algorithm/
# This needs O(n) extra space and is an example of not-in-place algorithm.
# An Not in-place Python program to reverse an array
def reverse_array_not_in_place(array):
    """Function to reverse arr[] from start to end. Create a copy array and store reversed elements """
    len_array = len(array)
    reverse_list = len_array * [0]
    for i in range(0, len_array):
        reverse_list[len_array - i - 1] = array[i]  # - 1 here to avoid IndexError: list assignment index out of range
        # Now copy reversed
    for i in range(0, len_array):
        array[i] = reverse_list[i]  # elements back to arr[]
    return array


# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
# An in-place Python program to reverse an array
# This needs O(1) extra space for exchanging elements and is an example of in-place algorithm.
def reverse_array_in_place(array):
    """Function to reverse arr[] from start to end"""
    len_array = len(array)
    for i in range(0, len_array // 2):
        array[i], array[len_array - i - 1] = array[len_array - i - 1], array[i]
    return array


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(reverse_array_not_in_place(arr))
    print(reverse_array_in_place(arr2))
