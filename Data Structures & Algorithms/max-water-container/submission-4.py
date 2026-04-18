class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # bruteforce
        max_ar = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                max_ar = max(max_ar, min(heights[i], heights[j]) * (j - i))
                
        return max_ar