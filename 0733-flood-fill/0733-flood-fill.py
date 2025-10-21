class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(image)
        n = len(image[0])
        q = deque()
        q.append([sr,sc])
        image[sr][sc] = color
        while q:
            x,y = q.popleft()
            for dir in directions:
                i = x+dir[0]
                j = y+dir[1]
                if 0<=i<m and 0<=j<n and image[i][j] == original_color:
                    image[i][j] = color
                    q.append((i,j))
        return image