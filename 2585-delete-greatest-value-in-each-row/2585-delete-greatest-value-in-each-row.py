# import numpy as np
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        if not grid :
            return 0
        ans = 0
        for i in range(len(grid)):
            grid[i].sort()
            # print(grid)
        for j in range(len(grid[0])):
            ans += max(grid[i][j] for i in range(len(grid)))
                
        return ans