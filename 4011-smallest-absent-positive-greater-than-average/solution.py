import math
from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        start = max(1, math.floor(avg) + 1)
        nums_set = set(nums)
        
        curr = start
        while curr in nums_set:
            curr += 1
        return curr

