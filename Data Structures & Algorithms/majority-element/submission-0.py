class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        targ = len(nums) // 2
        count = Counter(nums)

        for k in count:
            if count[k] > targ:
                return k 




        