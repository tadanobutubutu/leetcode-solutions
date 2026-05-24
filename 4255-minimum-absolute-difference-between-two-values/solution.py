class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last_1 = -1
        last_2 = -1
        ans = float('inf')
        
        for i, val in enumerate(nums):
            if val == 1:
                last_1 = i
                if last_2 != -1:
                    ans = min(ans, abs(last_1 - last_2))
            elif val == 2:
                last_2 = i
                if last_1 != -1:
                    ans = min(ans, abs(last_1 - last_2))
                    
        return ans if ans != float('inf') else -1

