from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            ans += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        if left == right:
            ans += nums[left]
        return ans

