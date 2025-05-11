class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image        
        oldcolor = image[sr][sc]
        self.dfs(image,color,sr,sc,oldcolor)
        return image
    def dfs(self,image,color,r,c,oldcolor):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]!= oldcolor:
            return
        print(image[r][c])
        image[r][c] = color
        self.dfs(image,color,r-1,c,oldcolor)
        self.dfs(image,color,r,c-1,oldcolor)
        self.dfs(image,color,r+1,c,oldcolor)
        self.dfs(image,color,r,c+1,oldcolor)