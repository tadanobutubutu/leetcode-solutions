from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        unique_nums = sorted(list(set(nums)), reverse=True)
        return unique_nums[:k]

