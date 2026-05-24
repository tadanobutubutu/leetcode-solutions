from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        m = max(amount)
        S = sum(amount)
        return max(m, (S + 1) // 2)

