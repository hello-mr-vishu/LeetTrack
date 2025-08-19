class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        original = image[sr][sc]
        if original == color:
            return image
        # image[sr][sc] = color
        q = deque()
        q.append((sr,sc))
        while q:
            i,j = q.popleft()
            if image[i][j] == original:
                image[i][j] = color
                for dx,dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0<= y <m and image[x][y] == original:
                        q.append((x,y))
        return image
