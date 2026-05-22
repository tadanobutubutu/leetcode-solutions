from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(n):
            x = i + 1
            if nums[i] >= x:
                if i + 1 == n or nums[i + 1] < x:
                    return x
        return -1

