def nth_ugly_number(n: int) -> int:
    ugly = [1]  # first ugly number is 1
    i2 = i3 = i5 = 0  # indexes for multiples of 2, 3, and 5

    while len(ugly) < n:
        # next candidates
        next2 = ugly[i2] * 2
        next3 = ugly[i3] * 3
        next5 = ugly[i5] * 5

        # pick the smallest next ugly number
        next_ugly = min(next2, next3, next5)
        ugly.append(next_ugly)

        # move the pointer(s) that produced this value
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1

    return ugly[-1]


print(nth_ugly_number(10))
