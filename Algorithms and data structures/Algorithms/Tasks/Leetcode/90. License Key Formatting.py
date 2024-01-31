# my solution
def license_key_formatting(s: str, k: int) -> str:
    result = ""
    counter = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "-":
            result += s[i].upper()
            counter += 1

        if counter == k:
            counter = 0
            result += "-"

    while result:
        if result[-1] == "-":
            result = result[:-1]
        else:
            break
    return result[-1::-1]
