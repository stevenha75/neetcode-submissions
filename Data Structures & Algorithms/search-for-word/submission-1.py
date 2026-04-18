class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # to avoid dupes -> visited list is necessary
        visited = []

        # when doing dfs we need variables to navigate thru
        # 2d array, string
        def dfs(r, c, i):
            # base cases
            # end of string
            if i == len(word):
                return True
            # false cases: OOB, !=, visited 
            if (r >= ROWS or c >= COLS or
                r < 0 or c < 0 or
                word[i] != board[r][c] or
                (r, c) in visited):
                return False
            
            # valid position -> visit
            visited.append((r, c))
            # check each dir
            if (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)):
                return True
            visited.remove((r, c))
        
        # loop through 2d array and check for valid paths
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False 


            
