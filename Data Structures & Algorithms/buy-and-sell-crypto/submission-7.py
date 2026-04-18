class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 # init window; L = buy, R = sell
        res = 0

        while R < len(prices):
            # only update if profitable
            if prices[R] > prices[L]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R # update to cheaper price
            R += 1 # time always moves forward

        return res

        