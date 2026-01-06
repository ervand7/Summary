from typing import List


def check_arithmetic_subarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    result = []

    def is_arithmetic(arr: List[int]) -> bool:
        arr.sort()
        first_distance = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != first_distance:
                return False

        return True

    for i in range(len(l)):
        start, stop = l[i], r[i]
        sub_arr = nums[start:stop + 1]
        result.append(is_arithmetic(sub_arr))

    return result


# ChatGPT solution
def check_arithmetic_subarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    ans = []

    for i in range(len(l)):
        sub = nums[l[i]:r[i] + 1]
        mn, mx = min(sub), max(sub)
        n = len(sub)

        if (mx - mn) % (n - 1) != 0:
            ans.append(False)
            continue

        d = (mx - mn) // (n - 1)
        seen = set(sub)

        ok = True
        for k in range(n):
            if mn + k * d not in seen:
                ok = False
                break

        ans.append(ok)

    return ans


print(check_arithmetic_subarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
