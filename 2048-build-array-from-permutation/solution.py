from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # nums[i] = a + b * n
            # a = nums[i] (original value)
            # b = nums[nums[i]] % n (original target value)
            nums[i] = nums[i] + n * (nums[nums[i]] % n)
        
        for i in range(n):
            nums[i] //= n
            
        return nums

