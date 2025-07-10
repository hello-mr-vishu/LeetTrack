class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):    
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0    
                elif i==0 and j==0:
                    dp[i][j]=1
                else:    
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]


        # Memo
        # def noofways(i,j):
        #     if i<0 or j<0:
        #         return 0            
        #     if obstacleGrid[i][j] == 1:
        #         return 0                
        #     if i == 0 and j== 0:
        #         return 1
            
        #     if dp[i][j]!= -1:
        #         return dp[i][j]

        #     up = noofways(i-1,j)
        #     right = noofways(i,j-1)

        #     dp[i][j] = up+right
        #     return dp[m-1][n-1]
        # return noofways(m-1,n-1)