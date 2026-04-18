class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                # case is a number
                stack.append(int(token))
            else:
                # is operator
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b 
                elif token == "/":
                    result = int(a / b)
                
                stack.append(result)

        return stack[0]






        