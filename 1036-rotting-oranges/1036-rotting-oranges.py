class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j,time):
            for dir in directions:
                x = i+dir[0]
                y = j+dir[1]
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] == 1 or (grid[x][y] > time + 1):
                        grid[x][y] = time + 1
                        dfs(x, y, time + 1)
        
        rotten = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dfs(i,j,2)
        minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    return -1
                minutes = max(minutes, grid[i][j])

        return minutes - 2 if minutes > 0 else 0

    