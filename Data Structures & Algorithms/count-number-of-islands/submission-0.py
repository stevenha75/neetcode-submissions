class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through each cell in the grid
        # When 1 -> perform DFS to mark land 
        # Convert land cells to 0 to mark them as explored
        # Increment the island count for each dfs init 

        if not grid or not grid[0]:
            return 0 
        
        def dfs(i, j): 
            # exit the DFS if out of bounds or @ a water cell
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return    
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands