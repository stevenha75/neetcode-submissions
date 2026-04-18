class Solution:
    # two pointer soln
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, v in enumerate(nums):
            # break early if impossible
            if v > 0:
                break 

            # get first num + dedupe
            if i > 0 and v == nums[i - 1]:
                continue
            
            # window two sum
            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = v + nums[L] + nums[R]
                if sum > 0:
                    R -= 1 
                elif sum < 0:
                    L += 1
                else:
                    res.append([v, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1] :
                        L += 1 

        return res 
            
