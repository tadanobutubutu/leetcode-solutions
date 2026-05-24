from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # 2と3の両方で割り切れる数（＝6で割り切れる数）をフィルタリング
        valid_nums = [x for x in nums if x % 6 == 0]
        
        # 該当する数が存在しない場合は0を返す
        if not valid_nums:
            return 0
            
        # 平均値を計算（小数点以下切り捨て）
        return sum(valid_nums) // len(valid_nums)

