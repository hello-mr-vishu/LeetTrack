from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in directions:
                    row, col = i + dr, j + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
