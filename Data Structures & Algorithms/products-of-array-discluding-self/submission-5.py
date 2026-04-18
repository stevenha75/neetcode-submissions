class Solution:
    # o(n) time, o(n) space 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = [1] * len(nums), [1] * len(nums)
        res = []

        # build L
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]

        # build R 
        for i in range(len(nums) - 2, -1, -1): 
            R[i] = R[i + 1] * nums[i + 1]

        # build res from L + R
        for i in range(len(nums)):
            print(L)
            print(R)
            
            res.append(L[i] * R[i])

        return res