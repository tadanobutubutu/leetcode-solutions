from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 配列の長さが2以下の場合はそのまま返す（高々2回の重複しかあり得ないため）
        if len(nums) <= 2:
            return len(nums)
            
        # 書き込みポインタ（w）を初期値2からスタート
        w = 2
        for r in range(2, len(nums)):
            # 現在の要素が、2つ前に書き込まれた要素と異なる場合のみ書き込む
            if nums[r] != nums[w - 2]:
                nums[w] = nums[r]
                w += 1
                
        return w

