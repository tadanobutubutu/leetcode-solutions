class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        z = nums.count(0)
        if z == 0 or z == n:
            return 0
        return nums[:n - z].count(0)

