# Given a string s consisting of words and spaces, return the length of the last
# word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# solution using build-in func
def length_of_last_word(s: str) -> int:
    return len(s.rsplit()[-1])


print(length_of_last_word("Hello world"))


# my first solution
def length_of_last_word(s: str) -> int:
    result = 0
    pointer = 0
    for i in s:
        if i != " ":
            pointer += 1
            result = pointer
        elif i == " " and pointer != 0:
            result = pointer
            pointer = 0

    return result


print(length_of_last_word("luffy is still joyboy"))


# my first solution: search from the end
def length_of_last_word(s: str) -> int:
    flag = False
    pointer = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            pointer += 1
            flag = True
        if flag is True and s[i] == " ":
            return pointer
    return pointer


print(length_of_last_word("luffy is still joyboy"))
