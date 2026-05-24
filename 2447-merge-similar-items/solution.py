from typing import List
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = defaultdict(int)
        for val, w in items1:
            weights[val] += w
        for val, w in items2:
            weights[val] += w
        return sorted([[val, w] for val, w in weights.items()])

