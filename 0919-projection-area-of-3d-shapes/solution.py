class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)

        xy = 0
        yz = 0
        zx = 0

        for i in range(n):
            max_row = 0
            max_col = 0
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            zx += max_row
            yz += max_col

        return xy + yz + zx

