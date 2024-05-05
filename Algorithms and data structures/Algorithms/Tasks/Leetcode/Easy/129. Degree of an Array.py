from typing import List


# my solution
def find_shortest_sub_array(nums: List[int]) -> int:
    h = {}
    max_count = 0
    for i in range(len(nums)):
        if nums[i] not in h:
            h[nums[i]] = {"count": 1, "start": i, "end": i}
        else:
            h[nums[i]]["count"] += 1
            h[nums[i]]["end"] = i

        max_count = max(max_count, h[nums[i]]["count"])

    result = float("inf")
    for k, v in h.items():
        if v["count"] == max_count:
            diff = v["end"] - v["start"]
            if diff < result:
                result = diff

    return result + 1
