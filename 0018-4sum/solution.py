from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def kSum(start: int, target: int, k: int) -> List[List[int]]:
            res = []
            if start == len(nums):
                return res
                
            average_value = target // k
            if nums[start] > average_value or target // k > nums[-1]:
                return res
                
            if k == 2:
                return twoSum(start, target)
                
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                for subset in kSum(i + 1, target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
            return res

        def twoSum(start: int, target: int) -> List[List[int]]:
            res = []
            left = start
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return res

        return kSum(0, target, 4)

