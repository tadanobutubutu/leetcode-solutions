from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = max(counts.values())
        return sum(freq for freq in counts.values() if freq == max_freq)

