class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow] # move pointer by 1
            fast = nums[nums[fast]] # move pointer by 2

            # loop found ->
            if slow == fast:
                break

        slow2 = 0

        # once slow1, slow 2 meet -> we are @ the start of the loop mathematically
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
        