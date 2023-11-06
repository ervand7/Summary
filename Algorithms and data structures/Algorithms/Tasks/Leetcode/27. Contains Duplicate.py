def containsDuplicate(nums: List[int]) -> bool:
    dct = {}
    for i in nums:
        dct[i] = dct.get(i, 0) + 1
    for key, value in dct.items():
        if value >= 2:
            return True
    return False
