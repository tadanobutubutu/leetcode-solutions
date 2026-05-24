from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        ans = 0
        for num, freq in counts.items():
            if freq % k == 0:
                ans += num * freq
        return ans

