class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            m = (l + r) // 2 

            # base case
            if nums[m] == target:
                return m

            # left side
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    # check right
                    l = m + 1 
                else: # in left
                    r = m - 1
            # right side 
            else:
                if target > nums[r] or target < nums[m]:
                    # check left
                    r = m - 1
                else: # in right
                    l = m + 1 
            
        return -1