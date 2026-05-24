from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        prev = -1
        
        for i in range(len(forts)):
            if forts[i] != 0:
                if prev != -1 and forts[prev] != forts[i]:
                    ans = max(ans, i - prev - 1)
                prev = i
                
        return ans

