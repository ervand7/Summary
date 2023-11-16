# O(n^2)
# Здесь на каждом шаге всплывает вверх самое большое число

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort([999, -3, 5, 0, -8, 1, 10, -177]))  # [-177, -8, -3, 0, 1, 5, 10, 999]
