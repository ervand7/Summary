# O(n^2)
# Здесь на каждом шаге самое маленькое значение падает вниз

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubble_sort([999, -3, 5, 0, -8, 1, 10, -177]))  # [-177, -8, -3, 0, 1, 5, 10, 999]
