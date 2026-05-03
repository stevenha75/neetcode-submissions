class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                t1 = stack.pop()
                t2 = stack.pop()
                
                if t == "+":
                    stack.append(t2 + t1)
                if t == "-":
                    stack.append(t2 - t1)
                if t == "*":
                    stack.append(t2 * t1)
                if t == "/":
                    stack.append(int(t2 / t1))
            else:
                stack.append(int(t))

        return stack[0]