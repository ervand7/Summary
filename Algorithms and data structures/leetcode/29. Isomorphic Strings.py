def isIsomorphic(s: str, t: str) -> bool:
    return [s.index(i) for i in s] == [t.index(i) for i in t]
