from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min = [0] * n
        right_min = [0] * n
        
        cur_min = float('inf')
        for i in range(n):
            left_min[i] = cur_min
            cur_min = min(cur_min, nums[i])
            
        cur_min = float('inf')
        for i in range(n - 1, -1, -1):
            right_min[i] = cur_min
            cur_min = min(cur_min, nums[i])
            
        ans = float('inf')
        for j in range(1, n - 1):
            if left_min[j] < nums[j] and right_min[j] < nums[j]:
                ans = min(ans, left_min[j] + nums[j] + right_min[j])
                
        return ans if ans != float('inf') else -1

