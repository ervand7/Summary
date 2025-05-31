from typing import List


# my solution
def find_x_sum(nums: List[int], k: int, x: int) -> List[int]:
    h = {}
    result = []
    for i in range(0, len(nums) - k + 1):
        if i == 0:
            for item in range(k):
                h[nums[item]] = h.get(nums[item], 0) + 1
        else:
            h[nums[i - 1]] -= 1
            h[nums[i + k - 1]] = h.get(nums[i + k - 1], 0) + 1

        h_sorted = sorted(h.items(), key=lambda x: (x[1], x[0]), reverse=True)
        result.append(sum([k * v for k, v in h_sorted[:x]]))

    return result


print(find_x_sum(nums=[1, 2, 2, 3, 4, 2, 3], k=6, x=2))
