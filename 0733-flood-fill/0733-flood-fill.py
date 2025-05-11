from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # bfs approach
        # if the image is large — Python’s default recursion limit might be exceeded. For large grids, consider using an iterative BFS approach.
        rows , columns = len(image),len(image[0])
        oldcolor = image[sr][sc]
        if image[sr][sc]==color:
            return image
        q = deque([(sr,sc)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        image[sr][sc]= color
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy

                if 0<=nx<rows and 0<=ny<columns and image[nx][ny] == oldcolor:
                    image[nx][ny] = color
                    q.append((nx,ny))
        return image













    # dfs
    #     if image[sr][sc] == color:
    #         return image        
    #     oldcolor = image[sr][sc]
    #     self.dfs(image,color,sr,sc,oldcolor)
    #     return image
    # def dfs(self,image,color,r,c,oldcolor):
    #     if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]!= oldcolor:
    #         return
    #     print(image[r][c])
    #     image[r][c] = color
    #     self.dfs(image,color,r-1,c,oldcolor)
    #     self.dfs(image,color,r,c-1,oldcolor)
    #     self.dfs(image,color,r+1,c,oldcolor)
    #     self.dfs(image,color,r,c+1,oldcolor)
