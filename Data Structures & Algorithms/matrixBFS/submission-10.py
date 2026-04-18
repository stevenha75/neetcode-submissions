class Solution:
    # shortest path -> BFS alg approach
    def shortestPath(self, grid: List[List[int]]) -> int:
        # initializing necessary variables
        ROWS, COLS =  len(grid), len(grid[0])
        queue = deque()
        visit = set()
        # make first visit
        queue.append((0, 0))
        visit.add((0, 0))

        # counter for current layer of bfs
        length = 0

        # is there another layer?
        while queue:
            # take snapshot of curr layer
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # check for success
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # add the next layer
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    # check validity of dir
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or
                        nr == ROWS or nc == COLS or
                        (nr, nc) in visit or grid[nr][nc] == 1):
                        continue
                    # we know nr, nc is a valid dir
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1





        