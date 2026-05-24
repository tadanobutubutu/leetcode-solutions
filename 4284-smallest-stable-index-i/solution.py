class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        
        curr_max = -1
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            score = curr_max - suffix_min[i]
            if score <= k:
                return i
        return -1

