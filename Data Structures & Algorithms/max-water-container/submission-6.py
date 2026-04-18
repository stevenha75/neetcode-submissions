class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer (o(n))
        res = 0

        L, R = 0, len(heights) - 1
        while L < R:
            cur = min(heights[L], heights[R]) * (R - L)
            res = max(res, cur)

            if heights[L] <= heights[R]:
                L += 1 
            else:
                R -= 1 

        return res 