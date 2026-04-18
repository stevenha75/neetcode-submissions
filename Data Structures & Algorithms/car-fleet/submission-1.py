class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        print(pairs)

        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)

            if len(stack) >= 2 and (stack[-1] <= stack[-2]):
                stack.pop()

        return len(stack)