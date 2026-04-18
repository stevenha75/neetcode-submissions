class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        # Use visited set to find dupes

        visited = set()
        res = 0 
        
        # init L, R for sliding window technique
        L = 0
        for R in range(len(s)):
            while s[R] in visited:
                visited.remove(s[L])
                L += 1

            # visit & check for max length
            visited.add(s[R])
            res = max(res, R - L + 1)
            
        return res
