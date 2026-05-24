from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        target = nums[0] + nums[1]
        ops = 1
        i = 2
        while i + 1 < len(nums):
            if nums[i] + nums[i+1] == target:
                ops += 1
                i += 2
            else:
                break
        return ops

