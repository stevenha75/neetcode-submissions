class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        L = 0
        res = 0

        for R in range(len(s)):
            # base case: duplicate char
            while s[R] in visited:
                visited.remove(s[L])
                L += 1
            
            visited.add(s[R])
            res = max(res, (R - L) + 1)
        
        return res
        