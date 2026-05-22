from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort with a custom key tuple: (number of 1 bits, original value)
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

