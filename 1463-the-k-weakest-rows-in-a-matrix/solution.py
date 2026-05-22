from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Store tuples of (number of soldiers, row index)
        rows_strength = [(sum(row), i) for i, row in enumerate(mat)]
        # Sort lexicographically: first by number of soldiers, then by row index
        rows_strength.sort()
        # Extract the first k row indices
        return [idx for count, idx in rows_strength[:k]]

