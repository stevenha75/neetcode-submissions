class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1:
            return nums[0]
        
        max_sum = float('-inf')
        # Bruteforce solution
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j + 1]))

        return max_sum