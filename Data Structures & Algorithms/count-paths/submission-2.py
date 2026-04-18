class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp approach (bottom-up approach)
        def dp(rows, cols):
            # init prev row
            prevRow = [0] * cols

            # loop through rows from bottom
            for r in range(rows - 1, -1, -1):
                currRow = [0] * cols
                currRow[cols - 1] = 1
                # loop through cols from right
                for c in range(cols - 2, -1, -1):
                    currRow[c] = currRow[c + 1] + prevRow[c]
                prevRow = currRow
            return prevRow[0]

        return dp(m, n)