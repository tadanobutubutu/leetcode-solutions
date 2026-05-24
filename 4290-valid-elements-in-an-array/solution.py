class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        left_max = [0] * n
        curr_max = -float('inf')
        for i in range(n):
            left_max[i] = curr_max
            curr_max = max(curr_max, nums[i])
            
        right_max = [0] * n
        curr_max = -float('inf')
        for i in range(n - 1, -1, -1):
            right_max[i] = curr_max
            curr_max = max(curr_max, nums[i])
            
        valid = []
        for i in range(n):
            if i == 0 or i == n - 1:
                valid.append(nums[i])
            elif nums[i] > left_max[i] or nums[i] > right_max[i]:
                valid.append(nums[i])
        return valid

