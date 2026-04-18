class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        q = deque()
        ROW, COL = len(grid), len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

        while q and fresh > 0:
            # take a snapshot of the current key
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr < 0 or nr == ROW or 
                        nc < 0 or nc == COL or 
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    else:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1

