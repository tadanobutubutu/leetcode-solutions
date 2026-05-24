from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collected = set()
        operations = 0
        for x in reversed(nums):
            operations += 1
            if x <= k:
                collected.add(x)
            if len(collected) == k:
                return operations
        return operations

