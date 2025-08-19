class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        original = image[sr][sc]
        if original == color:
            return image
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return 
            if image[i][j] != original:
                return 
            image[i][j] = color
            image[i][j] = color
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        dfs(sr,sc)
        return image