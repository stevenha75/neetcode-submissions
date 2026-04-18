class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # standardizes tuples
        triplets = set() 

        # loop through all pairs of 3 indices 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        triplets.add(tuple([nums[i], nums[j], nums[k]]))
        
        # cast triplet back into list from tuple
        return [list(triplet) for triplet in triplets]


