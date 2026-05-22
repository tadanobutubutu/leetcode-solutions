from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))

