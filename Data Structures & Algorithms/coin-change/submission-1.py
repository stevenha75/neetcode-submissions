class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # init dp 
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # fill dp 
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] < amount + 1 else -1 