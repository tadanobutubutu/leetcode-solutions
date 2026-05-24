from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(nums)
        evens = [x for x in counts if x % 2 == 0]
        if not evens:
            return -1
        return max(evens, key=lambda x: (counts[x], -x))

