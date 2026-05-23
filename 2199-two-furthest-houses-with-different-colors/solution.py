from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # Find the furthest house from the left with a different color
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
                
        # Find the furthest house from the right with a different color
        for j in range(n):
            if colors[j] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - j)
                break
                
        return max_dist

