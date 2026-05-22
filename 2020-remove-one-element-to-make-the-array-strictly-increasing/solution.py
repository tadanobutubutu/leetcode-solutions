from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def is_increasing(arr: List[int]) -> bool:
            return all(arr[j-1] < arr[j] for j in range(1, len(arr)))
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                # nums[i-1] を削除するか、nums[i] を削除するか試す
                return is_increasing(nums[:i-1] + nums[i:]) or is_increasing(nums[:i] + nums[i+1:])
                
        return True

