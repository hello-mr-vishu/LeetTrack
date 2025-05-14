from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m , n = len(grid),len(grid[0])
        visited = [[False for _ in range(n)]for _ in range(m)]
        def check(rows,cols):
            return rows>=0 and cols>=0 and rows<m and cols<n

        def boundary(rows,cols):
            return rows==0 or cols==0 or rows == m-1 or cols == n-1

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited[r][c]=True
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    newrow,newcol = row+dr,col+dc
                    if check(newrow,newcol) and not visited[newrow][newcol] and grid[newrow][newcol]==1:
                        visited[newrow][newcol] = True
                        q.append((newrow, newcol))

        # check evry element
        for i in range(m):
            for j in range(n):
                if boundary(i, j) and grid[i][j] == 1:
                    bfs(i, j)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    cnt+=1
        return cnt