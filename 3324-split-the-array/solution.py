from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for val, count in counts.items():
            if count > 2:
                return False
        return True

