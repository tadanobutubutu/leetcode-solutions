from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        for k in range(n):
            shifted = nums[n - k:] + nums[:n - k]
            if shifted == sorted_nums:
                return k
        return -1

