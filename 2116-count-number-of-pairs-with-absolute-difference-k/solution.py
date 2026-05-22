from typing import List
from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = Counter()
        ans = 0
        for num in nums:
            ans += counts[num - k] + counts[num + k]
            counts[num] += 1
        return ans

