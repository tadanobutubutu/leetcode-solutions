from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n
        if k == 0:
            return True
            
        for r in range(m):
            for j in range(n):
                if r % 2 == 0:
                    if mat[r][j] != mat[r][(j + k) % n]:
                        return False
                else:
                    if mat[r][j] != mat[r][(j - k) % n]:
                        return False
        return True

