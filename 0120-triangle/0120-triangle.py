class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def rectotal(i,j):
            
            if i == len(triangle)-1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = triangle[i][j] + min(rectotal(i+1,j),rectotal(i+1,j+1))
            return dp[i][j]
        # dp = [[-1 for _ in range(len(triangle))] for _ in range(len(triangle))]
        n = len(triangle)
        dp = [[-1 for _ in range(len(triangle[row]))] for row in range(n)]
        return rectotal(0,0)