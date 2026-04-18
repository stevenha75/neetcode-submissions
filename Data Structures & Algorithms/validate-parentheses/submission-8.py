class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctoo = {'}':'{', ')':'(', ']':'['}

        for c in s:
            if c in ctoo:
                if not stack or stack.pop() != ctoo[c]:
                    return False
            else:
                stack.append(c)

        return not stack

