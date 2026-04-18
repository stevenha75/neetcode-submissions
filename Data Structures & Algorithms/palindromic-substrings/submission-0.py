class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        # looping through all possible substrings
        for i in range(len(s)):
            # start at i for single char strings
            for j in range(i, len(s)):
                # checking current substring 
                is_palindrome = True 

                L = i
                R = j
                # check for palindrome
                while L <= R:
                    if s[L] != s[R]:
                        is_palindrome = False
                    L += 1
                    R -= 1
                
                if is_palindrome:
                    count += 1 

        return count