class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def noofways(i,j):
            if i<0 or j<0:
                return 0            
            if obstacleGrid[i][j] == 1:
                return 0                
            if i == 0 and j== 0:
                return 1
            
            if dp[i][j]!= -1:
                return dp[i][j]

            up = noofways(i-1,j)
            right = noofways(i,j-1)

            dp[i][j] = up+right
            return dp[i][j]
        return noofways(m-1,n-1)