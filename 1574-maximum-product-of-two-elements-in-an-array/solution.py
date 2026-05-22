from typing import List
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = heapq.nlargest(2, nums)
        return (m1 - 1) * (m2 - 1)

