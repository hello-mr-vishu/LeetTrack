class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[float('inf')] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res[i][j] = float('inf')
                if mat[i][j] == 0 :
                    res[i][j] = 0
                else:
                    if i>0:
                        res[i][j] = min(res[i][j],res[i-1][j]+1)
                    if j>0:
                        res[i][j] = min(res[i][j],res[i][j-1]+1)

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if mat[i][j] != 0:
                    if  i< rows-1:
                        res[i][j] = min(res[i][j],res[i+1][j]+1)
                    if j<cols-1:
                        res[i][j] = min(res[i][j],res[i][j+1]+1)

        return res