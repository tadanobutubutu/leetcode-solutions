from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for x in nums:
            element_sum += x
            while x > 0:
                digit_sum += x % 10
                x //= 10
        return abs(element_sum - digit_sum)

