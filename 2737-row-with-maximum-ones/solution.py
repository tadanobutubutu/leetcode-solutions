class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_ones = -1
        best_row = -1
        for r in range(len(mat)):
            ones = sum(mat[r])
            if ones > max_ones:
                max_ones = ones
                best_row = r
        return [best_row, max_ones]

