from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        return all(any(start <= x <= end for start, end in ranges) for x in range(left, right + 1))

