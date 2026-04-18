class Solution:
    # recursion / dfs
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False # oddcase

        def dfs(i, target):
            # base cases 
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)

        return dfs(0, sum(nums) // 2)