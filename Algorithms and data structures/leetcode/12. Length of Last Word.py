def lengthOfLastWord(s: str) -> int:
    return len(s.rsplit()[-1])
