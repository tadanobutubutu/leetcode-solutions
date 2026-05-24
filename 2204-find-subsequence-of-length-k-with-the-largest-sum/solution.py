from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        indexed_nums.sort(key=lambda x: x[1], reverse=True)
        top_k = indexed_nums[:k]
        top_k.sort(key=lambda x: x[0])
        return [val for idx, val in top_k]

