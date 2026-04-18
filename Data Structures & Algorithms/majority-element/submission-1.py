class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # space optimized 
        # o(n) time, o(1) space
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            elif n == candidate:
                count += 1
            else:
                count -= 1

        return candidate

        