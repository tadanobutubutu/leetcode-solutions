from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                target = nums[i-1] + 1
                ans += target - nums[i]
                nums[i] = target
        return ans

