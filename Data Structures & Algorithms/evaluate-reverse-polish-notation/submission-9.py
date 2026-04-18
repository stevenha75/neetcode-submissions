class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack soln seems ideal
        stack = []
        ops = ["+", "-", "*", "/"]

        for t in tokens:
            if t in ops:
                t1, t2 = stack.pop(), stack.pop()
                if t == "+":
                    t3 = t2 + t1
                elif t == "-":
                    t3 = t2 - t1
                elif t == "*":
                    t3 = t2 * t1
                else:
                    t3 = int(t2 / t1)
                stack.append(t3)
            else:
                stack.append(int(t))

        return stack[-1]
                    
