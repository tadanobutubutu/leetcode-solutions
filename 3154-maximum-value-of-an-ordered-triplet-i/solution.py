from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_i = 0
        max_diff = 0
        for x in nums:
            ans = max(ans, max_diff * x)
            max_diff = max(max_diff, max_i - x)
            max_i = max(max_i, x)
        return ans

