class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force attempt (o(n^2))
        res = []

        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if j != i:
                    val *= nums[j]

            res.append(val)

        return res 

