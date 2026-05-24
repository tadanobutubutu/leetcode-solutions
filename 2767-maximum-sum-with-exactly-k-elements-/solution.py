class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        M = max(nums)
        return k * M + k * (k - 1) // 2

