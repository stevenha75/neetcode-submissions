class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_zero = False

        # setup imaginary z_rows, z_cols set
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # cols set is at row 0
                    matrix[0][c] = 0
                    # rows set is at col 0 
                    # special boolean for row 0 -> b/c overlap
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # go through -> update matrix based on z_row, z_cols set
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # skip row 0 -> b/c it's a special case
                if matrix[r][0] == 0:
                    matrix[r][c] = 0
                elif matrix[0][c] == 0:
                    matrix[r][c] = 0

        # take care of col 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
       
        # taking care of row 0, col 0 
        # taking care of row 0 
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        
