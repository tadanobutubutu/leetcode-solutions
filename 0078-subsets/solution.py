from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            # 既存のすべての部分集合に現在のnumを追加した新しい部分集合を生成して追加
            res += [curr + [num] for curr in res]
        return res

