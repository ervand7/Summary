# my solution
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_table1 = {}
    hash_table2 = {}
    lst1 = []
    lst2 = []
    for i in range(len(s)):
        if hash_table1.get(s[i]) is None:
            hash_table1[s[i]] = i
            lst1.append(i)
        if hash_table2.get(t[i]) is None:
            hash_table2[t[i]] = i
            lst2.append(i)
        else:
            lst1.append(hash_table1[s[i]])
            lst2.append(hash_table2[t[i]])

        if lst1[-1] != lst2[-1]:
            return False

    return True


print(is_isomorphic("qwertyt", "asdfghg"))


# my old solution
def is_isomorphic(s: str, t: str) -> bool:
    return [s.index(i) for i in s] == [t.index(i) for i in t]


print(is_isomorphic("qwertyt", "asdfghg"))


# ChatGPT solution
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for i in range(len(s)):
        if mapping_s_to_t.get(s[i], t[i]) != t[i] \
                or mapping_t_to_s.get(t[i], s[i]) != s[i]:
            return False
        mapping_s_to_t[s[i]] = t[i]
        mapping_t_to_s[t[i]] = s[i]

    return True


print(is_isomorphic("qwertyt", "asdfghg"))
