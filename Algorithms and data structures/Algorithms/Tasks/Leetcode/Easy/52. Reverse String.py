from typing import List


# my solution
def reverse_string(s: List[str]) -> None:
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
