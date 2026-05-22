from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k = k % total
        
        if k == 0:
            return grid
            
        flat = []
        for r in grid:
            flat.extend(r)
            
        shifted = flat[-k:] + flat[:-k]
        
        ans = []
        for i in range(0, total, n):
            ans.append(shifted[i:i+n])
            
        return ans

