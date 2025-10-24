class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]== 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                i = x+dx
                j = y+dy
                if 0<=i<m and 0<=j<n :
                    if mat[i][j] > mat[x][y]+1:
                        mat[i][j] = mat[x][y]+1
                        q.append((i,j))
        return mat