class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Looks like a decision tree problem
        # So a brute force method would be a recursion tree to cover all
        # cases

        # possible questions:
        # empty array?
        # max array size?
        # no solution?

        def backtrack(i, cur_sum):
            # base case
            if i == len(nums):
                return 1 if cur_sum == target else 0 
            
            # recursive case (building out recursion tree)
            return (
                backtrack(i + 1, cur_sum + nums[i]) + # adding case
                backtrack(i + 1, cur_sum - nums[i]) # subtraction acse
            )

            # i is like the level of the recursion tree 

        return backtrack(0, 0)