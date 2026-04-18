class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # efficient soln?
        cache = {}

        for i, n in enumerate(nums):
            cache[n] = i

        for i, n in enumerate(nums):
            if (target - n) in cache and cache[target - n] != i:
                if cache[target - n] < i:
                    return [cache[target - n], i]
                else:
                    return [i, cache[target - n]]
            
