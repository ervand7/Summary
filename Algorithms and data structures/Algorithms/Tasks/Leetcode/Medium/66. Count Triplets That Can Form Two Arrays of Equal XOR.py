def count_triplets(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        xor_value = 0
        for j in range(i, n):
            xor_value ^= arr[j]

            if xor_value == 0 and j > i:
                count += (j - i)

    return count
