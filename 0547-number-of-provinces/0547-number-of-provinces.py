class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        def dfs(node):
            for neighbour, adj in enumerate(isConnected[node]):
                if adj and neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)        
        v = len(isConnected[0])
        # print(v)
        ans = 0
        for i in range(v):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans