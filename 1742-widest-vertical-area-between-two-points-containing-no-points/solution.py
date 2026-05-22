from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = sorted(p[0] for p in points)
        return max(x_coords[i] - x_coords[i - 1] for i in range(1, len(x_coords)))

