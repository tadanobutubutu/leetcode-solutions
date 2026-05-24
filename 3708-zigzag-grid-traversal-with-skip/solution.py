from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        flat = []
        n = len(grid)
        for i in range(n):
            if i % 2 == 0:
                # 偶数行は左から右
                flat.extend(grid[i])
            else:
                # 奇数行は右から左
                flat.extend(grid[i][::-1])
        return flat[::2]

