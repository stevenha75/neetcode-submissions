class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # efficient solution? 
        # sliding window approach

        # 10 1 5 6 7 1 

        min_price = float('inf')

        max_profit = 0

        # one pass approach
        for price in prices:
            if price < min_price:
                min_price = price # save the min_price

            profit = price - min_price

            # update max_profit
            if profit > max_profit:
                max_profit = profit
    
        return max_profit



