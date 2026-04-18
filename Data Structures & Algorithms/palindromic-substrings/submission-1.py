class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # efficient soln?
        def countPalindrome(l, r):
            count = 0
            
            # expand outwards & validate palindrome 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count

        # check all possible substring centers 
        for i in range(len(s)):
            # odd case
            res += countPalindrome(i, i)
            # even case
            res += countPalindrome(i, i + 1)
        
        return res
