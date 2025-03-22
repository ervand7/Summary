# my solution
def convert(s: str, num_rows: int) -> str:
    h = {}
    pointer = 1
    moving_down = True
    for letter in s:
        if h.get(pointer) is None:
            h[pointer] = letter
        else:
            h[pointer] += letter

        if pointer == num_rows:
            moving_down = False
        if pointer == 1:
            moving_down = True

        if moving_down is True:
            pointer += 1
        else:
            pointer -= 1

    return "".join(h.values())
