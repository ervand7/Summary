def four_sum_count(nums1, nums2, nums3, nums4):
    h = {}
    for a in nums1:
        for b in nums2:
            s = a + b
            h[s] = h.get(s, 0) + 1

    count = 0
    for c in nums3:
        for d in nums4:
            target = -(c + d)
            if target in h:
                count += h[target]

    return count
