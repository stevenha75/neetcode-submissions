class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # how can we improve a recursive function like this?
        # is there repeated work?
        # think -> memoization
        
        # creating a cache (saving solutions to subproblems)
        dp = {} # (i, cur_sum) -> # of ways

        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp: # check if it's already a soln
                return dp[(i, cur_sum)]
            
            # base case
            if i == len(nums):
                return 1 if cur_sum == target else 0 
            
            # recursive case (building out recursion tree)
            dp[(i, cur_sum)] = ( # save solution to sub problem
                backtrack(i + 1, cur_sum + nums[i]) + # adding case
                backtrack(i + 1, cur_sum - nums[i]) # subtraction acse
            )

            return dp[(i, cur_sum)] # returns final solution stored in the cache

            # i is like the level of the recursion tree 

        return backtrack(0, 0)