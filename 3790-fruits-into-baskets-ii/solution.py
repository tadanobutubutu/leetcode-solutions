from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used_baskets = [False] * n
        unplaced_count = 0
        
        for f in fruits:
            placed = False
            for j in range(n):
                if not used_baskets[j] and baskets[j] >= f:
                    used_baskets[j] = True
                    placed = True
                    break
            if not placed:
                unplaced_count += 1
                
        return unplaced_count

