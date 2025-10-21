class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 :
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        if fresh == 0:
            return 0
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        time = -1
        
        while queue:
            time += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dir in directions:
                    i = x+dir[0]
                    j = y+dir[1]
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        grid[i][j] = 2
                        queue.append((i,j))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time