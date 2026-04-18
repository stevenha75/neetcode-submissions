class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # goal: no dupes in rows, cols, sub-squares
        rows = defaultdict(set) # row : set
        cols = defaultdict(set) # col : set
        squares = defaultdict(set) # (r // 3, c // 3) : set

        # loop thru rows
        for r in range(9): # 0 -> 8
            # loop thru cols
            for c in range(9): # 0 -> 8
                # base case '.'
                if board[r][c] == '.':
                    continue
                
                # check for dupes -> ret false
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r // 3, c // 3)]):
                   return False

                # visit the value
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
