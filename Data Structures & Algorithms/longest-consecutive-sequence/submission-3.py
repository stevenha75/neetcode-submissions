class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sliding window?
        # what data struct? hashset?
        # bruteforce soln? trying every possibility
        # empty list case
        if not nums:
            return 0
        
        nums.sort()
        res = 1
        count = 1


        for i in range(1, len(nums)):
            # skip dupes
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                # we know it's consecutive
                count += 1
                res = max(count, res)
            else:
                count = 1
        
        return res

