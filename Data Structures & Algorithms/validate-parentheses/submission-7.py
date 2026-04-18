class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '}' or c == ']' or c == ')':
                if stack:
                    if c == '}':
                        if stack.pop() != '{':
                            return False
                    elif c == ']':
                        if stack.pop() != '[':
                            return False
                    elif c == ')':
                        if stack.pop() != '(':
                            return False
                else: 
                    return False
            else:
                stack.append(c)

        return not stack

