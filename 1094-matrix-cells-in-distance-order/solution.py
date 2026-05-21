class Solution:
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        res = []
        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                res.append((dist, r, c))

        res.sort()
        return [[r, c] for _, r, c in res]

