from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # 最長連続プレフィックスの和を計算
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
        # nums に含まれる値を set にする
        num_set = set(nums)
        
        # prefix_sum 以上の最小の missing integer を探す
        x = prefix_sum
        while x in num_set:
            x += 1
            
        return x

