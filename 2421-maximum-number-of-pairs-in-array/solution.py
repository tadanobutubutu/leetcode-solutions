from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        pairs = 0
        leftover = 0
        
        for count in counts.values():
            pairs += count // 2
            leftover += count % 2
            
        return [pairs, leftover]

