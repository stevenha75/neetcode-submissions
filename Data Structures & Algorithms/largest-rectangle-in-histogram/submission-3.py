class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i 

            while stack and stack[-1][1] > h:
                # we know the prev rec ends here
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        # take care of all of the rec that are boundless
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea