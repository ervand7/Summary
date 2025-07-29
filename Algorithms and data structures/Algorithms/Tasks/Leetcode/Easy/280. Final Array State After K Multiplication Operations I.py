# my solution
def get_final_state(nums, k, multiplier):
    for _ in range(k):
        min_index = min((val, i) for i, val in enumerate(nums))[1]
        nums[min_index] *= multiplier
    return nums
