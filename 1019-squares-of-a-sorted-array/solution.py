class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[pos] = nums[l] * nums[l]
                l += 1
            else:
                ans[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return ans

