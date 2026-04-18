class Solution:
    def findMin(self, nums: List[int]) -> int:
        # want o(logn) soln -> think binary search
        l, r = 0, len(nums) - 1 # pointers for bs

        res = nums[0]
        while l <= r:
            # once we find a sorted portion ->
            # check leftmost item (base case)
            if nums[l] <= nums[r]:
                # we are looking at a sorted part
                res = min(res, nums[l])
                break 
            
            # check middle
            m = (l + r) // 2
            res = min(res, nums[m])

            # move pointers
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1 
        
        return res

