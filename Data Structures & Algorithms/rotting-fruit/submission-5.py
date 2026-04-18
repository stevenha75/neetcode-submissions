class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, length = 0, 0
        ROW, COL =  len(grid), len(grid[0])
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q and fresh > 0:
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0 or 
                        r + dr == ROW or c + dc == COL or
                        grid[r + dr][c + dc] == 0 or 
                        grid[r + dr][c + dc] == 2):
                        continue
                    else:
                        grid[r + dr][c + dc] = 2
                        q.append((r + dr, c + dc))
                        fresh -= 1
                
            length += 1

        return length if fresh == 0 else -1 


                


                