# my solution
def count_largest_group(n: int) -> int:
    groups = {}
    max_val = 0
    max_val_count = 0
    for i in range(1, n + 1):
        val = sum([int(d) for d in str(i)])
        groups[val] = groups.get(val, 0) + 1
        v = groups[val]
        if v > max_val:
            max_val = v
            max_val_count = 1

        elif v == max_val:
            max_val_count += 1

    return max_val_count


# GhatGPT solution
def count_largest_group(n: int) -> int:
    groups = {}

    for num in range(1, n + 1):
        s = sum(int(d) for d in str(num))
        groups[s] = groups.get(s, 0) + 1

    max_size = max(groups.values())

    return sum(1 for size in groups.values() if size == max_size)
