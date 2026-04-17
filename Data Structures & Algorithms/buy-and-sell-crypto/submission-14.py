class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer aproach
        L, R = 0, 0 
        maxP = 0 

        while R < len(prices): # in bounds
            maxP = max(maxP, prices[R] - prices[L])

            if prices[R] < prices[L]:
                L = R 
            R += 1 

        return maxP