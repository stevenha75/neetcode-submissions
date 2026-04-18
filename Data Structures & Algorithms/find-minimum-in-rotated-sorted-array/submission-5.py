class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search coln
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # base case (we found a sorted chunk)
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # search right
                l = mid + 1
            else:
                # search left
                r = mid - 1

        return res 