from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        ans = 0
        for x in nums:
            if x == 0:
                right_sum = total_sum - left_sum
                diff = abs(left_sum - right_sum)
                if diff == 0:
                    ans += 2
                elif diff == 1:
                    ans += 1
            else:
                left_sum += x
        return ans

