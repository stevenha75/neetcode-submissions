class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # look for the start of a seq
            if (n - 1) not in numSet: # we are @ start of seq
                length = 1 # init length
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)

        return longest


