# my solution
def can_construct(ransom_note: str, magazine: str) -> bool:
    h1, h2 = {}, {}
    for i in ransom_note:
        h1[i] = h1.get(i, 0) + 1

    for i in magazine:
        h2[i] = h2.get(i, 0) + 1

    for k, v in h1.items():
        if h2.get(k, -1) < v:
            return False

    return True


# ChatGPT solution
def can_construct(ransom_note: str, magazine: str) -> bool:
    letter_counts = {}

    # Count the occurrences of each letter in magazine
    for letter in magazine:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Check if the letters in ransomNote can be constructed from magazine
    for letter in ransom_note:
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False
        letter_counts[letter] -= 1

    return True
