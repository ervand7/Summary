def max_length_between_equal_characters(s: str) -> int:
    result = 0

    first_occurrence = {}
    for idx, i in enumerate(s):
        if i not in first_occurrence:
            first_occurrence[i] = idx
        else:
            result = max(result, idx - first_occurrence[i])

    return result - 1
