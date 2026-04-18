class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # get the first num
        for i, val in enumerate(nums):
            # all numbers postive case
            if nums[i] > 0:
                break

            # dedup first num
            if i and nums[i - 1] == nums[i]:
                continue

            # get next numbers using two pointer approach
            L, R = i + 1, len(nums) - 1
            while L < R:
                tot = val + nums[L] + nums[R]

                if tot > 0:
                    R -= 1
                elif tot < 0:
                    L += 1
                else:
                    res.append([val, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    # dedup the 2nd num
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res
