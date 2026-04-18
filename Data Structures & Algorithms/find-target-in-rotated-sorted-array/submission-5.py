class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # change bounds 
            if nums[m] >= nums[l]:
            # left side
                if target < nums[l] or target > nums[m]:
                    # if this is the case -> we must explore right side
                    l = m + 1
                else:
                    r = m - 1
            else:
            # right side
                if target < nums[m] or target > nums[r]:
                    # look left
                    r = m - 1
                else:
                    # look right
                    l = m + 1
        return -1 

