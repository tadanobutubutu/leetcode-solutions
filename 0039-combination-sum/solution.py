from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def dfs(start: int, path: List[int], current_sum: int):
            if current_sum == target:
                result.append(path)
                return
                
            for i in range(start, len(candidates)):
                # 枝刈り：ソート済みなので、これ以上足すと target を超える場合は終了
                if current_sum + candidates[i] > target:
                    break
                    
                dfs(i, path + [candidates[i]], current_sum + candidates[i])
                
        dfs(0, [], 0)
        return result

