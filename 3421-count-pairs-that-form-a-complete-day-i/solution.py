from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_counts = [0] * 24
        pairs = 0
        for h in hours:
            r = h % 24
            target = (24 - r) % 24
            pairs += remainder_counts[target]
            remainder_counts[r] += 1
        return pairs

