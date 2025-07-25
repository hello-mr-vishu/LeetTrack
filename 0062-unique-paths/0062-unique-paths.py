class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # one array for previous row 
        # one array for the current row
        prev = [1]*n
        for i in range(1,m):
            cur = [0]*n
            for j in range(n):
                if j == 0:
                    cur[j] = 1
                else:
                    cur[j] = cur[j-1] + prev[j]
            prev = cur
        return prev[n-1]


        # Tabulation
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j ==0:
        #             dp[i][j]=1
        #         else:
        #             dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]
        
        # Memo
        # def noofways(i,j):
        #     if i == 0 or j == 0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     up = noofways(i-1,j)
        #     left = noofways(i,j-1)
        #     dp[i][j] = up + left

        #     return dp[i][j]

        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # return noofways(m-1,n-1)

        
        # Recursive 
        # def numberofways(i,j):
        #     if i ==0 or j == 0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     return numberofways(i-1,j)+numberofways(i,j-1)
        # return numberofways(m-1,n-1)
