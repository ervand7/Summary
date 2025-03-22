# my solution
def max_number_of_balloons(text: str) -> int:
    h = {}
    for i in text:
        if i in {"b", "a", "l", "o", "n"}:
            h[i] = h.get(i, 0) + 1

    if len(h) < 5:
        return 0

    result = 0

    while True:
        if h["b"] >= 1 and h["a"] >= 1 and h["l"] >= 2 and h["o"] >= 2 and h["n"] >= 1:
            result += 1
            h["b"] -= 1
            h["a"] -= 1
            h["l"] -= 2
            h["o"] -= 2
            h["n"] -= 1
        else:
            return result
