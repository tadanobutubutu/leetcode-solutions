class Solution:
    def maxSum(self, nums: list[int]) -> int:
        max_val = [-1] * 10
        ans = -1
        for x in nums:
            d = max(int(c) for c in str(x))
            if max_val[d] != -1:
                ans = max(ans, max_val[d] + x)
            max_val[d] = max(max_val[d], x)
        return ans

