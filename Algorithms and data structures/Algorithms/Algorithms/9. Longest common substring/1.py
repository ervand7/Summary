# dynamic programming

def longest_common_substring(str1, str2):
    # Create a matrix to store the length of common substrings
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Variables to store the length of the longest common substring and its ending position
    max_length = 0
    end_position = 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_position = i

    # Extract the longest common substring
    common_substring = str1[end_position - max_length: end_position]

    return common_substring


# Example usage:
str1 = "abcdeflkjbcdet"
str2 = "xbcdeyzjgrtbcdetiviv"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)  # bcdet
