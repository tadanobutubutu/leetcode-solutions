from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for r in range(2):
            for c in range(2):
                cells = [
                    grid[r][c],
                    grid[r+1][c],
                    grid[r][c+1],
                    grid[r+1][c+1]
                ]
                b_count = cells.count('B')
                w_count = cells.count('W')
                if b_count >= 3 or w_count >= 3:
                    return True
        return False

