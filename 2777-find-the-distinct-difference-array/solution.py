class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        suffix_counts = [0] * (n + 1)
        seen_suffix = set()
        for i in range(n - 1, -1, -1):
            seen_suffix.add(nums[i])
            suffix_counts[i] = len(seen_suffix)
        
        ans = []
        seen_prefix = set()
        for i in range(n):
            seen_prefix.add(nums[i])
            prefix_len = len(seen_prefix)
            suffix_len = suffix_counts[i + 1]
            ans.append(prefix_len - suffix_len)
        return ans

