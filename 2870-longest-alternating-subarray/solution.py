class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -1
        for l in range(n):
            for r in range(l + 1, n):
                expected_diff = 1 if (r - l) % 2 != 0 else -1
                if nums[r] - nums[r - 1] == expected_diff:
                    ans = max(ans, r - l + 1)
                else:
                    break
        return ans

