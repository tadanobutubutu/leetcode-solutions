from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while True:
            # 1. Left to Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
                
            # 2. Top to Bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
                
            # 3. Right to Left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
                
            # 4. Bottom to Top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
                
        return res

