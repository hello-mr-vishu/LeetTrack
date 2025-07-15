class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minPath(r, c):
            if r < 0 or c < 0:
                return float('inf')
            if r == 0 and c == 0:
                return grid[0][0]
            if dp[r][c] != -1:
                return dp[r][c]
            up = minPath(r - 1, c)
            left = minPath(r, c - 1)
            dp[r][c] = grid[r][c] + min(up, left)
            return dp[r][c]

        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return minPath(m - 1, n - 1)


        # Recursive solution
        # def minPath(m,n):
        #     if m < 0 or n < 0:
        #         return float('inf')
        #     if m==0 and n==0:
        #         return grid[0][0]
        #     return grid[m][n]+min(minPath(m-1,n),minPath(m,n-1))
        
        # r = len(grid)
        # c = len(grid[0])
        # return minPath(r-1,c-1)