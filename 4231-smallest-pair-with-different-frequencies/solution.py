from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        unique_vals = sorted(freq.keys())
        n = len(unique_vals)
        for i in range(n):
            x = unique_vals[i]
            for j in range(i + 1, n):
                y = unique_vals[j]
                if freq[x] != freq[y]:
                    return [x, y]
        return [-1, -1]

