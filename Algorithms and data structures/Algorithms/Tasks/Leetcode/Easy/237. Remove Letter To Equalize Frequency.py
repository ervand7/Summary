# my solution
def equal_frequency(word: str) -> bool:
    len_word = len(word)

    if len(set(word)) == 1:
        return True

    if len_word - len(set(word)) == 1:
        return True

    if len_word == len(set(word)):
        return True

    h = {}
    for i in word:
        h[i] = h.get(i, 0) + 1

    values = list(h.values())

    if len(h) == 2 and 1 in values:
        return True

    if len(h) == 2 and abs(values[0] - values[1]) == 1:
        return True

    if len(set(values)) > 2:
        return False

    if len(values) > 2 and values.count(max(values)) > values.count(min(values)):
        if min(values) == 1:
            return True
        return False

    if len(set(values)) > 2:
        return False

    values.sort()
    if values.count(values[0]) > 1 and values.count(values[-1]) > 1:
        return False

    if len(set(values)) == 1 and values[0] != 1:
        return False

    for i in range(1, len(values)):
        if abs(values[i] - values[i - 1]) > 1:
            return False

    return True


# ChatGPT solution
def equal_frequency(word: str) -> bool:
    # Manual letter-to-index mapping
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index_map = {char: i for i, char in enumerate(alphabet)}

    freq = [0] * 26  # Frequency array

    for ch in word:
        freq[index_map[ch]] += 1

    for i in range(26):
        if freq[i] == 0:
            continue

        # Remove one occurrence
        freq[i] -= 1

        # Gather all non-zero frequencies
        current = []
        for f in freq:
            if f > 0:
                current.append(f)

        # Check if all are equal
        if len(set(current)) == 1:
            return True

        # Restore frequency
        freq[i] += 1

    return False


print(equal_frequency("abbcccfff"))
