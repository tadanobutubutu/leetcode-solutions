class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)
        idx1 = nums.index(1)
        idxn = nums.index(n)
        
        ans = idx1 + (n - 1 - idxn)
        if idx1 > idxn:
            ans -= 1
        return ans

