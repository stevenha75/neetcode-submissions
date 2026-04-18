class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        # recursive function 
        def dfs(i , j):
            # base case
            if i == len(text1) or j == len(text2):
                return 0 # nothing left to match 
            # check if we've solved the subproblem
            if (i, j) in memo:
                return memo[(i, j)]

            # recursive cases
            # found char in lcs
            if text1[i] == text2[j]:
                # check rest of chars
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                # no match
                # check all other cases
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[(i, j)]

        return dfs(0, 0)
        
