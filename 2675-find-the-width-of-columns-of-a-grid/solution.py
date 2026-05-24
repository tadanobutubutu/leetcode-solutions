class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        ans = []
        for c in range(n):
            max_w = 0
            for r in range(m):
                max_w = max(max_w, len(str(grid[r][c])))
            ans.append(max_w)
        return ans

