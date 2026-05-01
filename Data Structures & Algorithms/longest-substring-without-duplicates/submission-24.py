class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 
        
        # two pointer approach
        L, R = 0, 0
        seen = set()
        res = 0

        while R < len(s):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])

            res = max(res, R - L + 1)
            R += 1 
        
        return res