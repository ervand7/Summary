from functools import lru_cache


def climbStairs(n: int) -> int:
    @lru_cache
    def dp(number):
        if number <= 1:
            return number
        else:
            return dp(number - 1) + dp(number - 2)

    return dp(n)


print(climbStairs(475))
# 831082459908702935293955784701120993704369028200651613859972830080739980541065544674812034151699525
