class MinStack:

    def __init__(self):
        self.stack = [] # [(val, min)]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, float('inf')))
        prev = self.stack[-1]
        self.stack.append((val, min(prev[1], val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            prev = self.stack[-1]
            return prev[0] # last item val

    def getMin(self) -> int:
        prev = self.stack[-1]
        return prev[1]