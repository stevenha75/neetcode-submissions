class Solution:
    def findMin(self, nums: List[int]) -> int:
        # log(n) -> binary search
        # how can we adapt binary search to this situation?
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # base case
            if nums[l] < nums[r]:
                # we are looking at a sorted portion
                res = min(res, nums[l])
                break
            
            # check middle
            m = (l + r) // 2
            res = min(res, nums[m])

            # -> continue
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1 
            
        return res 


