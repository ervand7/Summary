def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False


containsNearbyDuplicate([1, 2, 3, 1], 3)
