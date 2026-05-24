from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 重複する要素が隣り合うようにソートする
        nums.sort()
        res = [[]]
        prev_size = 0
        
        for i in range(len(nums)):
            # 重複要素の場合、直前のループで新しく追加された部分集合にのみ
            # 現在の要素を付与することで、重複する部分集合の生成を防ぐ
            start = prev_size if (i > 0 and nums[i] == nums[i - 1]) else 0
            prev_size = len(res)
            
            for j in range(start, prev_size):
                res.append(res[j] + [nums[i]])
                
        return res

