from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        # answer を matrix のコピーとして初期化
        answer = [row[:] for row in matrix]
        
        # 各列の最大値を計算
        col_max = []
        for j in range(n):
            col_max.append(max(matrix[i][j] for i in range(m)))
            
        # -1 の要素をその列の最大値に置き換える
        for i in range(m):
            for j in range(n):
                if answer[i][j] == -1:
                    answer[i][j] = col_max[j]
                    
        return answer

