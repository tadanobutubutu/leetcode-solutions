from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        min_sum = float('inf')
        for k in range(l, r + 1):
            for i in range(n - k + 1):
                cur = pref[i + k] - pref[i]
                if cur > 0:
                    if cur < min_sum:
                        min_sum = cur
                        
        return min_sum if min_sum != float('inf') else -1

