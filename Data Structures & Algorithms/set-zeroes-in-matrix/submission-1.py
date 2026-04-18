class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # naive solution
        z_rows = set()
        z_cols = set()

        # save 0_rows, 0_cols
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    z_rows.add(r)
                    z_cols.add(c)

        # loop through matrix and update vals
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in z_rows:
                    matrix[r][c] = 0
                elif c in z_cols:
                    matrix[r][c] = 0
