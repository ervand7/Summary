# my solution
def singleNumber(nums: List[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i


def singleNumber2(nums: List[int]) -> int:
    dct = {}
    for i in nums:
        dct[i] = dct.get(i, 0) + 1
    for key, value in dct.items():
        if value == 1:
            return key
