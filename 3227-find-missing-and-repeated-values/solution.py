from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        limit = n * n
        counts = [0] * (limit + 1)
        for row in grid:
            for val in row:
                counts[val] += 1
        
        a = -1
        b = -1
        for i in range(1, limit + 1):
            if counts[i] == 2:
                a = i
            elif counts[i] == 0:
                b = i
        return [a, b]

