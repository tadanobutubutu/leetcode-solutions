from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        count = 0
        for x in nums:
            if (x + diff) in seen and (x + 2 * diff) in seen:
                count += 1
        return count

