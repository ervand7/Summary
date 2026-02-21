from typing import List


def rearrange_array(nums: List[int]) -> List[int]:
    n = len(nums)
    look_positive = True
    for i in range(n):
        if look_positive:
            if nums[i] < 0:
                first_positive_idx = None
                first_positive_idx_val = None
                for j in range(i + 1, n):
                    if nums[j] >= 0:
                        first_positive_idx = j
                        first_positive_idx_val = nums[j]
                        break
                nums[i + 1:first_positive_idx + 1] = nums[i:first_positive_idx]
                nums[i] = first_positive_idx_val

            look_positive = False

        else:
            if nums[i] > 0:
                first_negative_idx = None
                first_negative_idx_val = None
                for j in range(i + 1, n):
                    if nums[j] < 0:
                        first_negative_idx = j
                        first_negative_idx_val = nums[j]
                        break
                nums[i + 1:first_negative_idx + 1] = nums[i:first_negative_idx]
                nums[i] = first_negative_idx_val

            look_positive = True

    return nums


# ChatGPT solution
def rearrange_array(nums: List[int]) -> List[int]:
    n = len(nums)
    look_positive = True

    for i in range(n):
        if look_positive:
            if nums[i] < 0:
                j = i + 1
                while j < n and nums[j] < 0:
                    j += 1

                # rotate right
                temp = nums[j]
                while j > i:
                    nums[j] = nums[j - 1]
                    j -= 1
                nums[i] = temp

            look_positive = False

        else:
            if nums[i] > 0:
                j = i + 1
                while j < n and nums[j] > 0:
                    j += 1

                # rotate right
                temp = nums[j]
                while j > i:
                    nums[j] = nums[j - 1]
                    j -= 1
                nums[i] = temp

            look_positive = True

    return nums


print(rearrange_array(nums=[3, 1, -2, -5, 2, -4]))
