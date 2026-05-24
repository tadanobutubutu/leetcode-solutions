from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        curr_min = float('inf')
        for c in cost:
            if c < curr_min:
                curr_min = c
            ans.append(curr_min)
        return ans

