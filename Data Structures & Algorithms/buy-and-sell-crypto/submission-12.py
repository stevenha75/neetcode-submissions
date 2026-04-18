class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # defo the perfect window question 
        # what are the conditions?
        # move the pointer if we find a better 'buy' price
        res = 0
        L = 0
        R = L + 1

        while R < len(prices):
            profit = prices[R] - prices[L]
            res = max(profit, res)

            if prices[L] > prices[R]:
                L = R
            R += 1

        return res 