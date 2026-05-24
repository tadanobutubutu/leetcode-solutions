from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        while True:
            # check if non-decreasing
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return operations
                
            if len(nums) < 2:
                return operations
                
            # Find the adjacent pair with the minimum sum (leftmost)
            min_sum = float('inf')
            best_idx = -1
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i+1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    best_idx = i
            
            # Replace the pair at best_idx with their sum
            nums = nums[:best_idx] + [min_sum] + nums[best_idx+2:]
            operations += 1

