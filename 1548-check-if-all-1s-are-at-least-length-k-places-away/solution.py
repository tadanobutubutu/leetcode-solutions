from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = -k - 1
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_idx - 1 < k:
                    return False
                last_idx = i
        return True

