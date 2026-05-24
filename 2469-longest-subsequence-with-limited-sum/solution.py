from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pref = []
        curr = 0
        for x in nums:
            curr += x
            pref.append(curr)
            
        ans = []
        for q in queries:
            ans.append(bisect.bisect_right(pref, q))
        return ans

