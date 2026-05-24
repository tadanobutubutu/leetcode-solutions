from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        jumps = 0
        cur_end = 0
        cur_far = 0
        
        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_far
                if cur_end >= n - 1:
                    break
                    
        return jumps

