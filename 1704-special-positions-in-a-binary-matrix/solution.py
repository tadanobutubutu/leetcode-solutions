from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(col) for col in zip(*mat)]
        return sum(
            mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1
            for i in range(len(mat))
            for j in range(len(mat[0]))
        )

