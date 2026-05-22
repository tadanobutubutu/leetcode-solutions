from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = sum(1 for p in position if p % 2 == 0)
        odds = len(position) - evens
        return min(evens, odds)

