from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        total_counts = Counter("".join(words))
        
        for char, count in total_counts.items():
            if count % n != 0:
                return False
        return True

