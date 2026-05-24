from typing import List
from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        counts = Counter(nums)
        for freq in counts.values():
            if is_prime(freq):
                return True
        return False

