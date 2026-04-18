class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from rotten fruits, each layer is a minute 
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque() # (r, c)
        time = 0

        # init q + fresh
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        # go layer by layer (entire q)
        while fresh > 0 and q:
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft() # spread from cur
                
                r, c = cur
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr in range(m) and
                        nc in range(n) and
                        grid[nr][nc] == 1 # fresh!
                    ):
                        grid[nr][nc] = 2 # set rotten!
                        fresh -= 1
                        q.append((nr, nc))
                
            time += 1 

        return time if fresh == 0 else -1