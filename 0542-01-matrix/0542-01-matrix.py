class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[float('inf')]*m for _ in range(n)]
        q = deque()
        # print(ans)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j]=0
                    q.append((i,j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            len_q = len(q)
            x,y = q.popleft()
            for dx, dy in directions:
                i = x+dx
                j = y+dy
                if 0<=i<n and 0<=j<m :
                    if ans[i][j] > ans[x][y]+1:
                        ans[i][j] = ans[x][y] + 1
                        q.append((i,j))
        return ans