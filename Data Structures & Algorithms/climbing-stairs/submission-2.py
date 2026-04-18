class Solution:
    def climbStairs(self, n: int) -> int:
        # saving work w/ hashmap
        memo = {}

        # returns # of paths from cur step
        def dfs(step):
            # base cases
            if step == n:
                return 1
            if step > n:
                return 0 
            if step in memo:
                return memo[step]

            memo[step] = dfs(step + 1) + dfs(step + 2)
            return memo[step]
            

        return dfs(0)