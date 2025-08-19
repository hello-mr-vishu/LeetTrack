class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # directions = [[1,0],[0,1],[-1,0],[0,-1]]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(grid):
            q = deque()
            fresh = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        q.append((i,j))
                    elif grid[i][j] ==1:
                        fresh += 1
            elapsedtime = 0

            while q and fresh >0:
                elapsedtime +=1
                for _ in range(len(q)):
                    i,j = q.popleft()

                    for dir in directions:
                        x = i +dir[0]
                        y = j +dir[1]
                        if 0<=x and x<n and y>=0 and y<m and grid[x][y] ==1:
                            grid[x][y] = 2
                            fresh -= 1
                            q.append((x,y))
            
            return elapsedtime if fresh ==0  else -1
        return bfs(grid)