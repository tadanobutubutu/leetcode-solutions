from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(c * (c - 1) // 2 for c in counts.values())

