from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
        return ans

