class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (i, j)
        res = 0

        # visits entire island
        # node: (i, j)
        def dfs(node, grid, visited):
            n, m = len(grid), len(grid[0])

            # visit
            if node not in visited and grid[node[0]][node[1]] == "1":
                visited.add(node)
            else:
                return

            dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in dirs:
                nr, nc = node[0] + dr, node[1] + dc
                if 0 <= nr < n and 0 <= nc < m:
                    dfs((nr, nc), grid, visited)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1 

                    # mark entire island visited 
                    dfs((i, j), grid, visited)

        return res