def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')


def hammingWeight2(n):
    """
    :type n: int
    :rtype: int
    """
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c
