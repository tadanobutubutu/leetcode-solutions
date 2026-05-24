from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, val in enumerate(nums):
            indices[val].append(i)
        
        min_diff = float('inf')
        for val, idx_list in indices.items():
            if len(idx_list) >= 3:
                for s in range(len(idx_list) - 2):
                    diff = idx_list[s+2] - idx_list[s]
                    if diff < min_diff:
                        min_diff = diff
                        
        if min_diff == float('inf'):
            return -1
        return 2 * min_diff

