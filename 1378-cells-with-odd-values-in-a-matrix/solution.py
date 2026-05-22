from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        for r, c in indices:
            row_count[r] ^= 1
            col_count[c] ^= 1
            
        odd_rows = sum(row_count)
        odd_cols = sum(col_count)
        
        even_rows = m - odd_rows
        even_cols = n - odd_cols
        
        return odd_rows * even_cols + even_rows * odd_cols

