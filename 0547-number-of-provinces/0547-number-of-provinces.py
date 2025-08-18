class Solution:
    def findCircleNum(self, isconn: List[List[int]]) -> int:
        row = len(isconn)
        # col = len(i[0])
        visited = set()
        def bfs(node):
            while q:
                node = q.popleft()
                for neighbour in range(row):
                    if isconn[node][neighbour] == 1 and neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
        
        province = 0
        for city in range(row):
            if city not in  visited:
                q = deque([city])
                visited.add(city)
                bfs(city)
                province +=1
        return province