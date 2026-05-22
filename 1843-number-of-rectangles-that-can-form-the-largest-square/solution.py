from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        side_lengths = [min(l, w) for l, w in rectangles]
        max_len = max(side_lengths)
        return side_lengths.count(max_len)

