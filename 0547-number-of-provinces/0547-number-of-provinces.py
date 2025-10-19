class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        def dfs(x):
            for neighbour in range(m):
                if mat[x][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        m = len(mat)
        # n = len(mat[0])
        visited = set()
        cnt = 0
        for i in range(m):
            # print(visited)
            if i not in visited:
                visited.add(i)
                dfs(i)
                cnt+=1
            # print(cnt)
        return cnt