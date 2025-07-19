class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]

        for j in range(n):
            dp[0][j] = matrix[0][j]
        # for i in range(1,m):
        #     for j in range(n):
        #         up = matrix[i][j] + dp[i-1][j]
        #         leftdiag = matrix[i][j]
        #         if j - 1 >= 0:
        #             leftdiag += dp[i - 1][j - 1]
        #         else:
        #             leftdiag += float('inf')
        #         rightdiag = matrix[i][j] 
        #         if j+1<m:
        #             rightdiag +=  dp[i+1][j+1]
        #         else:
        #             rightdiag += float('inf')
        #         dp[i][j] = min(up,leftdiag,rightdiag)
        for i in range(1, m):
            for j in range(n):
                up = matrix[i][j] + dp[i - 1][j]
                leftdiag = matrix[i][j] + (dp[i - 1][j - 1] if j > 0 else float('inf'))
                rightdiag = matrix[i][j] + (dp[i - 1][j + 1] if j < n - 1 else float('inf'))
                dp[i][j] = min(up, leftdiag, rightdiag)
        # res = float('inf')
        # for j in range(n):
        #     res = min(dp[m][j],res)
        # return res
        return min(dp[m - 1])