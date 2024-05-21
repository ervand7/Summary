# my solution (slow)
def backspace_compare(s: str, t: str) -> bool:
    def make_result_string(s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == "#":
                if i == 0:
                    if i + 1 < len(s):
                        s = s[1:]
                    else:
                        return ""
                elif i == 1:
                    if i + 1 < len(s):
                        flag = False
                        val = 0
                        if s[i + 1] == "#":
                            val = i - 1
                            flag = True
                        s = s[2:]
                        if flag:
                            i = val
                    else:
                        return ""
                elif i >= 2:
                    if i + 1 < len(s):
                        flag = False
                        val = 0
                        if s[i + 1] == "#":
                            val = i - 1
                            flag = True
                        s = s[:i - 1] + s[i + 1:]
                        if flag:
                            i = val

                    else:
                        return s[:i - 1]

            else:
                i += 1

        return s

    first = make_result_string(s)
    second = make_result_string(t)
    return first == second


# ChatGPT solution
def backspace_compare(s: str, t: str) -> bool:
    def build_final_string(s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return build_final_string(s) == build_final_string(t)
