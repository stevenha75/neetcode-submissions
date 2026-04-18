class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(c.lower() for c in s if c.isalnum())

        return filtered_string == filtered_string[::-1]

        