from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # nums[0] は固定。nums[1:] のうち最も小さい2つの要素を足す
        remaining = sorted(nums[1:])
        return nums[0] + remaining[0] + remaining[1]

