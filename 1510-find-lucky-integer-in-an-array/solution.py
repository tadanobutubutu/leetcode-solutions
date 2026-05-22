from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        lucky = [x for x, freq in counts.items() if x == freq]
        return max(lucky) if lucky else -1

