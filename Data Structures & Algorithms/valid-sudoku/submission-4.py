class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Potential bruteforce methods?
        # Look through each row for dupes, 
        # Look through each col for dupes,
        # Look through each 3x3 for dupes

        # Row check
        for r in range(len(board)):
            row_set = set()
            for c in range(len(board[0])):
                if board[r][c] not in row_set:
                    row_set.add(board[r][c])
                elif board[r][c] == '.':
                    continue
                else:
                    return False 
        
        # Col check
        for c in range(len(board[0])):
            col_set = set()
            for r in range(len(board)):
                if board[r][c] not in col_set:
                    col_set.add(board[r][c])
                elif board[r][c] == '.':
                    continue
                else:
                    return False 

        # 3x3 Check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        val = board[r][c]
                        if val in box_set:
                            return False
                        elif val == '.':
                            continue
                        box_set.add(val)

        return True 


