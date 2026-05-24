class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                ans = max(ans, 1)
                for r in range(l + 1, n):
                    if nums[r] <= threshold and nums[r] % 2 != nums[r - 1] % 2:
                        ans = max(ans, r - l + 1)
                    else:
                        break
        return ans

