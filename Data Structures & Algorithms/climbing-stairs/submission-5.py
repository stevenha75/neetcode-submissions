class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1], memo[2] = 1, 2

        def dfs(n):
            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)