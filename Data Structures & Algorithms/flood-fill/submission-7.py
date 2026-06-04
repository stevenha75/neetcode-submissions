class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # bfs implementation
        orig = image[sr][sc]
        if orig == color:
            return image
        
        m, n = len(image), len(image[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # check new dir for validity
                if (0 <= nr < m) and (0 <= nc < n) and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image