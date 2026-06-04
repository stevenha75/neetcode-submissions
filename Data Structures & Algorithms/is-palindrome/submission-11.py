class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # find alnum
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            # have two to compare
            if s[l].lower() != s[r].lower():
                return False
            
            # look at more
            l += 1 
            r -= 1

        return True
