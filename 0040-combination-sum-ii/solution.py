from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def dfs(start: int, path: List[int], current_sum: int):
            if current_sum == target:
                result.append(path)
                return
                
            for i in range(start, len(candidates)):
                # 枝刈り：足して target を超えるならループ終了
                if current_sum + candidates[i] > target:
                    break
                    
                # 重複の回避：同じ探索レベルで同じ値を重複して選択しない
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                # i + 1 を渡すことで各要素は1回限りの使用にする
                dfs(i + 1, path + [candidates[i]], current_sum + candidates[i])
                
        dfs(0, [], 0)
        return result

