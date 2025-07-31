# my solution
def frequency_sort(s: str) -> str:
    h = {}
    for i in s:
        h[i] = h.get(i, 0) + 1

    s_sorted = sorted(h.items(), key=lambda x: x[1], reverse=True)
    result = []
    for val, count in s_sorted:
        result.extend([val] * count)

    return "".join(result)
