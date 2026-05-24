from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        last_covered = -1
        for j in range(n):
            if nums[j] == key:
                start = max(last_covered + 1, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    res.append(i)
                last_covered = end
        return res

