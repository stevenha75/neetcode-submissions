class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # init count buckets 
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        index = 0
        for i in range(len(count)):
            while count[i]:
                nums[index] = i
                count[i] -= 1
                index += 1 

        