class Solution:
    # bfs soln. (same complexities)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # early break
        if image[sr][sc] == color:
            return image

        m, n = len(image), len(image[0]) 
        init = image[sr][sc]
        
        # init q 
        queue = deque()
        queue.append((sr, sc))
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


        while queue:
            R, C = queue.popleft()
            image[R][C] = color

            for dr, dc in dirs: 
                nr = R + dr
                nc = C + dc 

                # check bounds, visited
                if (0 <= nr < m and 
                    0 <= nc < n and
                    image[nr][nc] == init):
                    queue.append((nr, nc))

        return image



