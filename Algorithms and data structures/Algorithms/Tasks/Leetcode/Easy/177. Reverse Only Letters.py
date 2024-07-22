# my solution
def reverse_only_letters(s: str) -> str:
    s = list(s)
    pointer = len(s) - 1
    for i in range(len(s)):
        if s[i].isalpha():
            while pointer > i:
                if s[pointer].isalpha():
                    s[i], s[pointer] = s[pointer], s[i]
                    pointer -= 1
                    break
                pointer -= 1

    return "".join(s)
