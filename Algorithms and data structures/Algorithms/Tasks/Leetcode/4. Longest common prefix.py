from typing import List


# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# my solution
# O(m * n)
# The time complexity of this solution is O(m * n), where 'm' is the length of the
# smallest string and 'n' is the number of strings in the list.
def find_longest_common_prefix(strs: List[str]) -> str:
    pointer = 0
    smallest = min(strs)
    for i in range(len(smallest)):
        unique = set()
        for string in strs:
            unique.add(string[i])
        if len(unique) == 1:
            pointer += 1
        else:
            break

    return smallest[:pointer]


print(find_longest_common_prefix(["qwerty", "dfgfdsg", "qwerty3"]))
