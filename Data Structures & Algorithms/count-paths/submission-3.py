class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # at first seems recursive (hint: subproblems)
        # keep in mind: can only go down & right
        row = [1] * n 

        for i in range(m - 2, -1, -1):
            # default to 1 for new_row
            new_row = [1] * n

            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            
            row = new_row
        
        return row[0]

        