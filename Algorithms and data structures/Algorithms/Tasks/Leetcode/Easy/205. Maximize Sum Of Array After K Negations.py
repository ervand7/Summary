# ChatGPT solution
def largest_sum_after_k_negations(nums, k):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0 < k:
            nums[i] = -nums[i]
            k -= 1

    nums.sort()
    if k % 2 == 1:
        nums[0] = -nums[0]

    return sum(nums)


largest_sum_after_k_negations([-8, 3, -5, -3, -5, -2], 6)
