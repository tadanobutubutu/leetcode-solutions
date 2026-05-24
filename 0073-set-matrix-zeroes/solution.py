from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # 1. 最初の行に0があるかチェック
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
                
        # 2. 最初の列に0があるかチェック
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
                
        # 3. 最初の行と最初の列をマーカーとして使用して0をチェック
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # 4. マーカーに基づいて0をセット
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # 5. 最初の行と列自体の更新
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0
                
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0

