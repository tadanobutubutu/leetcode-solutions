from collections import defaultdict
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarrays = []
        for i in range(n - k + 1):
            subarrays.append(set(nums[i : i + k]))
            
        counts = defaultdict(int)
        for s in subarrays:
            for val in s:
                counts[val] += 1
                
        candidates = [val for val, count in counts.items() if count == 1]
        if candidates:
            return max(candidates)
        else:
            return -1

