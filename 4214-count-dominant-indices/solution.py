from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        ans = 0
        suffix_sum = nums[-1]
        suffix_count = 1
        
        for i in range(n - 2, -1, -1):
            if nums[i] > suffix_sum / suffix_count:
                ans += 1
            suffix_sum += nums[i]
            suffix_count += 1
            
        return ans

