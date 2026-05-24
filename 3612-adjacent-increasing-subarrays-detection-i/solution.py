from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def is_increasing(sub: List[int]) -> bool:
            return all(sub[i] < sub[i+1] for i in range(len(sub) - 1))
            
        for a in range(n - 2 * k + 1):
            if is_increasing(nums[a : a + k]) and is_increasing(nums[a + k : a + 2 * k]):
                return True
                
        return False

