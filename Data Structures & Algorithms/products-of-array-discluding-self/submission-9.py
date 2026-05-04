class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # forward pass
        left_product = 1 
        for i in range(1, len(nums)):
            left_product *= nums[i - 1]
            res[i] = left_product
        
        right_product = 1 
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            res[i] *= right_product
        
        return res