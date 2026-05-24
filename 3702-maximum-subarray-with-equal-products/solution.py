import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def get_lcm(a, b):
            return (a * b) // math.gcd(a, b)
        
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            current_prod = 1
            current_gcd = 0
            current_lcm = 1
            for j in range(i, n):
                val = nums[j]
                current_prod *= val
                current_gcd = math.gcd(current_gcd, val) if current_gcd != 0 else val
                current_lcm = get_lcm(current_lcm, val)
                
                if current_prod == current_lcm * current_gcd:
                    max_len = max(max_len, j - i + 1)
        return max_len

