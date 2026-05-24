from typing import List

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for x in nums:
            if x == -1:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
            else:
                k = 0
                seen.insert(0, x)
        return ans

