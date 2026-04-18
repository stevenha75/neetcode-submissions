class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # turn nums into a set
        vals = set()

        for i in nums:
            vals.add(i)

        for i in range(len(nums) + 1):
            if i not in vals:
                return i