from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        for i, c in enumerate(s):
            if c in first:
                dist = i - first[c] - 1
                if dist != distance[ord(c) - 97]:
                    return False
            else:
                first[c] = i
        return True

