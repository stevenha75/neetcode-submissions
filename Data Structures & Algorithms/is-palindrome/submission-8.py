class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []

        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())

        joined = ''.join(cleaned)

        return joined == joined[::-1]