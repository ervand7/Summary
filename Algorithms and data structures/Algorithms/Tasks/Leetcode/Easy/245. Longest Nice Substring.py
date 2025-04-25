# my solution
def longest_nice_substring(s: str) -> str:
    max_length = 0
    result = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            arr = s[i:j + 1]
            len_arr = len(arr)
            if len_arr > 1:
                set_arr = set(arr)
                cond = all([i.swapcase() in set_arr for i in set_arr])
                if cond and len_arr > max_length:
                    max_length = len_arr
                    result = arr

    return result


# ChatGPT solution
def longest_nice_substring(s: str) -> str:
    def helper(sub: str) -> str:
        if len(sub) < 2:
            return ""

        charset = set(sub)
        for i, c in enumerate(sub):
            if c.swapcase() not in charset:
                # Split and recurse
                left = helper(sub[:i])
                right = helper(sub[i + 1:])
                return left if len(left) >= len(right) else right

        return sub

    return helper(s)
