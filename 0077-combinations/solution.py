from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start: int, path: List[int]):
            # 必要な数に達したら結果に追加
            if len(path) == k:
                res.append(list(path))
                return
            # 残りの要素数が必要な数に足りない場合は枝刈り
            if len(path) + (n - start + 1) < k:
                return
            
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return res

