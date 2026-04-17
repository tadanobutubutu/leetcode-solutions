class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    # 単独の塔の表面積 = 6*h - 2*(h-1)
                    ans += 6 * h - 2 * (h - 1)

                # 上の塔と接している部分を引く
                if i > 0:
                    ans -= 2 * min(h, grid[i - 1][j])

                # 左の塔と接している部分を引く
                if j > 0:
                    ans -= 2 * min(h, grid[i][j - 1])

        return ans

