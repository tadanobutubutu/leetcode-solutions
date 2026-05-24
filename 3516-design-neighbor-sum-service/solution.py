from typing import List

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        for r in range(self.n):
            for c in range(self.n):
                self.pos[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total

    def diagonalSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

