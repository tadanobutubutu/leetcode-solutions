from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        unique_sums = set()
        n = len(nums)
        
        # 両端からペアを作って和をセットに格納していく
        for i in range(n // 2):
            unique_sums.add(nums[i] + nums[n - 1 - i])
            
        return len(unique_sums)

