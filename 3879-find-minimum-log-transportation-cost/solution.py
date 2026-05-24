class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        if n > k:
            return k * (n - k)
        else:
            return k * (m - k)

