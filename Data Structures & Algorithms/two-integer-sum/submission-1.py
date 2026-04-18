class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce soln
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1): # starts 1 ahead but ends @ the same loco
                if (nums[i] + nums[j]) == target:
                    return [i, j]