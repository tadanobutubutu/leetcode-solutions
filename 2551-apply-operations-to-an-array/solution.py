from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. 隣接する要素が等しい場合の操作を順次適用
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        # 2. 0以外の要素を抽出し、残りを0で埋める
        non_zeros = [x for x in nums if x != 0]
        return non_zeros + [0] * (n - len(non_zeros))

