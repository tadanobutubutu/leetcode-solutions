from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[::2])
        odds = sorted(nums[1::2], reverse=True)
        res = []
        for i in range(len(evens)):
            res.append(evens[i])
            if i < len(odds):
                res.append(odds[i])
        return res

