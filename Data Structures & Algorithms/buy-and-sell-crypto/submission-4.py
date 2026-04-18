class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 # init window; L = buy, R = sell
        res = 0

        while R < len(prices):
            res = max(res, prices[R] - prices[L])

            if prices[R] < prices[L]:
                L = R
            R += 1

        return res

        