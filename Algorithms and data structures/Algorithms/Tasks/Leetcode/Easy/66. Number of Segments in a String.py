# my solution
def count_segments(s: str) -> int:
    pointer = 0
    flag = True
    for i in range(len(s)):
        if s[i] != " ":
            if flag is True:
                pointer += 1
                flag = False
        else:
            flag = True

    return pointer
