def majorityElement(nums: List[int]) -> int:
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1

    max_value = max(dic.values())
    for key, value in dic.items():
        if value == max_value:
            return key
