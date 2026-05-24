from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counts = Counter(digits)
        ans = []
        
        # Check all even numbers from 100 to 998
        for x in range(100, 1000, 2):
            d1 = x // 100
            d2 = (x // 10) % 10
            d3 = x % 10
            
            cand_counts = Counter([d1, d2, d3])
            
            possible = True
            for d, req_count in cand_counts.items():
                if counts[d] < req_count:
                    possible = False
                    break
            
            if possible:
                ans.append(x)
                
        return ans

