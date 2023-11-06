from functools import lru_cache


def climbStairs(n: int) -> int:
    @lru_cache
    def dp(number):
        if number in (1, 2):
            return number
        else:
            return dp(number - 1) + dp(number - 2)

    return dp(n)


print(climbStairs(475))
# 1344719667586153181419716641724567886890850696275767987106294472017884974410332069524504824747437757
