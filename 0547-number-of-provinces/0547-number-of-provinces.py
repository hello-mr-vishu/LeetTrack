class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        visited = set()
        m = len(mat)
        provinces = 0
        for i in range(m):
            if i not in visited:
                queue = deque([i])
                while queue:
                    city = queue.popleft()
                    for neighbour in range(m):
                        if mat[city][neighbour] == 1 and neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)
                provinces += 1
        return provinces