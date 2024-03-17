# my solution
def reverse_str(s: str, k: int) -> str:
    if len(s) < k:
        return s[::-1]

    result = ""
    pointer = 0
    while pointer <= len(s):
        data = list(s[pointer: pointer + k])
        for i in range(len(data) // 2):
            data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
        result += "".join(data)
        result += s[pointer + k:pointer + k * 2]
        pointer += k * 2

    return result


# ChatGPT solution
def reverse_str(s: str, k: int) -> str:
    s_list = list(s)
    for i in range(0, len(s), 2 * k):
        s_list[i:i + k] = reversed(s_list[i:i + k])
    return ''.join(s_list)
