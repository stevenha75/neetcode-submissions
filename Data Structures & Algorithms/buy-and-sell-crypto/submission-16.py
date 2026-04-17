class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer aproach
        L, R = 0, 1 
        maxP = 0 

        while R < len(prices): # in bounds
            buy, sell = prices[L], prices[R]
            maxP = max(maxP, sell - buy)

            if sell < buy:
                L = R 
            R += 1 

        return maxP