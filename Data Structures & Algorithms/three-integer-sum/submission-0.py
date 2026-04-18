class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force soln
        res = []
        nums.sort()

        # Goal: a + b + c = 0

        # finding a
        for i, v in enumerate(nums):
            if v > 0:
                # can't get a + b + c = 0
                break

            if i > 0 and nums[i - 1] == v:
                continue # skip duplicate a's

            # finding b + c (l + r)
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = v + nums[l] + nums[r]

                if total > 0:
                    r = r - 1
                elif total < 0:
                    l = l + 1
                else:
                    res.append([v, nums[l], nums[r]])

                    # Combo found -> need to find more w/ a
                    r -=1
                    l += 1

                    # IGNORE DUPES W/ LEFT 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
