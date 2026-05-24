from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            distincts = set()
            for j in range(i, n):
                distincts.add(nums[j])
                ans += len(distincts) ** 2
        return ans

