from typing import List


# my solution
def summary_ranges(self, nums: List[int]) -> List[str]:
    if len(nums) == 1:
        return [str(nums[0])]

    result = []
    start = 0
    first = True
    for i in range(1, len(nums)):
        if first is True:
            start = nums[i - 1]
            first = False

        if nums[i] - nums[i - 1] > 1:
            diapason = f"{start}->{nums[i - 1]}" if nums[i - 1] - start != 0 else str(start)
            result.append(diapason)
            first = True
            start = nums[i]

        if i == len(nums) - 1:
            diapason = f"{start}->{nums[i]}" if nums[i] - start != 0 else str(start)
            result.append(diapason)

    return result
