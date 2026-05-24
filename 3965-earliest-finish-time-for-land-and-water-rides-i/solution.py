from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = float('inf')
        
        for i in range(n):
            for j in range(m):
                # Land -> Water
                finish_lw = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]
                # Water -> Land
                finish_wl = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]
                ans = min(ans, finish_lw, finish_wl)
                
        return ans

