class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visit):
            rows, cols = len(grid), len(grid[0])

            # base cases
            # oob, visited, blocked
            if (min(r, c) < 0) or \
                r == rows or c == cols \
                or ((r, c) in visit ) or \
                grid[r][c] == 1: 
                return 0
            # success
            if (r == rows - 1) and (c == cols - 1):
                return 1

            #visit
            visit.add((r, c)) # you add to a hashset cus it has no sense of order

            count = 0
            # recursive calls in all directions
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            # backtrack
            visit.remove((r, c))
            
            return count
        
        # initial call
        return dfs(grid, 0, 0, set())

