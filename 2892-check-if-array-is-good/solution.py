class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        if n <= 0:
            return False
        expected = list(range(1, n)) + [n, n]
        return sorted(nums) == expected

