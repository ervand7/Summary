def detect_capital_use(word: str) -> bool:
    return word.islower() or word.isupper() or (word.istitle() and word[1:] == word[1:].lower())
