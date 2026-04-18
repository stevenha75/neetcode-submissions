class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        maxsofar = 0

        for n in nums:
            maxsofar += n

            global_max = max(global_max, maxsofar)

            if maxsofar < 0:
                maxsofar = 0 

        return global_max 