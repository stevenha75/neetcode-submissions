class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window approach
        # char:index
        visited = {}
        maxl = 0
        L = 0
        R = 0

        while R < len(s):
            if s[R] in visited and visited[s[R]] >= L:
                # remove dupe from substring
                L = visited[s[R]] + 1

            visited[s[R]] = R
            maxl = max(maxl, R - L + 1)
            R += 1
        
        return maxl