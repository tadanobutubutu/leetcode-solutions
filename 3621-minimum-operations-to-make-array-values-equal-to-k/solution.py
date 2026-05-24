from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        if min_val < k:
            return -1
        
        unique_vals = set(nums)
        if min_val == k:
            return len(unique_vals) - 1
        else:
            return len(unique_vals)

