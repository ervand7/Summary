# ChatGPT solution
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> str:
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    result = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(result):
            result = odd_palindrome

        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(result):
            result = even_palindrome

    return result
