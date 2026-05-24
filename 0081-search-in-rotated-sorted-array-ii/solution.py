from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
                
            # 枝刈り・重複処理：両端と中央の値がすべて等しい場合、
            # どちらの側がソート済みか判定できないため、左右の境界を1つ縮める
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # 左側がソートされている場合
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右側がソートされている場合
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False

