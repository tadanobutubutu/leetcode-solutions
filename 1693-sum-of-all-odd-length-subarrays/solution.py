from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        return sum(arr[i] * (((i + 1) * (n - i) + 1) // 2) for i in range(n))

