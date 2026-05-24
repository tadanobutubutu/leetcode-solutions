from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        num_set = set(nums)
        ans = []
        for x in range(min_val + 1, max_val):
            if x not in num_set:
                ans.append(x)
        return ans

