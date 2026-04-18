class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 # init window; L = buy, R = sell
        res = 0

        while R < len(prices):
            # only calc profit if it's positive
            if prices[L] < prices[R]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R # buy at the cheapest price
            R += 1 # time always moves forward

        return res




        