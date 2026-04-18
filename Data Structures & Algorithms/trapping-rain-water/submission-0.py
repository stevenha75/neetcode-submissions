class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        l_max = height[L]
        r_max = height[R]
        res = 0

        while L < R:
            if height[L] < height[R]:
                L += 1
                l_max = max(l_max, height[L])
                res += l_max - height[L]
            else:
                R -= 1
                r_max = max(r_max, height[R])
                res += r_max - height[R]

        return res
