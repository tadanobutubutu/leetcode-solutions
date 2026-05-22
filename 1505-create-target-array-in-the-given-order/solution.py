from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, idx in zip(nums, index):
            target.insert(idx, n)
        return target

