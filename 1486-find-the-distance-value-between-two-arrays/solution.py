import bisect
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
            ans += 1
        return ans

