class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L, R = 0, 0
        global_max = float('-inf')
        maxsofar = 0

        while L <= R and R < len(nums):
            maxsofar += nums[R]
            global_max = max(global_max, maxsofar)

            if maxsofar < 0:
                R = R + 1
                L = R    
                maxsofar = 0            
                continue 

            R += 1

        return global_max 


