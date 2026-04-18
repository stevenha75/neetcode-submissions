class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # can start anywhere
        # window approach ideal
        visited = set()
        maxl = 0
        L = 0
        R = 0

        while R < len(s):
            if s[R] in visited:
                # remove dupe from substring
                visited.remove(s[L])
                L += 1
                continue
            visited.add(s[R])
            maxl = max(maxl, len(visited))
            R += 1
        
        return maxl