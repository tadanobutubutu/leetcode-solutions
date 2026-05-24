from typing import List
from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counts = Counter(frozenset(w) for w in words)
        
        ans = 0
        for count in counts.values():
            if count > 1:
                ans += count * (count - 1) // 2
        return ans

