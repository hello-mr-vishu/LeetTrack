class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def noofways(i,j):
            if i == 0 or j == 0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            up = noofways(i-1,j)
            left = noofways(i,j-1)
            dp[i][j] = up + left

            return dp[i][j]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return noofways(m-1,n-1)

        
        # Recursive 
        # def numberofways(i,j):
        #     if i ==0 or j == 0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     return numberofways(i-1,j)+numberofways(i,j-1)
        # return numberofways(m-1,n-1)
