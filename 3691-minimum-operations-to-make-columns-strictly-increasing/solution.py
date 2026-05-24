from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total_ops = 0
        
        for j in range(n):
            for i in range(1, m):
                target = grid[i-1][j] + 1
                if grid[i][j] < target:
                    total_ops += target - grid[i][j]
                    grid[i][j] = target
                    
        return total_ops

