class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # reshape が不可能なら元の行列を返す
        if m * n != r * c:
            return mat
        
        # 1次元に展開
        flat = []
        for row in mat:
            flat.extend(row)
        
        # 新しい行列に詰め直す
        res = []
        idx = 0
        for _ in range(r):
            res.append(flat[idx:idx + c])
            idx += c
        
        return res

