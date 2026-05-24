from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n
        
        for i, w in enumerate(words):
            if w == target:
                dist = abs(i - startIndex)
                ans = min(ans, dist, n - dist)
                
        return ans if ans < n else -1

