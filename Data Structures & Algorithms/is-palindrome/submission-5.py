class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            # find first char from left
            while L < R and not s[L].isalnum():
                L += 1
            # find first char from right
            while L < R and not s[R].isalnum():
                R -= 1
            
            # compare
            if s[L].lower() != s[R].lower():
                return False
            else:
                L += 1
                R -= 1


        return True
        