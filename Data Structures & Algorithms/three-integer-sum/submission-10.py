class Solution:
    # bruteforce -> triple loop
    # can I do better? -> maybe for each n -> do a two sum? 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            cur, targ = nums[i], -nums[i]
            L, R = i + 1, len(nums) - 1

            # two pointer approach (inner two sum)
            while L < R:
                lr = nums[L] + nums[R]

                if lr < targ:
                    L += 1
                elif lr > targ:
                    R -= 1
                else:
                    res.append([cur, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1

        return res
        