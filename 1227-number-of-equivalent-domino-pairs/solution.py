from typing import List
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter()
        for a, b in dominoes:
            key = (a, b) if a < b else (b, a)
            count[key] += 1
            
        ans = 0
        for val in count.values():
            ans += val * (val - 1) // 2
            
        return ans

