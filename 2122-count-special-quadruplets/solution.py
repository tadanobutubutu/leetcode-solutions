from typing import List
from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        
        for b in range(n - 3, 0, -1):
            c = b + 1
            for d in range(c + 1, n):
                freq[nums[d] - nums[c]] += 1
            
            for a in range(b):
                target = nums[a] + nums[b]
                count += freq[target]
                
        return count

