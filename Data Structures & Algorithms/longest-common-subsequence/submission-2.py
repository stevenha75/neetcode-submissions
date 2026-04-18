class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d dp approach o(m*n) space & time complexity
        # setting up the 2d array
        dp = [
            [0 for j in range(len(text2) + 1)]
            for i in range(len(text1) + 1)
        ]

        # loop backgrounds through dp array (bottom-up approach)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # case 1 char match
                if text2[j] == text1[i]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # other
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]