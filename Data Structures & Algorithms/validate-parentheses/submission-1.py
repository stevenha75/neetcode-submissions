class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            # remove the innermost pair
            s = s.replace('[]', '')
            s = s.replace('()', '')
            s = s.replace('{}', '')

        return s == ''