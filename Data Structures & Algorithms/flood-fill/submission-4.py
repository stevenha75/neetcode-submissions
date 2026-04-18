class Solution:
    # bfs soln. (same complexities)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # early break
        init = image[sr][sc]
        if init == color:
            return image

        m, n = len(image), len(image[0]) 
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            R, C = queue.popleft()

            for dr, dc in dirs: 
                nr = R + dr
                nc = C + dc 

                # check bounds, visited
                if (0 <= nr < m and 
                    0 <= nc < n and
                    image[nr][nc] == init):
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image
