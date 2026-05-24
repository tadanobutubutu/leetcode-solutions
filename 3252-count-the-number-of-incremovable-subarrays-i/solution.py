from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        for start in range(n):
            for end in range(start, n):
                # nums[start...end] を除外したリスト
                remaining = nums[:start] + nums[end+1:]
                
                # 厳密に単調増加か確認
                is_increasing = True
                for k in range(len(remaining) - 1):
                    if remaining[k] >= remaining[k+1]:
                        is_increasing = False
                        break
                
                if is_increasing:
                    ans += 1
                    
        return ans

